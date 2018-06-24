import RPi.GPIO as GPIO
from  module.wheel import  Wheel

#Left
INTA1 = 11	#OUT1
INTA2 = 13	#OUT2
PWMA  = 12	#PWM

STB  = 15	#STANDBY

#Right
INTB1 = 31
INTB2 = 33
PWMB = 35


class Car(object):
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		
		self.left_wheel = Wheel(INTA1, INTA2, PWMA, STB)
		self.right_wheel = Wheel(INTB1, INTB2, PWMB, STB)

	def changeSpeed(self,speed):
		self.left_wheel.setPwm(speed)
		self.right_wheel.setPwm(speed)
		
	def forward(self,speed):
		self.left_wheel.forward()
		self.right_wheel.forward()

	def backward(self,speed):
		self.left_wheel.backward()
		self.right_wheel.backward()

	def left(self,speed):
		self.left_wheel.stop()
		self.right_wheel.forward()

	def right(self,speed):
		self.left_wheel.forward()
		self.right_wheel.stop()

	def stop(self):
		self.left_wheel.stop()
		self.right_wheel.stop()

	def shutdown(self):
		self.stop()
		GPIO.cleanup()
