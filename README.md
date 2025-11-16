# 🛫 Indian Airlines IVR System
https://ai-enabled-flight-ivr.onrender.com/

A sophisticated Interactive Voice Response (IVR) system for Indian Airlines built with FastAPI, Twilio, OpenAI, and Redis. Features natural language processing for seamless flight booking, status checking, and cancellation.

## ✨ Features

- **🎯 Digit-Based Menu System**: Easy-to-navigate menu with options 1-9
- **🤖 AI-Powered Conversations**: Natural language understanding using OpenAI GPT-4
- **📞 Twilio Integration**: Production-ready voice call handling
- **💾 Redis Storage**: Fast session management and booking storage
- **🗣️ Indian English Voice**: Natural-sounding voice with Polly.Aditi
- **🔄 Multi-turn Dialogue**: Context-aware conversations
- **📊 Real-time Processing**: Instant speech recognition and response

## 🎯 IVR Menu Options

When customers call, they can:

1. **Press 1** - Book a flight
2. **Press 2** - Check booking status
3. **Press 3** - Cancel a booking
4. **Press 4** - Speak with an agent
5. **Press 9** - Repeat menu

## 🏗️ Architecture

```
┌─────────────┐
│   Customer  │
│    Calls    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Twilio Voice   │
│   (+1978...)    │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│   FastAPI       │
│   Application   │
└──────┬──────────┘
       │
       ├──────────► OpenAI GPT-4 (Natural Language)
       │
       └──────────► Redis (Session & Data Storage)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Redis Server
- Twilio Account
- OpenAI API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd indian-airlines-ivr
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn twilio redis openai python-dotenv pydantic
   ```

4. **Set up Redis**
   ```bash
   # Install Redis (Ubuntu/Debian)
   sudo apt-get install redis-server
   
   # Start Redis
   redis-server
   
   # Or using Docker
   docker run -d -p 6379:6379 redis:latest
   ```

5. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   # Twilio Configuration
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=+19789694592
   
   # OpenAI Configuration
   OPENAI_API_KEY=your_openai_api_key
   
   # Redis Configuration
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_DB=0
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## 🔧 Twilio Configuration

### Setup Webhook URLs

1. Log in to your [Twilio Console](https://console.twilio.com/)
2. Navigate to Phone Numbers → Your Number
3. Configure Voice & Fax:
   - **A CALL COMES IN**: `https://your-domain.com/twilio/incoming_call` (POST)
   - **STATUS CALLBACK URL**: `https://your-domain.com/twilio/status` (POST)

### Expose Local Server (Development)

Use ngrok to expose your local server:
```bash
ngrok http 8000
```

Then use the ngrok URL (e.g., `https://abc123.ngrok.io`) in Twilio webhook configuration.

## 📡 API Endpoints

### Health & Status
- `GET /` - Health check
- `GET /health` - Detailed health status
- `GET /test-ai` - Test OpenAI configuration

### Twilio Webhooks
- `POST /twilio/incoming_call` - Main entry point for calls
- `POST /twilio/gather` - Handle digit input from menu
- `POST /twilio/conversational_gather` - Process speech input
- `POST /twilio/status` - Call status callbacks

### Booking Management
- `GET /bookings` - List all bookings
- `GET /booking/{booking_id}` - Get booking details
- `DELETE /booking/{booking_id}` - Cancel booking

### Debugging
- `GET /sessions` - List active call sessions

## 🎭 Conversation Flow Examples

### Booking a Flight
```
System: "Welcome to Indian Airlines. Press 1 to book a flight..."
User: [Presses 1]
System: "Great! I'll help you book a flight. Please tell me your destination city."
User: "I want to fly to Mumbai"
System: "Perfect! When would you like to travel?"
User: "December 25th"
System: "And what's your name for the booking?"
User: "John Smith"
System: "Perfect! Your flight to Mumbai on December 25th has been booked. 
         Your booking ID is AI20241114123456..."
```

### Checking Booking Status
```
System: "Welcome to Indian Airlines. Press 2 to check your booking..."
User: [Presses 2]
System: "I can help you check your booking. Please provide your booking ID."
User: "AI20241114123456"
System: "Your booking AI20241114123456 is confirmed. 
         Destination: Mumbai. Date: December 25th..."
```

## 🧪 Testing

### Test Health Endpoint
```bash
curl http://localhost:8000/health
```

### Test AI Configuration
```bash
curl http://localhost:8000/test-ai
```

### List Active Sessions
```bash
curl http://localhost:8000/sessions
```

### View All Bookings
```bash
curl http://localhost:8000/bookings
```

## 📊 Data Models

### Booking Structure
```json
{
  "booking_id": "AI20241114123456",
  "passenger_name": "John Smith",
  "destination": "Mumbai",
  "date": "December 25th",
  "created_at": "2024-11-14T10:30:00"
}
```

### Session Structure
```json
{
  "call_sid": "CAxxxxx",
  "from_number": "+1234567890",
  "status": "in-progress",
  "intent": "book_flight",
  "conversation_history": [
    {"role": "user", "content": "I want to fly to Mumbai"},
    {"role": "assistant", "content": "Perfect! When would you like to travel?"}
  ]
}
```

## 🔐 Security Best Practices

1. **Never commit `.env` file** - Contains sensitive credentials
2. **Use environment variables** - For all secrets and configurations
3. **Validate Twilio requests** - Implement request signature validation
4. **Rate limiting** - Implement rate limiting for API endpoints
5. **HTTPS only** - Always use HTTPS in production
6. **Sanitize inputs** - Validate and sanitize all user inputs

## 🚀 Deployment

### Using Docker

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   EXPOSE 8000
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Build and run**
   ```bash
   docker build -t indian-airlines-ivr .
   docker run -p 8000:8000 --env-file .env indian-airlines-ivr
   ```

### Using Cloud Platforms

- **Heroku**: Add `Procfile` with `web: uvicorn main:app --host 0.0.0.0 --port $PORT`
- **AWS**: Deploy using Elastic Beanstalk or ECS
- **Google Cloud**: Deploy using Cloud Run or App Engine
- **Azure**: Deploy using App Service

## 🛠️ Troubleshooting

### Redis Connection Issues
```bash
# Check if Redis is running
redis-cli ping
# Expected output: PONG
```

### OpenAI API Issues
```bash
# Test API key
curl http://localhost:8000/test-ai
```

### Twilio Webhook Issues
- Ensure ngrok is running (development)
- Check webhook URLs in Twilio console
- Verify server is accessible from internet
- Check Twilio debugger for error logs

### Call Quality Issues
- Check internet connection stability
- Verify Twilio account has sufficient balance
- Review call logs in Twilio console

## 📈 Monitoring

Key metrics to monitor:
- Call volume and duration
- Booking conversion rate
- Speech recognition confidence scores
- API response times
- Error rates
- Session cleanup success

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Twilio** - Voice communication platform
- **OpenAI** - Natural language processing
- **FastAPI** - Modern web framework
- **Redis** - Fast data storage

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Contact: support@indianairlines.com
- Documentation: [Link to docs]

## 🔮 Future Enhancements

- [ ] Multi-language support (Hindi, Tamil, Bengali, etc.)
- [ ] Payment integration for booking confirmation
- [ ] SMS confirmation for bookings
- [ ] Email notifications
- [ ] Real-time flight status updates
- [ ] Seat selection capability
- [ ] Loyalty program integration
- [ ] Analytics dashboard
- [ ] Voice biometrics for authentication
- [ ] WhatsApp integration

## 📚 Additional Resources

- [Twilio Voice Documentation](https://www.twilio.com/docs/voice)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Redis Documentation](https://redis.io/documentation)

---

**Made with ❤️ for Indian Airlines**
