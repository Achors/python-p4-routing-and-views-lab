#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<h1>{param}</h1>'

@app.route('/count/<int:param>')
def count(param):
    num = '\n'.join(map(str, range(1, param + 1)))
    return f'<pre>{num}</pre>'