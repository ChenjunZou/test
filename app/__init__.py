from flask import Flask


def create_app(config=None):
    """Application factory for the personal website."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["TESTING"] = False

    if config:
        app.config.update(config)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
