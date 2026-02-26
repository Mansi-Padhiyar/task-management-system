from flask import Blueprint, request, jsonify
from extensions import db
from models import Task

bp = Blueprint("tasks", __name__)

@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()
    return jsonify({
        "id": task.id,
        "title": task.title,
        "status": task.status
    })

@bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {"id": t.id, "title": t.title, "status": t.status}
        for t in tasks
    ])

@bp.route("/tasks/<int:id>/status", methods=["PUT"])
def update_status(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    new_status = data["status"]

    if not task.can_transition(new_status):
        return jsonify({"error": "Invalid state transition"}), 400

    task.status = new_status
    db.session.commit()
    return jsonify({"message": "Updated"})