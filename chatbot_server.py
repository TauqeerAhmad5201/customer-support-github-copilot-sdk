import asyncio
import sys
from flask import Flask, render_template, request, jsonify, Response
from copilot import CopilotClient
from copilot.generated.session_events import SessionEventType
import threading
import queue
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
# Global client and session
copilot_client = None
copilot_session = None
response_queue = queue.Queue()
background_loop = None
background_thread = None
executor = ThreadPoolExecutor(max_workers=1)

def start_background_loop():
    """Start a background event loop in a separate thread"""
    global background_loop
    background_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(background_loop)
    background_loop.run_forever()

def run_coroutine_in_background(coro):
    """Run a coroutine in the background event loop"""
    return asyncio.run_coroutine_threadsafe(coro, background_loop)

async def initialize_copilot():
    """Initialize the Copilot client and create a session"""
    global copilot_client, copilot_session
    
    copilot_client = CopilotClient()
    await copilot_client.start()
    
    copilot_session = await copilot_client.create_session({
        "model": "gpt-4.1",
        "streaming": True,
    })
    
    # Event handler for streaming responses
    def handle_event(event):
        if event.type == SessionEventType.ASSISTANT_MESSAGE_DELTA:
            response_queue.put(("delta", event.data.delta_content))
        if event.type == SessionEventType.SESSION_IDLE:
            response_queue.put(("done", None))
        if event.type == SessionEventType.ERROR:
            response_queue.put(("error", str(event.data)))
    
    copilot_session.on(handle_event)
    print("✓ Copilot client initialized successfully")

async def send_message_to_copilot(message):
    """Send a message to Copilot and return the response"""
    global copilot_session
    
    # Clear the queue
    while not response_queue.empty():
        response_queue.get()
    
    # Send the message
    await copilot_session.send_and_wait({"prompt": message})

@app.route('/')
def index():
    """Serve the chatbot interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages with streaming response"""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        def generate():
            # Send message using the background event loop
            future = run_coroutine_in_background(send_message_to_copilot(user_message))
            
            # Stream the response
            full_response = ""
            while True:
                try:
                    event_type, data = response_queue.get(timeout=30)
                    
                    if event_type == "delta":
                        full_response += data
                        yield f"data: {data}\n\n"
                    elif event_type == "done":
                        yield "data: [DONE]\n\n"
                        break
                    elif event_type == "error":
                        yield f"data: [ERROR] {data}\n\n"
                        break
                except queue.Empty:
                    yield "data: [TIMEOUT]\n\n"
                    break
            
            # Wait for the coroutine to complete
            try:
                future.result(timeout=1)
            except:
                pass
        
        return Response(generate(), mimetype='text/event-stream')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'copilot_initialized': copilot_session is not None
    })

def initialize_app():
    """Initialize the application"""
    global background_thread
    
    print("Initializing Customer Support Chatbot...")
    
    # Start background event loop
    background_thread = threading.Thread(target=start_background_loop, daemon=True)
    background_thread.start()
    
    # Wait a moment for the loop to start
    import time
    time.sleep(0.5)
    
    # Initialize Copilot in the background loop
    future = run_coroutine_in_background(initialize_copilot())
    future.result()  # Wait for initialization to complete
    
    print("✓ Chatbot ready!")

if __name__ == '__main__':
    initialize_app()
    print("\n" + "="*50)
    print("🤖 Customer Support Chatbot Server Running")
    print("="*50)
    print("Open your browser and visit: http://localhost:5001")
    print("Press Ctrl+C to stop\n")
    
    app.run(debug=False, host='0.0.0.0', port=5001, threaded=True)
