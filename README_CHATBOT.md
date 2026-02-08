# Customer Support Chatbot with GitHub Copilot SDK

A modern, web-based customer support chatbot powered by GitHub Copilot SDK with real-time streaming responses.

## Features

- 🤖 **AI-Powered Support**: Uses GitHub Copilot's GPT-4.1 model for intelligent responses
- 💬 **Real-time Streaming**: See responses as they're being generated
- 🎨 **Modern UI**: Beautiful, responsive chat interface
- ⚡ **Quick Questions**: Pre-defined questions for common inquiries
- 🔄 **Conversation Context**: Maintains conversation history

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up GitHub Copilot SDK** (if not already done):
   ```bash
   pip install github-copilot-sdk
   ```

## Usage

1. **Start the Chatbot Server**:
   ```bash
   python chatbot_server.py
   ```

2. **Open Your Browser**:
   Navigate to `http://localhost:5000`

3. **Start Chatting**:
   - Type your questions in the input box
   - Click quick question buttons for common queries
   - Watch responses stream in real-time

## Project Structure

```
.
├── chatbot_server.py       # Flask server with Copilot integration
├── templates/
│   └── index.html          # Chat interface UI
├── main.py                 # Original Copilot SDK example
└── requirements.txt        # Python dependencies
```

## How It Works

1. **Backend** (`chatbot_server.py`):
   - Initializes GitHub Copilot SDK client
   - Creates a persistent session for conversations
   - Handles streaming responses via Server-Sent Events (SSE)
   - Manages async operations in Flask

2. **Frontend** (`templates/index.html`):
   - Modern chat interface with smooth animations
   - Real-time message streaming
   - Responsive design for all devices
   - Quick question buttons for common queries

## API Endpoints

- `GET /` - Serves the chat interface
- `POST /api/chat` - Sends messages and streams responses
- `GET /api/health` - Health check endpoint

## Customization

### Change the AI Model
Edit `chatbot_server.py`:
```python
copilot_session = await copilot_client.create_session({
    "model": "gpt-4.1",  # Change to your preferred model
    "streaming": True,
})
```

### Customize Quick Questions
Edit `templates/index.html` in the `<div class="quick-questions">` section.

### Add System Prompt
Modify the `send_message_to_copilot` function:
```python
await copilot_session.send_and_wait({
    "prompt": f"You are a helpful customer support agent. {message}"
})
```

## Troubleshooting

**Port Already in Use**:
```bash
# Change port in chatbot_server.py
app.run(debug=False, host='0.0.0.0', port=5001)  # Use different port
```

**Copilot Not Responding**:
- Check your GitHub Copilot access
- Verify SDK installation: `pip install --upgrade github-copilot-sdk`

## Use Cases

- **Technical Support**: Answer product questions
- **Developer Assistance**: Help with code and APIs
- **Onboarding**: Guide new users
- **Troubleshooting**: Debug issues with customers
- **Documentation**: Provide instant access to information

## Next Steps

Consider adding:
- User authentication
- Conversation history persistence (database)
- Multi-language support
- File upload capability
- Integration with ticketing systems
- Analytics and logging
- Rate limiting
- HTTPS/SSL for production

## License

This project integrates with GitHub Copilot SDK. Check GitHub's terms of service for SDK usage.
