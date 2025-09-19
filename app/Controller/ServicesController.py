from flask import Blueprint, render_template, jsonify

services_bp = Blueprint("services", __name__, template_folder="../templates/Services")

class ServicesController:
    def __init__(self):
        pass
    def list_services(self):        
        services = [
            {"id": 1, "name": "Web Development", "description": "Building responsive websites"},
            {"id": 2, "name": "Mobile Apps", "description": "Android/iOS app development"},
            {"id": 3, "name": "Cloud Solutions", "description": "Deployment and cloud support"},
            {"id": 4, "name": "AI & Data", "description": "Data science and machine learning projects"}
        ]
        return services

controller = ServicesController()

@services_bp.route("/")
def index():
    return render_template("Services/index.html", services=controller.list_services())

@services_bp.route("/api")
def api_services():
    return jsonify(controller.list_services())
