# Webhook Integration App

This project captures GitHub events (push, pull request, merge) via webhooks and displays them using a Next.js frontend, Flask backend, and MongoDB database.

---

## How to Run

### 1. Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python run.py
```

Flask server runs on `http://localhost:5000`.

### 2. Expose Backend to Internet (for GitHub webhook)

```bash
ngrok http 5000
```

Copy the `https://*.ngrok.io` URL and use it in your GitHub webhook settings:
```
https://<ngrok-subdomain>.ngrok.io/webhook
```

Make sure GitHub Action repo sends POST requests to the above `/webhook` endpoint.


### 3. Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

Runs on `http://localhost:3000`.


## Tech Stack

- **Frontend**: Next.js
- **Backend**: Flask
- **Database**: MongoDB
