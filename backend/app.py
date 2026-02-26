from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "tasks.db"

# Initialize database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()


@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    tasks = [{"id": row[0], "title": row[1]} for row in rows]
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json

    if not data or "title" not in data or data["title"].strip() == "":
        return jsonify({"error": "Title is required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)