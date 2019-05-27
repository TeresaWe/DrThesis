#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from psychopy import core, event, iohub, visual, gui, data
from button import Button, ButtonGrid
import time, random, os, sys, glob, threading
from pyo import *

class LernPhase:
	def __init__(self, maxTime, myWin):
		self.maxTime = maxTime
		self.myWin = myWin
		self.freq = SigTo(value=440, time=0.001, init=440)
		self.sine = SineLoop(freq=[self.freq, self.freq], feedback=0.08, mul=.3)
		self.freqTarget = {'C': 261.626 ,'Cis': 277.183,'D' : 293.665,'Dis' : 311.127,'E' : 329.628,'F' : 349.228,'Fis' : 369.994,'G' : 391.995,'Gis' : 415.305,'A' : 440,'B' : 466.164,'H': 493.883}
		self.instr = visual.TextStim(win=self.myWin, name='instr',
						text="",
						font='Comic Sans',
						pos=(0, 0), height=160, wrapWidth=None, ori=0, 
						color='white', colorSpace='rgb', opacity=1,
						depth=0.0);

		self.instr2 = visual.TextStim(win=self.myWin, name='instr',
						text="+",
						font='Comic Sans',
						pos=(0, 0), height=180, wrapWidth=None, ori=0, 
						color='white', colorSpace='rgb', opacity=1,
						depth=0.0);

	def Trial(self, note):
		trialClock = core.Clock()
		self.instr.text = note
		self.instr.draw()
		self.freq.value = self.freqTarget[note]		
		self.myWin.flip()
		self.sine.out()
		pause = 0
		while trialClock.getTime() + pause < self.maxTime:
			for keys in event.getKeys(timeStamped=True):
				if keys[0]in ['escape', 'q']:
					self.myWin.close()
					self.sine.stop()
					core.quit()
				if keys[0] in ['p']:
					self.sine.stop()
					pause = pause + trialClock.getTime()
					while True:
						if 'p' in event.getKeys():
							break;
					self.sine.out()
					trialClock.reset()
		self.sine.stop()

	def TrialHandler(self, notes, reps):
		for i in range(0, reps):
			self.instr2.draw()
			self.myWin.flip()
			core.wait(2)
			note = random.choice(notes)
			notes.remove(note)
			self.Trial(note)
