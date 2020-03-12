import os

import signal

from flask import Flask

import generator



app = Flask(__name__)



signal.signal(signal.SIGINT, lambda s, f: os._exit(0))



@app.route("/")
def home():
    return "Hello World!!!"



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
