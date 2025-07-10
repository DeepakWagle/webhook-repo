from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime, timezone

app = Flask(__name__)
client = MongoClient("mongodb+srv://<username>:<password>@webhook-db.ti2po2o.mongodb.net/?retryWrites=true&w=majority&appName=webhook-db")
db = client["webhookdb"]
events = db["events"]

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("✅ Webhook received:", data)

    event_type = request.headers.get("X-GitHub-Event")

    payload = {}

    if event_type == "push":
        payload = {
            "type": "push",
            "author": data["pusher"]["name"],
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    elif event_type == "pull_request":
        pr = data["pull_request"]
        payload = {
            "type": "pull_request",
            "author": pr["user"]["login"],
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": pr["created_at"]
        }

    if payload:
        print("📝 Inserting into MongoDB:", payload)
        events.insert_one(payload)
        return jsonify({"status": "saved"}), 200

    return jsonify({"status": "ignored"}), 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def get_events():
    data = list(events.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
