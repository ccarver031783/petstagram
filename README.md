# Petstagram: React + Django + Kubernetes Microservices

This project is a full-stack web application scaffolded with:

- **Frontend**: React + TypeScript + Vite
- **Backend**: Django + Django REST Framework
- **Orchestration**: Kubernetes Python Operators
- **Dev Environment**: Dockerized with local `venv` support

---

## 🚀 Project Overview

Petstagram is a modular microservice-based platform designed for local development and cloud-native deployment. The signup flow is built with a React frontend and a Django backend, containerized for Kubernetes orchestration via custom Python operators.

---

## 🧩 Tech Stack

### Frontend
- React + TypeScript
- Vite for fast builds and HMR
- ESLint with type-aware linting and React-specific rules

### Backend
- Django
- Django REST Framework
- CORS headers for local API access

### DevOps
- Docker
- Kubernetes (with Python operator logic)
- GitHub Actions (planned for CI/CD and container builds)

---

## 🧪 Local Development

### Setup

```bash
# Clone the repo
git clone https://github.com/your-username/petstagram.git
cd petstagram

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install backend dependencies
pip install -r requirements.txt

# Start Django backend
python manage.py runserver

# Start React frontend
cd frontend
npm install
npm run dev
