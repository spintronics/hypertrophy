from flask import Flask

app = Flask("hypertrophy")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"