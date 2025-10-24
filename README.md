✈️ Twilio Flight Booking IVR Backend

This project implements a simple Interactive Voice Response (IVR) system for a mock airline (Skyline Airlines/Indian Airlines) using FastAPI and Twilio's TwiML.

The backend exposes a series of webhook endpoints that Twilio calls to guide a user through a voice-based process for booking, checking, or canceling a flight.

🚀 Features

Welcome Message: Greets the caller and prompts for the primary action.

Voice Recognition: Uses Twilio's speech-to-text to understand user intent (book, check, or cancel).

Booking Flow: Collects destination and date via voice input.

Check/Cancel Flow: Collects a mock booking ID via voice input.

Twilio Integration: Generates TwiML (XML) responses for all interactions.
