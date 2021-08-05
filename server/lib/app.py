from server.util import get_fixture
from flask import Flask


def create_app(test_config=None):
    app = Flask("hypertrophy")

    if test_config:
        app.config.update(test_config)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    @app.route("/exercise/<string:exercise_id>")
    def get_exercise(exercise_id):
        return get_fixture("exercise")

    return app