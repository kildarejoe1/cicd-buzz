import os

import signal

from flask import Flask

import generator



app = Flask(__name__)



signal.signal(signal.SIGINT, lambda s, f: os._exit(0))



@app.route("/")

def generate_buzz():

    page = '<html><body><h1>'

    page += generator.generate_buzz()

    page += '</h1></body><p>Heroku App</html>'

    return page



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
