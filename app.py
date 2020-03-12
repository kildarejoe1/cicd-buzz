import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!!!"

@app.route("/user")
def user(user):
    return "Hello User: %s " % user



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
