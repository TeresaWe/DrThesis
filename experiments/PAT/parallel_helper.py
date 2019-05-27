from psychopy import parallel
from psychopy import core
import random

class Trigger:
	def send(self, x):
		port = parallel.PParallelLinux(address='/dev/parport0')
		port.setData(x)

	def sendDuration(self, x, duration):
		self.send(x)
		core.wait(duration)
		self.send(x)
