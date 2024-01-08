#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<h1>{param}</h1>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(map(str, range(1, param + 1)))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = perform_operation(num1, operation, num2)
    return f'<!doctype html><title>Math Result</title><h1>{result}</h1>'

def perform_operation(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero'
        else:
            return num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Error: Modulo by zero'
        else:
            return num1 % num2
    else:
        return 'Error: Invalid operation'
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)