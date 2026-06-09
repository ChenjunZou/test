from app import create_app


class TestCreateApp:
    def test_creates_app(self):
        app = create_app()
        assert app is not None

    def test_testing_config(self):
        app = create_app({"TESTING": True})
        assert app.config["TESTING"] is True

    def test_default_not_testing(self):
        app = create_app()
        assert app.config["TESTING"] is False

    def test_custom_config_overrides(self):
        app = create_app({"SECRET_KEY": "custom-key"})
        assert app.config["SECRET_KEY"] == "custom-key"
