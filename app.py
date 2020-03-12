import os

import signal

from flask import Flask

import generator



app = Flask(__name__)



signal.signal(signal.SIGINT, lambda s, f: os._exit(0))



@app.route("/")

def generate_buzz():

    page = '<html><body>'
    page +='<head> <title>Henrys Example</title> <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script> <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script></head>'
    page += '<div class="container"><h1>'
    page += generator.generate_buzz()
    page += '</h1></div></body></html>'

    return page



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
