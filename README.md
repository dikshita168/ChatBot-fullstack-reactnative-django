# 🤖 AI Chatbot — React Native + Django

A full-stack AI chatbot application built using **React Native (Expo)** for the mobile frontend and **Django REST Framework** for the backend.

The application allows users to send messages from a mobile interface, which are processed by the Django backend and connected to an AI service.

---

## 🚀 Tech Stack

### Frontend

- React Native
- Expo
- JavaScript / JSX
- React Native Components
- Fetch API
- Environment Variables

### Backend

- Python
- Django
- Django REST Framework
- REST API

### Database / Infrastructure

- PostgreSQL / SQLite
- Redis
- Docker *(planned)*

### AI

- AI API integration
- Secure API key handling through Django backend

---

## 📱 Features

- 🤖 AI-powered chatbot
- 💬 Real-time chat interface
- 👤 User and bot message bubbles
- 📱 Mobile-friendly React Native UI
- 🔌 Django REST API
- 🔐 Secure API key handling
- 🌐 Frontend-backend communication
- 📝 Conversation history *(planned)*
- 🔑 JWT authentication *(planned)*
- ⚡ Redis caching *(planned)*

---

## 📂 Project Structure

```text
ChatBot-fullstack/
│
├── chatbot-app-FE/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInput.jsx
│   │   │   └── MessageBubble.jsx
│   │   │
│   │   ├── screens/
│   │   │   ├── HomeScreen.jsx
│   │   │   └── ChatScreen.jsx
│   │   │
│   │   ├── services/
│   │   │   └── chatApi.js
│   │   │
│   │   └── styles/
│   │       ├── chatStyles.js
│   │       └── homeStyles.js
│   │
│   ├── App.js
│   ├── package.json
│   └── .env.example
│
├── chatbot-app-BE/
│   │
│   ├── api/
│   ├── chatbot_backend/
│   ├── manage.py
│   ├── requirements.txt
│   └── .env.example
│
├── .gitignore
└── README.md