import RPi.GPIO as GPIO

class Wheel(object):
        def __init__(self, in_1, in_2, pwm, stb):
                self.pin1 = in_1
                self.pin2 = in_2

                GPIO.setup(in_1, GPIO.OUT)
                GPIO.setup(in_2, GPIO.OUT)
                GPIO.setup(pwm, GPIO.OUT)
                GPIO.setup(stb, GPIO.OUT)

                GPIO.output(stb, GPIO.HIGH)
                self.pwm = GPIO.PWM(pwm, 60)
	
	def setPwm(self,speed):
                self.pwm.start(speed)
                self.pwm.ChangeDutyCycle(speed)
		
        def forward(self):
                GPIO.output(self.pin1, GPIO.LOW)
                GPIO.output(self.pin2, GPIO.HIGH)
		self.setPwm(100)

        def backward(self):
                GPIO.output(self.pin1, GPIO.HIGH)
                GPIO.output(self.pin2, GPIO.LOW)
		self.setPwm(20)

        def stop(self):
                GPIO.output(self.pin1, GPIO.LOW)
                GPIO.output(self.pin2, GPIO.LOW)

