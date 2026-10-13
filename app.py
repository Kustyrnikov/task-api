from flask import Flask, jsonify, abort
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "tasks.json")
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "tasks.json")


def load_tasks():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/")
def index():
    return jsonify({
        "service": "task-api",
        "message": "Simple Flask application inside Docker",
        "endpoints": [
            "/health",
            "/api/tasks",
            "/api/tasks/<id>"
        ]
    })


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/tasks")
def list_tasks():
    return jsonify(load_tasks())


@app.get("/api/tasks/<int:task_id>")
def get_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)

    abort(404, description="Task not found")


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": error.description}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
