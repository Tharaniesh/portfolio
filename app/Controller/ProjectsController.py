from flask import Blueprint, render_template, jsonify


projects_bp = Blueprint("projects", __name__, template_folder="../templates/Projects")

class ProjectsController:
    def __init__(self):
        pass
    def list_projects(self):
        projects = [
            {"id": 1, "name": "Flask App", "status": "Completed"},
            {"id": 2, "name": "Portfolio Website", "status": "In Progress"},
            {"id": 3, "name": "AI Chatbot", "status": "Planned"}
        ]
        return projects
controller = ProjectsController()

@projects_bp.route("/")
def index():
    return render_template("Projects/index.html", projects=controller.list_projects())

@projects_bp.route("/api")
def api_projects():
    return jsonify(controller.list_projects())
