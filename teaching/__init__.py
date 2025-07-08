from flask import Flask


def create_app():
    app = Flask(__name__)

    # Register blueprint
    from .home import home_bp
    app.register_blueprint(home_bp)

    from .about import about_bp
    app.register_blueprint(about_bp)

    return app
