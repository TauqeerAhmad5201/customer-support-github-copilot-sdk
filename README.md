# Customer Support Chatbot with GitHub Copilot SDK

A modern, real-time customer support chatbot powered by GitHub Copilot SDK (GPT-4.1) with a beautiful web interface and streaming responses.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.0+-green.svg)
![GitHub Copilot SDK](https://img.shields.io/badge/GitHub_Copilot-SDK-purple.svg)

## 🌟 Features

- 🤖 **AI-Powered Support**: Leverages GitHub Copilot's GPT-4.1 model for intelligent, context-aware responses
- 💬 **Real-time Streaming**: Watch responses being generated in real-time with smooth animations
- 🎨 **Modern UI**: Beautiful, responsive chat interface with gradient backgrounds
- ⚡ **Quick Questions**: Pre-defined buttons for common customer inquiries
- 🔄 **Conversation Context**: Maintains conversation history throughout the session
- 🌐 **Web-Based**: No installation required for end-users, just open in a browser
- ⚙️ **Easy Customization**: Simple configuration for models, prompts, and UI elements

## 📋 Prerequisites

Before setting up this project, ensure you have:

- **Python 3.8 or higher** installed on your system
- **GitHub Copilot access** (GitHub Copilot Individual, Business, or Enterprise subscription)
- **pip** (Python package installer)
- A modern web browser (Chrome, Firefox, Safari, or Edge)

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/TauqeerAhmad5201/customer-support-github-copilot-sdk.git
cd customer-support-github-copilot-sdk
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Flask** - Web framework for the server
- **github-copilot-sdk** - GitHub's Copilot SDK for AI integration
- **asyncio** - Asynchronous I/O support

### Step 3: Configure GitHub Copilot SDK

The GitHub Copilot SDK requires authentication. Make sure you're signed in to GitHub Copilot:

```bash
# The SDK will use your existing GitHub Copilot authentication
# Ensure you have an active GitHub Copilot subscription
```

**Note**: The Copilot SDK typically uses your existing GitHub authentication. If you encounter authentication issues, ensure that:
1. You have an active GitHub Copilot subscription
2. You're logged into GitHub on your machine
3. Your GitHub CLI or credentials are properly configured

### Step 4: Start the Server

```bash
python chatbot_server.py
```

You should see output similar to:
```
Initializing Customer Support Chatbot...
✓ Copilot client initialized successfully
✓ Chatbot ready!

==================================================
🤖 Customer Support Chatbot Server Running
==================================================
Open your browser and visit: http://localhost:5001
Press Ctrl+C to stop
```

### Step 5: Access the Chatbot

Open your web browser and navigate to:
```
http://localhost:5001
```

You should see the customer support chatbot interface!

## 📁 Project Structure

```
customer-support-github-copilot-sdk/
├── chatbot_server.py       # Flask server with Copilot SDK integration
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Chat interface HTML/CSS/JS
├── README.md              # This file
└── README_CHATBOT.md      # Detailed technical documentation
```

## 🎯 Usage

### Basic Chat

1. Type your question in the input box at the bottom
2. Press Enter or click the Send button
3. Watch as the AI generates a response in real-time

### Quick Questions

Click any of the predefined quick question buttons:
- "How do I reset my password?"
- "What are your business hours?"
- "How can I contact support?"
- "Tell me about your products"

### Chat Features

- **Streaming Responses**: Responses appear character-by-character as they're generated
- **Conversation History**: Previous messages remain visible in the chat window
- **Auto-Scroll**: The chat automatically scrolls to show new messages
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## 🔧 Configuration

### Change the AI Model

Edit `chatbot_server.py` (line 37-40):

```python
copilot_session = await copilot_client.create_session({
    "model": "gpt-4.1",  # Change to your preferred model
    "streaming": True,
})
```

### Change the Server Port

Edit `chatbot_server.py` (line 150):

```python
app.run(debug=False, host='0.0.0.0', port=5001, threaded=True)
# Change port=5001 to your desired port
```

### Customize Quick Questions

Edit `templates/index.html` in the `<div class="quick-questions">` section to add or modify quick question buttons.

### Add a System Prompt

To customize the AI's behavior, modify the `send_message_to_copilot` function in `chatbot_server.py`:

```python
async def send_message_to_copilot(message):
    system_prompt = "You are a helpful and friendly customer support agent."
    await copilot_session.send_and_wait({
        "prompt": f"{system_prompt}\n\nUser: {message}"
    })
```

## 🌐 API Endpoints

The server provides the following REST API endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serves the chat interface HTML |
| `/api/chat` | POST | Accepts chat messages and streams AI responses |
| `/api/health` | GET | Health check endpoint (returns server status) |

### Example API Usage

**Health Check:**
```bash
curl http://localhost:5001/api/health
```

**Send Chat Message:**
```bash
curl -X POST http://localhost:5001/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how can you help me?"}'
```

## 🐛 Troubleshooting

### Port Already in Use

If you see an error that port 5001 is already in use:

```bash
# Option 1: Kill the process using the port
lsof -ti:5001 | xargs kill -9

# Option 2: Change the port in chatbot_server.py
# Edit line 150 to use a different port (e.g., 5002)
```

### Copilot SDK Not Responding

**Issue**: Chatbot doesn't respond or shows connection errors

**Solutions**:
1. Verify your GitHub Copilot subscription is active
2. Ensure you're logged into GitHub
3. Try reinstalling the SDK:
   ```bash
   pip uninstall github-copilot-sdk
   pip install --upgrade github-copilot-sdk
   ```
4. Check if your network allows connections to GitHub's API

### Module Not Found Errors

If you get `ModuleNotFoundError`:

```bash
# Make sure all dependencies are installed
pip install -r requirements.txt

# Or install individually
pip install flask
pip install github-copilot-sdk
```

### Browser Shows "Connection Refused"

**Solution**: Make sure the server is running:
1. Check that `chatbot_server.py` is running without errors
2. Verify the correct port (default: 5001)
3. Try accessing `http://127.0.0.1:5001` instead of `localhost`

## 💡 Use Cases

This chatbot can be adapted for various customer support scenarios:

- **Technical Support**: Answer product and technical questions
- **Developer Assistance**: Help developers with API documentation and code
- **Onboarding**: Guide new users through setup and features
- **Troubleshooting**: Debug issues with customers in real-time
- **FAQ Automation**: Provide instant answers to frequently asked questions
- **Documentation Access**: Give users quick access to documentation
- **Pre-Sales Support**: Answer questions about products and services

## 🔒 Security Considerations

- **API Keys**: The GitHub Copilot SDK uses your GitHub credentials. Keep them secure.
- **Production Deployment**: For production use, consider:
  - Adding HTTPS/SSL encryption
  - Implementing rate limiting
  - Adding user authentication
  - Setting up proper logging and monitoring
  - Configuring CORS policies
- **Data Privacy**: Be mindful of sensitive data sent through the chatbot

## 🚧 Future Enhancements

Consider adding these features:

- [ ] User authentication and session management
- [ ] Persistent conversation history (database storage)
- [ ] Multi-language support
- [ ] File upload capability for screenshots/documents
- [ ] Integration with ticketing systems (Jira, Zendesk, etc.)
- [ ] Analytics and conversation insights
- [ ] Rate limiting and abuse prevention
- [ ] Admin dashboard for monitoring
- [ ] Export conversation transcripts
- [ ] Customizable themes and branding

## 📚 Additional Documentation

For more detailed technical information, see [README_CHATBOT.md](README_CHATBOT.md).

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project integrates with GitHub Copilot SDK. Please review GitHub's terms of service and licensing for SDK usage.

## 🙏 Acknowledgments

- Built with [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
- Powered by [Flask](https://flask.palletsprojects.com/)
- UI inspired by modern chat interfaces

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section above
2. Review the [GitHub Copilot SDK documentation](https://docs.github.com/en/copilot)
3. Open an issue in this repository

---

**Happy Chatting! 🤖💬**
