from flask import Blueprint, render_template, jsonify

# Define a Blueprint for portfolio
portfolio_bp = Blueprint("portfolio", __name__, template_folder="../templates/portfolio")

class PortfolioController:
    def __init__(self):
        pass

    def list_portfolio_items(self):        
        portfolio_items = [
            {"id": 1, "title": "Personal Portfolio Website", "category": "Web Development"},
            {"id": 2, "title": "E-commerce Mobile App", "category": "Mobile Apps"},
            {"id": 3, "title": "Network Analyzer Tool", "category": "Software Project"},
            {"id": 4, "title": "Volunteer Connect App", "category": "Community Project"}
        ]
        return portfolio_items

controller = PortfolioController()

@portfolio_bp.route("/")
def home():
    return render_template("portfolio/home.html", portfolio=controller.list_portfolio_items())

@portfolio_bp.route("/api")
def api_portfolio():
    return jsonify(controller.list_portfolio_items())
