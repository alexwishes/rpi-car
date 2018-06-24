# -*- coding: utf-8 -*
from flask import Flask, render_template, request, abort
from module.car import Car

app = Flask(__name__)

car = Car()

@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")

@app.route('/pwm', methods=['GET'])
def setPwm():
    try:
        speed = request.args.get('speed', 0)
    except ValueError:
        abort(404)
    else:
	car.changeSpeed(float(speed))
    return 'ok';

@app.route('/handle', methods=['GET'])
def handle():
    try:
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)
    else:
	if operation == 'forward':
		car.forward(60)
	elif operation == 'backward':
		car.backward(20)
	elif operation == 'right':
		car.right(100)
	elif operation == 'left':
		car.left(100)
	elif operation == 'pause':
		car.stop()
        else:
            abort(404)
    return 'ok'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=False)
