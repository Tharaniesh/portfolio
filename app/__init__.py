from flask import Flask
from conf.db_config import get_db_connection

def create_app():
    app = Flask(__name__)
    try:
        conn = get_db_connection()
        if conn.is_connected():
            print("✅ Database connection established")
            conn.close()
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    from app.routes import main as main_routes
    app.register_blueprint(main_routes)
    try:
        from app.Controller.ServicesController import services_bp
        from app.Controller.ProjectsController import projects_bp
        from app.Controller.PortfolioController import portfolio_bp
        app.register_blueprint(services_bp, url_prefix="/services")
        app.register_blueprint(projects_bp, url_prefix="/projects")
        app.register_blueprint(portfolio_bp, url_prefix="/portfolio")
    except Exception:
        print("⚠ No controllers found yet, only main routes loaded.")
    return app
