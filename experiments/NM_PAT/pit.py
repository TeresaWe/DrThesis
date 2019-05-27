#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from psychopy import core, event, iohub, visual, gui, data
from button import Button, ButtonGrid
import time, random, os, sys, glob, threading
from pyo import *

class PIT:
	def __init__(self, rows, cols, buttons, maxTime, myWin, thisExp):
		self.maxTime = maxTime
		self.buttonGrid = ButtonGrid(myWin, buttons, rows=0, cols=6)
		self.buttonGrid.autoDraw = False
		self.io = iohub.launchHubServer()
		self.trialN = 0
		self.myWin = myWin
		self.thisExp = thisExp
		self.instr = visual.TextStim(win=self.myWin, name='instr',
						text=u'+',
						font='Comic Sans',
						pos=(0, 0), height=180, wrapWidth=None, ori=0, 
						color='white', colorSpace='rgb', opacity=1,
						depth=0.0);

		self.freq = SigTo(value=440, time=0.001, init=440)
		self.sine = SineLoop(freq=[self.freq, self.freq], feedback=0.08, mul=.3)
		self.freqTarget = {'C': 261.626 ,'Cis': 277.183,'D' : 293.665,'Dis' : 311.127,'E' : 329.628,'F' : 349.228,'Fis' : 369.994,'G' : 391.995,'Gis' : 415.305,'A' : 440,'B' : 466.164,'H': 493.883}


	def Trial(self, target):
		self.trialN += 1
		self.freq.value = self.freqTarget[target]
		self.sine.out()
		trialClock = core.Clock()
		self.buttonGrid.random()
		clicked = True
		pause = 0
		while trialClock.getTime() + pause < self.maxTime and clicked:			
			for evt in self.io.devices.mouse.getEvents():
			    pos = (evt.x_position, evt.y_position)
			    if evt.type == iohub.constants.EventConstants.MOUSE_BUTTON_PRESS:
			        self.buttonGrid.click(pos)
				clicked = False
			for keys in event.getKeys(timeStamped=True):
				if keys[0] in ['escape', 'q']:
					self.myWin.close()
					self.io.quit()
					core.quit()
				if keys[0] in ['p']:
					self.sine.stop()
					pause = pause + trialClock.getTime()
					while True:
						if 'p' in event.getKeys():
							break;
					self.sine.out()
					trialClock.reset()
			self.buttonGrid.draw()
			self.myWin.flip()

		self.buttonGrid.autoDraw = False
		self.sine.stop()
		self.thisExp.addData('trial number', self.trialN)
		try:
			self.thisExp.addData('answer', self.buttonGrid.checkedLabels()[0])
		except:
			self.thisExp.addData('answer', "")
		self.thisExp.addData('target note', target)	
		self.thisExp.nextEntry()
		self.buttonGrid.reset()


	def TrialHandler(self, targets, reps):
		for i in range(0, reps):
			self.instr.draw()
			self.myWin.flip()
			core.wait(3)
			note = random.choice(targets)
			targets.remove(note)
			self.Trial(note)





