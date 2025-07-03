from flask import Blueprint, request, jsonify
from datetime import datetime
from app.extensions import collection

webhook = Blueprint("Webhook", __name__, url_prefix="/webhook")

@webhook.route("", methods=["POST"])
def receiver():
    event_type = request.headers.get("X-GitHub-Event")
    data = request.json
    event_doc = {}

    if event_type == "push":
        event_doc = {
            "event_type": "push",
            "author": data["pusher"]["name"],
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": datetime.utcnow()
        }

    elif event_type == "pull_request":
        event_doc = {
            "event_type": "pull_request",
            "author": data["pull_request"]["user"]["login"],
            "from_branch": data["pull_request"]["head"]["ref"],
            "to_branch": data["pull_request"]["base"]["ref"],
            "timestamp": datetime.utcnow()
        }

    elif event_type == "merge":
        event_doc = {
            "event_type": "merge",
            "author": data["sender"]["login"],
            "from_branch": data["pull_request"]["head"]["ref"],
            "to_branch": data["pull_request"]["base"]["ref"],
            "timestamp": datetime.utcnow()
        }

    if event_doc:
        collection.insert_one(event_doc)
        return jsonify({"message": "Event stored"}), 200

    return jsonify({"message": "Event ignored"}), 400

@webhook.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find().sort("timestamp", -1))
    for e in events:
        e["_id"] = str(e["_id"])
        e["timestamp"] = e["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")
    return jsonify(events)