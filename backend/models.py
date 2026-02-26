from extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="TODO")

    def can_transition(self, new_status):
        valid_transitions = {
            "TODO": ["IN_PROGRESS"],
            "IN_PROGRESS": ["DONE"],
            "DONE": []
        }

        if new_status not in ["TODO", "IN_PROGRESS", "DONE"]:
            return False

        return new_status in valid_transitions[self.status]