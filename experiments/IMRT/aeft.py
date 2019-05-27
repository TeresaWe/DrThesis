# Neue AEFT-Version (26.05.17)
# Letztes Update 31.05.2017

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
import numpy as np
import os  
import threading
import sys  



# declaration of global variables (used by response pad)
global green, left, right
right = False
left = False
green = False

def StartResponsePad():
	import pyxid
	global right, left, green

	dev = pyxid.get_xid_devices()[0]
	dev.reset_base_timer()

	while True:
		dev.poll_for_response()
		if dev.response_queue_size() > 0:
			response = dev.get_next_response()
			if response['pressed'] == True:
				if response['key'] == 3:
					right = True
				if response['key'] == 7:
					green = True
				if response['key'] == 2:
					left = True

def StartRPThread():
	rp = threading.Thread(target=StartResponsePad)
	rp.daemon = True
	rp.start()

class Trial:
	def __init__(self, condition, minID, maxID):
		trial_handler = data.TrialHandler(nReps=1, method='sequential',
		trialList=data.importConditions(condition, selection='0:145'),
		seed=None, name='Block_1')

		self.TrialData = trial_handler.trialList
		self.LastTrial = 0
		self.ActiveTrial = 0
		self.minID = minID
		self.maxID = maxID
		self.correct = 0
		self.meanTime = 0

	def NextTrial(self):
		self.LastTrial = self.ActiveTrial
		try:
			ID = np.random.randint(self.minID, self.maxID)
		#	print("ID: " + str(ID)) (only for debugging purposes)
		except:
			print("ERROR: Trial List empty.")
			raise 
		self.ActiveTrial = self.TrialData[ID]
		try:
			self.TrialData.pop(ID)
		except:
			print("ERROR: Trial List empty.")
			raise
		self.maxID += -1

	def TrialBlock(self, number):
		global left, right
		self.Clock = core.Clock()

		Achtung = visual.TextStim(win=myWin, name='Achtung',
    		text='Achtung!',
    		font='Arial',
    		pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    		color='white', colorSpace='rgb', opacity=1,
    		depth=0.0);

		continueRoutine = True
		continueTrial = True
		self.N = 0
		self.N2 = self.maxID - self.minID

		while continueTrial:
			if self.N + 1 >= self.N2:
					continueTrial = False

			self.NextTrial()

			target = sound.Sound(self.ActiveTrial['file_target'], secs=-1)
			interleaved = sound.Sound(self.ActiveTrial['file_interleaved'], secs=-1)

			targetStatus = 0
			interleavedStatus = 0
			continueRoutine_Buffer = False
			continueRoutine = True
			firstPress = True

			self.Clock.reset()

			while continueRoutine:
				t = self.Clock.getTime()

				if t <= 5.4:
					right = False
					left = False

				if t >= 1 and targetStatus == 0:
					Achtung.draw()
					myWin.flip()

				if t >= 2 and targetStatus == 0:
					myWin.flip()
					target.play()
					targetStatus = 1

				if t >= 5.4 and interleavedStatus == 0:
					interleaved.play()
					interleavedStatus = 1

				if right and firstPress and interleavedStatus == 1:
					continueRoutine_Buffer = True
					right = False
					firstPress = False
					answer = "n"
					tKey = t - 5.4

				if left and firstPress and interleavedStatus == 1:
					continueRoutine_Buffer = True
					left = False
					firstPress = False
					answer = "c"
					tKey = t - 5.4

				if continueRoutine_Buffer and interleavedStatus == 1 and t >= 7.4:
					continueRoutine = False

				if interleavedStatus == 1 and t >= 9:
					answer = "none"
					tKey = -1
					continueRoutine = False

				if event.getKeys(keyList=["escape"]):
					core.quit()

			thisExp.addData('file_target',self.ActiveTrial['file_target'])
			thisExp.addData('file_interleaved',self.ActiveTrial['file_interleaved'])
			thisExp.addData('cond',self.ActiveTrial['cond'])
			thisExp.addData('target',self.ActiveTrial['target'])
			thisExp.addData('Ans_corr',self.ActiveTrial['Ans_corr'])
			thisExp.addData('cond_inside',self.ActiveTrial['cond_inside'])
			thisExp.addData('block_number', number)
			thisExp.addData('trial_number', self.N)
			thisExp.addData('time', tKey)
			thisExp.addData('answer', answer)
			if answer == str(self.ActiveTrial['Ans_corr']):
				thisExp.addData('correct answer?', 1)
				self.correct += 1
			else:
				thisExp.addData('correct answer?', 0)

			thisExp.nextEntry()

			self.meanTime += tKey / 16
			self.N += 1


if __name__ == "__main__":

	### Init of Psychopy stuff
	expName = 'AEFT'  #
	expInfo = {u'session': u'001', u'participant': u'' , u'condition type': ['A', 'B']}
	dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
	if dlg.OK == False:
		core.quit()  # user pressed cancel
	expInfo['date'] = data.getDateStr()  # add a simple timestamp
	expInfo['expName'] = expName
	if expInfo['condition type'] == "A":
		conditions = "conditions_FormA.csv"
	if expInfo['condition type'] == "B":
		conditions = "conditions_FormB.csv"
	

	filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

	thisExp = data.ExperimentHandler(name=expName, version='',
    	extraInfo=expInfo, runtimeInfo=None,
    	originPath=None,
    	savePickle=True, saveWideText=True,
    	dataFileName=filename)

	global myWin
	myWin = visual.Window(size=(1920, 1200), fullscr=True, allowGUI=False,winType='pyglet',
	monitor='testMonitor', screen=0, color=[-1.000,-1.000,-1.000], colorSpace='rgb',
	blendMode='avg')

	# Init of response pad
	StartRPThread()

	# Instructions
	continueInstruction = True
	while continueInstruction:
		head_geninstr = visual.TextStim(win=myWin, name='head_geninstr',
	    text='Welcome!',
	    font='Comic Sans',
	    pos=(0, 0.7), height=0.1, wrapWidth=1.5, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=0.0);
		main_geninstr = visual.TextStim(win=myWin, name='main_geninstr',
	    text=u'In this task you will hear a melody, consisting 6 tones, played on an electronic piano. After that, you will hear a sequence of two mixed melodies. Sometimes the melody which you heard first will be included but entangled with another melody. In the other cases the melody will not be inlcuded in the mixed sequence. \n\n\n\n',
	    font='Arial',
	    pos=(0, 0), height=0.065, wrapWidth=1.5, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-1.0);
		foot_geninstr = visual.TextStim(win=myWin, name='foot_geninstr',
	    text=u'Continue with the green button!',
	    font='Arial',
	    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-2.0);

		head_geninstr.draw()
		main_geninstr.draw()
		foot_geninstr.draw()
		myWin.flip()

		if event.getKeys(keyList=["escape"]):
					core.quit()

		if green:
			continueInstruction = False
			green = False

	continueInstruction = True
	while continueInstruction:
		main_geninstr_2 = visual.TextStim(win=myWin, name='main_geninstr_2',
	    text=u'After you have heard the melody and the mixed sequence, you should decide if the melody was included in the mixed sequence. Press the button on the right-hand side if the melody was included, on the left-hand side if not. Please try to be as fast as possible. Press the green button to continue with a short trial.',
	    font='Arial',
	    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=0.0);
		foot_geninstr_2 = visual.TextStim(win=myWin, name='foot_geninstr_2',
	    text=u'Continue with the green button!',
	    font='Arial',
	    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-1.0);

		main_geninstr_2.draw()
		foot_geninstr_2.draw()
		myWin.flip()

		if event.getKeys(keyList=["escape"]):
					core.quit()

		if green:
			continueInstruction = False
			green = False

	# Practice Block
	trial = Trial(conditions, 0, 16)
	trial.TrialBlock("practice")

	msg = "You have answered %i stimuli correctly. \n (reaction time=%.2f s)" %(trial.correct , trial.meanTime)


	continueInstruction = True
	while continueInstruction:
		head_feedback = visual.TextStim(win=myWin, name='head_feedback',
	    text=u'Trial finished!',
	    font='Arial',
	    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-1.0);
		main_feedback = visual.TextStim(win=myWin, name='main_feedback',
	    text=msg,
	    font='Arial',
	    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-2.0);
		foot_feedback = visual.TextStim(win=myWin, name='foot_feedback',
	    text=u'Continue with the green button!',
	    font='Arial',
	    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-3.0);

		head_feedback.draw()
		main_feedback.draw()
		foot_feedback.draw()
		myWin.flip()

		if event.getKeys(keyList=["escape"]):
					core.quit()

		if green:
			continueInstruction = False
			green = False

	continueInstruction = True
	while continueInstruction:
		head_begin = visual.TextStim(win=myWin, name='head_begin',
	    text='Start of the experiment',
	    font='Arial',
	    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=0.0);
		main_begin = visual.TextStim(win=myWin, name='main_begin',
	    text='First part. You are now well prepared for the experiment. If you have any questions, please ask the supervisor.',
	    font='Arial',
	    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-1.0);
		foot_begin = visual.TextStim(win=myWin, name='foot_begin',
	    text=u'Continue with the green button!',
	    font='Arial',
	    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-3.0);

		head_begin.draw()
		main_begin.draw()
		foot_begin.draw()
		myWin.flip()

		if event.getKeys(keyList=["escape"]):
					core.quit()

		if green:
			continueInstruction = False
			green = False

	# First 8 trials
	trial = Trial(conditions, 16,  80)
	trial.TrialBlock(1)

	continueInstruction = True
	while continueInstruction:
		main_begin_2 = visual.TextStim(win=myWin, name='main_begin_2',
	    text='Break!',
	    font='Arial',
	    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=0.0);
		foot_begin_2 = visual.TextStim(win=myWin, name='foot_begin_2',
	    text=u'Continue with the green button!',
	    font='Arial',
	    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=-2.0);

		main_begin_2.draw()
		foot_begin_2.draw()
		myWin.flip()

		if event.getKeys(keyList=["escape"]):
					core.quit()

		if green:
			continueInstruction = False
			green = False

	# Second 8 trials
	trial = Trial(conditions, 80, 144)
	trial.TrialBlock(2)

	continueInstruction = True
	while continueInstruction:
		main_thanks = visual.TextStim(win=myWin, name='main_thanks',
	    text=u'Thank you for your participation. The supervisor will now continue to guide you through the session.',
	    font='Arial',
	    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
	    color='white', colorSpace='rgb', opacity=1,
	    depth=0.0);

		main_thanks.draw()
		myWin.flip()

		if event.getKeys(keyList=["escape"]):
					core.quit()

		if green:
			continueInstruction = False
			green = False
