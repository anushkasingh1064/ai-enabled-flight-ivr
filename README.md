# Legacy IVR to Conversational AI Integration

A comprehensive middleware solution for modernizing legacy VXML-based IVR systems with AI-powered natural language understanding capabilities.

---

## Overview

This project implements a complete integration solution connecting legacy VXML-based IVR systems with modern Conversational AI platforms. The system serves as a middleware layer that bridges traditional telephony infrastructure with AI-powered natural language processing capabilities.

### Problem Statement

Legacy IVR systems rely on rigid menu structures and DTMF inputs, leading to poor user experience, limited flexibility, high maintenance costs, and inability to understand natural language.

### Solution

This project provides natural language understanding via OpenAI GPT-4, context-aware conversational flows, seamless integration with existing VXML infrastructure, real-time speech processing via Twilio, and session management with dialogue state tracking.

---

## Project Modules

### Module 1: Legacy System Analysis and Requirements Gathering

**Objective:** Assess current VXML-based systems and define technical and functional integration requirements

**Tasks Completed:**
- Reviewed architecture and capabilities of existing IVR implementations
- Documented integration needs for alignment with ACS and BAP platforms
- Identified technical challenges, constraints, and compatibility gaps

**Key Findings:**
- Identified VXML 2.1 compatibility requirements
- Documented real-time data handling needs (response time < 3 seconds)
- Defined API contract specifications for webhook integration
- Established session management requirements for stateful conversations

**Gap Analysis:**

| Legacy System | Modern Requirement | Solution Implemented |
|---------------|-------------------|---------------------|
| DTMF input only | Natural language | AI-powered NLU with OpenAI GPT-4 |
| Static menu trees | Dynamic dialogue | Intent-based conversational routing |
| No context retention | Context-aware responses | Session-based state management |
| Limited flexibility | Adaptive conversation flows | Multi-turn dialogue handling |

---

### Module 2: Integration Layer Development

**Objective:** Build a middleware/API layer to connect legacy IVRs to the Conversational AI stack

**Tasks Completed:**
- Designed and implemented RESTful API using FastAPI framework
- Created connectors enabling communication between VXML and Twilio
- Ensured real-time data handling with sub-2-second response times
- Validated integration layer with sample transactions and flow testing

**Technical Implementation:**

**Core Components:**
1. **FastAPI Middleware:** RESTful API server handling webhook requests
2. **VXML Handler:** Generates TwiML responses compatible with Twilio
3. **Session Manager:** Maintains conversation state across multiple turns
4. **AI Connector:** Interfaces with OpenAI GPT-4 for natural language processing

**API Endpoints:**
- POST /twilio/voice - Entry point for incoming calls
- POST /twilio/process - Processes user speech input
- POST /twilio/status - Handles call status callbacks
- GET /health - Health check and system status
- GET /sessions - Lists all active call sessions
- GET /session/{call_sid} - Retrieves specific session details
- GET /test-ai - Tests OpenAI API integration

**Integration Patterns:**

Data flow: Twilio receives call → Sends webhook to middleware → Middleware creates session → Returns TwiML response → User speaks → Twilio sends speech-to-text → Middleware processes with AI → Generates response → Converts to TwiML → Twilio speaks to user → Loop continues until completion

---

### Module 3: Conversational AI Interface Development

**Objective:** Introduce natural language capabilities to the IVR system via conversational flows

**Tasks Completed:**
- Developed conversational dialogue flows mapping to existing IVR logic
- Integrated OpenAI GPT-4 for natural language understanding
- Enabled real-time voice input/output handling via Twilio Speech API
- Implemented intent recognition and entity extraction
- Created multi-turn dialogue management system

**AI Capabilities:**

**Intent Recognition:**
- book_flight: User wants to make a flight reservation
- check_booking: Query existing booking status
- cancel_booking: Cancel an existing reservation
- unknown: Requires clarification

**Entity Extraction:**
- Destinations: Automatically extracts city names (Mumbai, Delhi, Bangalore, etc.)
- Dates: Understands relative dates (tomorrow, next Friday) and absolute dates
- Booking IDs: Extracts alphanumeric booking identifiers
- Passenger Names: Captures full names from speech

**Dialogue Management:**
- Maintains conversation history across multiple turns
- Tracks collected information throughout the call
- Handles context switches gracefully
- Provides clarifying questions when input is ambiguous
- Generates natural, conversational responses

---

## System Architecture

### Architecture Overview

```
User Layer:
- Phone Call from Customer
- Voice input/output

Telephony Layer (Twilio):
- Phone Number: +19789694592
- Speech-to-Text (Enhanced, Indian English)
- Text-to-Speech (Amazon Polly - Aditi voice)
- Call routing and management
- Webhook communication via TwiML

Integration Layer (Middleware - FastAPI):
- Main Application (main.py)
  - Request routing and handling
  - Webhook endpoint management
  - Response generation

- VXML Handler
  - Generates TwiML responses
  - Converts AI responses to voice format
  - Manages speech gathering

- Session Manager
  - Creates and tracks call sessions
  - Maintains conversation history
  - Stores user context and collected data
  - Automatic cleanup on call end

- AI Connector
  - Interfaces with OpenAI GPT-4
  - Sends conversation context
  - Receives intent and entities
  - Generates conversational responses

Conversational AI Layer (OpenAI):
- GPT-4 Model
- Natural Language Understanding
- Intent classification
- Entity extraction
- Context-aware response generation

Data Layer:
- Session Storage (In-memory for development)
- Conversation history
- User context and state
- Collected transaction data
```

### Request/Response Flow

**Incoming Call Flow:**
1. Customer calls +19789694592
2. Twilio receives call, POSTs to /twilio/voice
3. Middleware creates new session with unique call_sid
4. Returns TwiML with welcome message
5. Twilio speaks: "Welcome to Indian Airlines! How may I help you?"
6. Gathers user speech input

**Conversation Processing Flow:**
1. User speaks their request
2. Twilio converts speech to text (Speech-to-Text)
3. POSTs to /twilio/process with SpeechResult
4. Middleware retrieves session by call_sid
5. Adds user message to conversation history
6. Sends conversation to OpenAI GPT-4 with system prompt
7. GPT-4 analyzes intent, extracts entities, generates response
8. Response includes: intent, message, collected_info, completion status
9. Middleware updates session with AI response
10. Generates TwiML with AI message
11. Returns to Twilio
12. Twilio speaks AI response to user (Text-to-Speech)
13. Gathers next input if conversation incomplete
14. Repeats until transaction complete

**Session Management:**
- Each call gets unique session with call_sid
- Session stores: conversation_history, intent, collected_info, timestamps
- Sessions cleaned up automatically when call ends
- Can handle multiple concurrent calls independently

---

## Technology Stack

**Backend Framework:**
- Python 3.9+
- FastAPI 0.104.1 (Web framework)
- Uvicorn 0.24.0 (ASGI server)
- Pydantic 2.5.0 (Data validation)

**Voice & Telephony:**
- Twilio Voice API (Phone system integration)
- Twilio Speech Recognition (Speech-to-Text, Enhanced, en-IN)
- Amazon Polly (Text-to-Speech, Aditi voice for Indian English)
- Phone Number: +19789694592

**AI & Natural Language Processing:**
- OpenAI GPT-4 (Natural language understanding)
- Custom system prompts for intent recognition
- Automatic entity extraction
- Context-aware dialogue management

**Development Tools:**
- python-dotenv (Environment variable management)
- Git/GitHub (Version control)
- VS Code (Development environment)

**Deployment:**
- Azure App Service (Production hosting)
- ngrok (Local development tunneling)

---

## Installation Guide

### Prerequisites

- Python 3.9 or higher installed
- pip package manager
- Twilio account with phone number
- OpenAI API account and API key
- Git installed

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/legacy-ivr-ai-integration.git
cd legacy-ivr-ai-integration
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

You should see (venv) in your terminal prompt after activation.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages (requirements.txt):
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
twilio==8.10.0
openai==1.3.0
python-dotenv==1.0.0
pydantic==2.5.0
```

### Step 4: Configure Environment Variables

Create a file named .env in the project root directory:

```bash
# Create .env file
# Windows:
type nul > .env

# Mac/Linux:
touch .env
```

Add the following to .env file:

```
# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Twilio Configuration
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=+19789694592

# Application Settings
ENVIRONMENT=development
DEBUG=True
```

**How to get API keys:**

**OpenAI API Key:**
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key (starts with sk-)
6. Paste in .env file

**Twilio Credentials:**
1. Go to https://console.twilio.com/
2. Find Account SID and Auth Token on dashboard
3. Copy and paste into .env file

### Step 5: Run the Application

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Expected output:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Keep this terminal running - this is your server.

### Step 6: Verify Installation

Open a NEW terminal (keep server running) and test:

```bash
# Test health endpoint
curl http://localhost:8000/health

# Expected response:
# {"status":"healthy","openai_configured":true,"twilio_number":"+19789694592","active_calls":0}

# Test AI integration
curl http://localhost:8000/test-ai

# Expected response:
# {"status":"ok","message":"OpenAI API is working!"}
```

Or open in browser: http://localhost:8000/health

---

## Configuration

### Twilio Webhook Setup

To connect your Twilio phone number to the middleware:

**Step 1: Make Your Local Server Publicly Accessible**

**Option A: Using ngrok (for testing)**

In a NEW terminal (keep server running):

```bash
# Download ngrok from https://ngrok.com/download
# Then run:
ngrok http 8000
```

You'll see output like:
```
Forwarding  https://abc123.ngrok-free.app -> http://localhost:8000
```

Copy that HTTPS URL (the ngrok URL).

**Option B: Deploy to Azure (for production)**

```bash
# Install Azure CLI, then:
az login

az webapp up \
  --name indian-airlines-ivr \
  --resource-group ivr-rg \
  --runtime "PYTHON:3.9" \
  --sku B1

# Your URL will be: https://indian-airlines-ivr.azurewebsites.net
```

**Step 2: Configure Twilio Console**

1. Go to https://console.twilio.com/
2. Navigate to Phone Numbers → Manage → Active Numbers
3. Click on your number (+19789694592)
4. Scroll to "Voice Configuration" section
5. Under "A Call Comes In":
   - Select: Webhook
   - HTTP POST
   - URL: https://your-ngrok-url.ngrok-free.app/twilio/voice
   (or your Azure URL: https://indian-airlines-ivr.azurewebsites.net/twilio/voice)
6. Under "Status Callback URL":
   - URL: https://your-url/twilio/status
   - HTTP POST
7. Click Save

---

## Usage

### Testing the System

**Via Phone Call:**

Call +1 (978) 969-4592 and try these conversations:

**Example 1 - Flight Booking:**
```
AI: "Welcome to Indian Airlines! How may I help you?"
You: "I want to book a flight"
AI: "I can help you book a flight. Where would you like to fly to?"
You: "Mumbai"
AI: "Great! When would you like to travel to Mumbai?"
You: "Tomorrow"
AI: "Perfect! What's your name for the booking?"
You: "John Smith"
AI: "Booking confirmed for John Smith to Mumbai tomorrow. Booking ID: AI20251022145623"
```

**Example 2 - Natural Language:**
```
You: "I need to fly to Delhi next Friday"
AI: "Got it! Flight to Delhi on [date]. What's your name for the booking?"
You: "Sarah"
AI: "Perfect! Your flight is booked, Sarah."
```

**Example 3 - Check Booking:**
```
You: "Check my booking"
AI: "I can check that for you. What's your booking ID?"
You: "AI20251022145623"
AI: "Your booking is confirmed and on schedule."
```

**Via API:**

```bash
# Check system health
curl http://localhost:8000/health

# View active sessions
curl http://localhost:8000/sessions

# Get specific session details
curl http://localhost:8000/session/CALL_SID_HERE

# Test AI integration
curl http://localhost:8000/test-ai
```

**Via Browser:**

Open http://localhost:8000/docs for interactive API documentation (Swagger UI).

---

## API Documentation

### Endpoints

**POST /twilio/voice**
- Description: Entry point for incoming calls from Twilio
- Called by: Twilio when call is received
- Returns: TwiML with welcome message
- Creates new session for the call

**POST /twilio/process**
- Description: Processes user speech input
- Called by: Twilio after capturing user's voice
- Receives: SpeechResult (user's spoken words)
- Processes through OpenAI GPT-4
- Returns: TwiML with AI-generated response

**POST /twilio/status**
- Description: Receives call status updates
- Called by: Twilio for call events
- Handles cleanup when call ends

**GET /health**
- Description: Health check endpoint
- Returns: System status, OpenAI config status, active calls count
- Use for monitoring

**GET /sessions**
- Description: List all active call sessions
- Returns: Array of active sessions with details

**GET /session/{call_sid}**
- Description: Get detailed information about specific session
- Returns: Full session data including conversation history

**GET /test-ai**
- Description: Test OpenAI API integration
- Returns: Success or error status
- Use for debugging AI connection

---

## Deployment to Azure

### Prerequisites

- Azure account (free tier available)
- Azure CLI installed

### Deployment Steps

**Step 1: Install Azure CLI**

Windows:
```bash
winget install Microsoft.AzureCLI
```

Mac:
```bash
brew install azure-cli
```

Linux:
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Step 2: Login to Azure**

```bash
az login
```

Your browser will open for authentication.

**Step 3: Deploy Application**

```bash
# Navigate to project directory
cd legacy-ivr-ai-integration

# Deploy
az webapp up \
  --name indian-airlines-ivr \
  --resource-group ivr-integration-rg \
  --runtime "PYTHON:3.9" \
  --sku B1 \
  --location centralindia
```

Wait 3-5 minutes for deployment to complete.

**Step 4: Configure Environment Variables in Azure**

```bash
az webapp config appsettings set \
  --name indian-airlines-ivr \
  --resource-group ivr-integration-rg \
  --settings \
    OPENAI_API_KEY="your-openai-key" \
    TWILIO_ACCOUNT_SID="your-twilio-sid" \
    TWILIO_AUTH_TOKEN="your-twilio-token" \
    TWILIO_PHONE_NUMBER="+19789694592" \
    ENVIRONMENT="production"
```

**Step 5: Verify Deployment**

```bash
# Check if app is running
curl https://indian-airlines-ivr.azurewebsites.net/health

# Or open in browser
```

**Step 6: Update Twilio Webhooks**

Update your Twilio webhook URLs to:
- Voice: https://indian-airlines-ivr.azurewebsites.net/twilio/voice
- Status: https://indian-airlines-ivr.azurewebsites.net/twilio/status

**Monitoring Deployment:**

```bash
# View logs
az webapp log tail \
  --name indian-airlines-ivr \
  --resource-group ivr-integration-rg

# Stop app
az webapp stop --name indian-airlines-ivr --resource-group ivr-integration-rg

# Start app
az webapp start --name indian-airlines-ivr --resource-group ivr-integration-rg

# Delete app
az webapp delete --name indian-airlines-ivr --resource-group ivr-integration-rg
```

---

## Testing

### Manual Testing Checklist

**Phone Call Tests:**
- [ ] Call connects and welcome message plays
- [ ] System understands "book a flight"
- [ ] Collects destination correctly
- [ ] Collects date correctly
- [ ] Collects passenger name
- [ ] Generates booking confirmation
- [ ] Understands "check booking"
- [ ] Understands "cancel booking"
- [ ] Handles unclear input with clarifying questions
- [ ] Context maintained across multiple turns

**API Tests:**
```bash
# Health check
curl http://localhost:8000/health

# OpenAI integration
curl http://localhost:8000/test-ai

# Active sessions
curl http://localhost:8000/sessions
```

**Browser Tests:**
- Open http://localhost:8000/docs
- Test each endpoint using Swagger UI
- Verify responses are correct

### Test Scenarios

**Scenario 1: Simple Booking**
- Input: "Book a flight"
- Expected: Asks for destination

**Scenario 2: Complete Information**
- Input: "Book a flight to Mumbai tomorrow for John"
- Expected: Extracts all information and confirms

**Scenario 3: Context Retention**
- Input: "Book a flight"
- Response: "Where to?"
- Input: "Actually, check my booking first"
- Expected: Switches context smoothly

**Scenario 4: Ambiguous Input**
- Input: "Umm... I want to... maybe... book?"
- Expected: Asks clarifying question

---

## Project Structure

```
legacy-ivr-ai-integration/
├── main.py                 # Main FastAPI application with all logic
├── requirements.txt        # Python package dependencies
├── .env                    # Environment variables (not in git)
├── .env.template          # Template for environment variables
├── .gitignore             # Git ignore rules
├── README.md              # This documentation file
└── LICENSE                # MIT License
```

---

## Key Features

**Natural Language Understanding:**
- Understands variations in phrasing
- No need for exact keywords
- Handles Indian English effectively

**Context Awareness:**
- Remembers conversation history
- Tracks information across turns
- Handles topic switches

**Intent Recognition:**
- Automatically detects user goals
- No rigid menu navigation required
- Dynamic response generation

**Entity Extraction:**
- Extracts dates (relative and absolute)
- Identifies city names
- Captures booking IDs
- Recognizes passenger names

**Error Handling:**
- Gracefully handles unclear input
- Asks clarifying questions
- Falls back to agent if needed
- Comprehensive logging

**Session Management:**
- Unique session per call
- Automatic cleanup
- Conversation history preserved
- State tracking across interactions

---

## Troubleshooting

**Problem: "OpenAI API key invalid"**

Solution:
```bash
# Check .env file
cat .env | grep OPENAI

# Verify key starts with "sk-"
# Generate new key at https://platform.openai.com/api-keys
```

**Problem: "Twilio webhooks not working"**

Solution:
- Verify ngrok is running if testing locally
- Check webhook URLs in Twilio console are correct
- Ensure URLs use HTTPS (not HTTP)
- Check server is running and accessible

**Problem: "Call connects but no AI response"**

Solution:
```bash
# Check OpenAI is configured
curl http://localhost:8000/test-ai

# Check logs in terminal where uvicorn is running
# Look for error messages
```

**Problem: "ModuleNotFoundError"**

Solution:
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**Problem: "ngrok command not found"**

Solution:
- Download from https://ngrok.com/download
- Extract to a folder
- Run from that folder: ./ngrok http 8000
- Or add to PATH

---

## Module Completion Summary

**Module 1: Legacy System Analysis ✓**
- Analyzed VXML-based IVR architecture
- Documented integration requirements
- Identified technical constraints
- Completed gap analysis

**Module 2: Integration Layer ✓**
- Built FastAPI middleware
- Implemented VXML/TwiML handlers
- Created session management system
- Validated with transaction testing

**Module 3: Conversational AI ✓**
- Integrated OpenAI GPT-4
- Developed dialogue flows
- Implemented intent recognition
- Enabled real-time voice processing

---

## Future Enhancements

- Multi-language support (Hindi, Tamil, Bengali)
- Database persistence with PostgreSQL
- Redis for distributed session storage
- Voice biometrics authentication
- Real-time analytics dashboard
- SMS and email confirmations
- Call recording and transcription
- Advanced sentiment analysis
- WebSocket support for live monitoring

---

## License

This project is licensed under the MIT License.

---

**Live Demo:** Call +1 (978) 969-4592

---

## Acknowledgments

- OpenAI for GPT-4 API
- Twilio for Voice services
- FastAPI framework
- Microsoft Azure for cloud hosting
- Python community for excellent libraries
