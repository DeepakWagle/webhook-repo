# 📦 GitHub Webhook Listener – Flask + MongoDB + UI

This project listens to GitHub Webhook events (Push and Pull Request) and logs them in MongoDB Atlas. A simple Flask-based UI fetches and displays the latest events every 15 seconds.

---

## 🚀 Features

- ✅ Receives GitHub Webhook events via `/webhook`
- ✅ Handles both `push` and `pull_request` events
- ✅ Stores parsed data in MongoDB Atlas
- ✅ `/events` API to fetch event logs
- ✅ Frontend UI updates automatically

---

## ⚙️ Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| Backend      | Python Flask             |
| Frontend     | HTML + JavaScript        |
| Database     | MongoDB Atlas            |
| Tunnel       | Ngrok                    |
| Integration  | GitHub Webhooks          |

---

## 📂 Project Structure
```

webhook-repo/
├── app.py              # Flask app (webhook + events)
├── templates/
│   └── index.html        # Frontend
├── requirements.txt    # Dependencies
└── README.md           # This file
```
---

## 📦 Setup Instructions (Step-by-Step)

### 1. Clone the Repository

```bash
git clone https://github.com/DeepakWagle/webhook-repo.git
cd webhook-repo
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. MongoDB Atlas Setup
- Create a free cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Add your IP (or `0.0.0.0/0`)
- Get your connection URI and update it in `app.py`:

```python
client = MongoClient("your-connection-string")
```

### 4. Run the Flask App
```bash
python app.py
```
Server runs at:
http://127.0.0.1:5000/

### 5. Run Ngrok to Expose It
```bash
ngrok http 5000
```
Ngrok gives a URL like:
https://abcd-1234.ngrok-free.app

Leave this terminal open.

### 6. Configure GitHub Webhook
In your action-repo:

Go to Settings → Webhooks → Add Webhook

Use this payload URL:
- Payload URL: `https://abcd-1234.ngrok-free.app/webhook`
- Content type: `application/json`
- Events: Push + Pull Request


### 7. Trigger GitHub Events
Push:
```bash
echo "test" >> test.txt
git add .
git commit -m "Test webhook"
git push origin main
```

Pull Request:
```bash
git checkout -b test-pr
echo "PR test" >> pr.txt
git add .
git commit -m "Testing PR"
git push origin test-pr
```
Then go to GitHub and open a PR from test-pr → main.

### 8. View Events in Browser
Local URL:
http://127.0.0.1:5000/

Ngrok URL (example):
https://abcd-1234.ngrok-free.app/

Expected output:

DeepakWagle pushed to main on 2025-07-05T07:09:15.308084+00:00  
DeepakWagle submitted a pull request from feature-pr-test to main on 2025-07-05T07:13:18Z

---

## 📽️ Demo Video

🎥 [Watch Demo Here](https://www.loom.com/share/fcd8a2aff560428395e9006564e654d6?sid=24b59bc0-6955-46c3-a9ee-6f02c1f8e5b7)


## 🙋‍♂️ Author
**Deepak Wagle**  
Python Fullstack Developer Applicant  
[GitHub: DeepakWagle](https://github.com/DeepakWagle)


---
### ✅ Next Step: Save → Commit → Push

```bash
git add README.md
git commit -m "Clean up and finalize README for Techstax"
git push