#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
import time, random, os, sys, glob, threading
from psychopy import locale_setup, gui, visual, core, data, event, logging, prefs
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
from pyo import *
from powermate import PowerMateBase, LedEvent, MAX_BRIGHTNESS
from parallel_helper import Trigger

################# own classes / functions setup ################
prefs.general['audioLib'] = ['pyo']
# function which returns random frequency between 220 and 880 Hz
def rnd_tone():
	return random.randrange(220, 880, 1)

def rnd_note(pre):
	note = random.choice(notes)
	if trial_num >= 32:
		if notes_count[note] < 3:
			notes_count[note] += 1
			return note
	if note == pre:
		return rnd_note(pre)
	if notes_count[note] < 3:
		notes_count[note] += 1
		return note
	return rnd_note(pre)


# class which overrides classmethods of PowerMateBase of powermate.py
class PATPowerMate(PowerMateBase):
	def __init__(self, path):
		super(PATPowerMate, self).__init__(path)
		self._pulsing = False
		self._brightness = MAX_BRIGHTNESS

	# use rotation of powermate to increase/decrease frequency by 10 cents
	def rotate(self, rotation):
		global FirstTouch
		global useTrigger
		if FirstTouch and useTrigger:
			Trigger().send(200)
			FirstTouch = False

		if rotation < 0:
			freq.value = freq.value / 1.0057778950655485929679257
		if rotation > 0:
			freq.value = freq.value * 1.0057778950655485929679257

	# use push_rotation of powermate to inc/dec freq by 1 cent
	def push_rotate(self, rotation):
		global FirstTouch
		global useTrigger
		if FirstTouch and useTrigger:
			Trigger().send(200)
			FirstTouch = False

		if rotation < 0:
			freq.value = freq.value / 1.00057778950655485929679257
		if rotation > 0:
			freq.value = freq.value * 1.00057778950655485929679257

	def short_press(self):
		global nextStep
		nextStep = True


def StartResponsePad():
	import pyxid
	global green, blue

	dev = pyxid.get_xid_devices()[0]
	dev.reset_base_timer()

	while True:
		dev.poll_for_response()
		if dev.response_queue_size() > 0:
			response = dev.get_next_response()
			if response['pressed'] == True:
				if response['key'] == 3:
					blue = True
				if response['key'] == 7:
					green = True

def StartPowerMate():
	pm = PATPowerMate(glob.glob('/dev/input/by-id/*PowerMate*')[0])
	pm_thread = threading.Thread(target=pm.run)
	pm_thread.daemon = True
	pm_thread.start()


################ psychopy setup ################

# store info about the experiment session
expName = u'Absolute Pitch Experiment'  
expInfo = {'participant name':'', 'session':'001', 'use trigger':True}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
	core.quit()  # user pressed cancel
expInfo['date'] = "2018_Mar_03" #data.getDateStr() #2018_month_Date_time e.g. 2018_Mar_03_1022
expInfo['expName'] = expName


global useTrigger
useTrigger = False

if expInfo['use trigger']:
	useTrigger = True


# set filename
filename = u"data/" + expInfo['participant name'] + "_" + expInfo['date'] + "/" + expName
os.makedirs("data/" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "/")


# psychopy experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
	extraInfo=expInfo, runtimeInfo=None,
	originPath=None,
	savePickle=True, saveWideText=True,
	dataFileName=filename)

# save a log file for detail verbose info
# logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# set up a stimulus window and mouse
myWin = visual.Window(size=(1920, 1200), fullscr=True, allowGUI=False,winType='pyglet',
	monitor='testMonitor', screen=0, color=[-1.000,-1.000,-1.000], colorSpace='rgb',
	blendMode='avg',)

# set up fonts
sans = ['Gill Sans MT', 'Arial','Helvetica','Verdana'] 

# set up trial_num and first stimulus window
trial_num = 0

# set up notes
notes = ['A','A# / B','H','C','C# / Db','D','D# / Eb','E','F','F# / Gb','G','G# / Ab'] 
notes_count = {'A': 0,'A# / B': 0,'H' : 0,'C' : 0,'C# / Db' : 0,'D' : 0,'D# / Eb' : 0,'E' : 0,'F' : 0,'F# / Gb' : 0,'G' : 0,'G# / Ab': 0}
notes_trig = {'A': 101,'A# / B': 102,'H' : 103,'C' : 104,'C# / Db' : 105,'D' : 106,'D# / Eb' : 107,'E' : 108,'F' : 109,'F# / Gb' : 110,'G' : 111,'G# / Ab': 112}

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started

# boot sound engine and initialize sine-generator
pyoServer = Server().boot()
pyoServer.start()
pyoServer.recordOptions(dur=-1, filename="data/" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "/" + "audio.ogg", fileformat=7, sampletype=0)


freq = SigTo(value=440, time=0.001, init=440)
sine = SineLoop(freq=[freq, freq], feedback=0.08, mul=.3)

# boot powermate and response pad
global FirstTouch, green, blue 
FirstTouch = False
green = False
blue = False
try:
	StartPowerMate()
except:
	print("ERROR: Powermate not detected")
	raise

rp = threading.Thread(target=StartResponsePad)
rp.daemon = True
rp.start()

################ instructions page 1 ################

head_geninstr = visual.TextStim(win=myWin, name='head_geninstr',
	text='Welcome!',
	font='Comic Sans',
	pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
	color='white', colorSpace='rgb', opacity=1,
	depth=0.0);
main_geninstr = visual.TextStim(win=myWin, name='main_geninstr',
	text=u'In this task, we want to find out whether you have perfect/absolute pitch. \n \nYou are going to hear an artificial sine-tone, which can be adjusted using the pitch-wheel in front of you. By turning the wheel right or left you can modify the pitch in steps of 1/10 halftones. If you keep the wheel pressed down while turning, you can modify the pitch in steps of 1/100 halftones. Please confirm your choice with the big button on the right-hand side of the pad. In the next step you can try out the pitch-wheel.',
	font='Arial',
	pos=(0, 0.3), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);
foot_geninstr = visual.TextStim(win=myWin, name='foot_geninstr',
	text=u'Please continue by pressing the green button.',
	font='Arial',
	pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);


head_geninstr.setAutoDraw(True)
main_geninstr.setAutoDraw(True)
foot_geninstr.setAutoDraw(True)
	
myWin.flip()

# continue with instructions if green-button pressed

end = True
while end:
	if green:
		break
	for key in event.getKeys():
		if key in ['escape']: 
			myWin.close()
			core.quit()
		if key in ['return']:
			end = False

green = False

head_geninstr.setAutoDraw(False)
main_geninstr.setAutoDraw(False)
foot_geninstr.setAutoDraw(False)


################ instructions page 2 ################

main_testinstr = visual.TextStim(win=myWin, name='main_testinstr',
	text=u'Please try out the pitch-wheel.',
	font='Arial',
	pos=(0, 0.3), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);

head_testinstr = visual.TextStim(win=myWin, name='head_testinstr',
	text=u'You have confirmed your choice.',
	font='Comic Sans',
	pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
	color='white', colorSpace='rgb', opacity=1,
	depth=0.0);

foot_testinstr = visual.TextStim(win=myWin, name='foot_testinstr',
	text=u'Please continue by pressing the green button.',
	font='Arial',
	pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-2.0);


main_testinstr.setAutoDraw(True)
foot_testinstr.setAutoDraw(True)
myWin.flip()
sine.out()

end = True
while end:
	if blue:
		head_testinstr.draw()
		myWin.flip()
		core.wait(2)
	blue = False
	if green:
		sine.stop()
		end = False
	for key in event.getKeys():
		if key in ['return']: 
			sine.stop()
			end = False
		if key in ['escape']: 
			sine.stop()
			myWin.close()
			core.quit()
	myWin.flip()

main_testinstr.setAutoDraw(False)
foot_testinstr.setAutoDraw(False)

# trialclock setup
trialClock = core.Clock()
green = False

################ instructions page 3 ################
main_geninstr2 = visual.TextStim(win=myWin, name='main_geninstr2',
	text=u'You are now going to see different names of notes one at a time. It is your task to modify the pitch (with the wheel) so that it matches the tone shown to you at the display. We are using the german tone-names. Please confirm your choice by pressing the big button on the right-hand side of the pad. The test automatically continues after 15 seconds, even if you have not confirmed your choice, so do not think too long about it. Feel free to choose an octave, which you are comfortable with and the pitch which feels right for you!. You do not have to obey any convention (e.g. tuning after 440Hz). The most important aspect is to adjust the pitch as exactly as possible. Remember: You can modify the pitch in steps of 1/100 halftones by pressing the pitch-wheel while turning.',
	font='Arial',
	pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);
foot_geninstr2 = visual.TextStim(win=myWin, name='foot_geninstr2',
	text=u'The next step is a small excercise. Please proceed by pressing the green button.',
	font='Arial',
	pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-2.0);


main_geninstr2.setAutoDraw(True)
foot_geninstr2.setAutoDraw(True)
myWin.flip()

end = True
while end:
	if green:
		break
	for key in event.getKeys():
		if key in ['escape']: 
			myWin.close()
			core.quit()
		if key in ['return']:
			end = False

green = False

main_geninstr2.setAutoDraw(False)
foot_geninstr2.setAutoDraw(False)

################ instructions page 4 ################

cross = visual.TextStim(myWin, 
						units='norm',height = 0.4,
						pos=(0, 0), text="+", 
						font=sans, 
						alignHoriz = 'center',alignVert='center',
						color='white')

end = True

random_note = random.choice(notes)
ResponseInstruction = visual.TextStim(myWin, 
						units='norm',height = 0.4,
						pos=(0, 0), text=random_note, 
						font=sans, 
						alignHoriz = 'center',alignVert='center',
						color='white')

while end:
	

	# set random starting frequency/note and start sine-generator 
	freq.value = rnd_tone()
	sine.out()

	ResponseInstruction.text = random.choice(notes)
	ResponseInstruction.draw()  
	myWin.flip()

	# set conditions
	subject_response_finished = 0
	trialClock.reset()

	# receive mouse-wheel movement and tune frequency
	while subject_response_finished == 0:
		t = trialClock.getTime()

		# end trial if duration > 15s
		if t >= 15:
			if useTrigger:
				Trigger().send(202)
			sine.stop()
			cross.draw()
			myWin.flip()
			core.wait(3)
			subject_response_finished = 1
			trial_num += 1
			if trial_num >= 3:
				sine.stop()
				end = False


		# trigger events for escape key
		for key in event.getKeys():
			if key in ['escape']: 
				sine.stop()
				myWin.close()
				core.quit()

		# continue with next trial if powermate-button pressed
		if blue:
			sine.stop()
			cross.draw()
			myWin.flip()
			core.wait(3)
			subject_response_finished = 1
			blue = False
			trial_num += 1
			if trial_num >= 3:
				sine.stop()
				end = False

	
################ instructions page 5 ################


main_geninstr3 = visual.TextStim(win=myWin, name='main_geninstr2',
	text=u'Excercise finished! Do you have any questions? Please ask the supervisor. Please concentrate on tuning the pitch as exactly as possible. You have 15 seconds for every tone. Confirm by pressing the big button as soon as you are confident in your choice. Feel free to use any octave/tuning. Attention: Please do not sing, buzz or try to gain an advantage in any other way!',
	font='Arial',
	pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);
foot_geninstr3 = visual.TextStim(win=myWin, name='foot_geninstr2',
	text=u'Please proceed to the experiment by pressing the green button!',
	font='Arial',
	pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-2.0);


main_geninstr3.setAutoDraw(True)
foot_geninstr3.setAutoDraw(True)
myWin.flip()

end = True
while end:
	if green:
		break
	for key in event.getKeys():
		if key in ['escape']: 
			myWin.close()
			core.quit()
		if key in ['return']:
			end = False

green = False

main_geninstr3.setAutoDraw(False)
foot_geninstr3.setAutoDraw(False)

################ start of trials ################

trial_num = 0
stage = 1

end = True
random_note = rnd_note("")
ResponseInstruction.text = random_note

pyoServer.recstart()

while end:
	# exit if trial limit reached
	if trial_num >= 35:
		sine.stop()
		end = False

	# select and draw note
	if trial_num > 0:
		pre_note = random_note
		random_note = rnd_note(pre_note)
		ResponseInstruction.text = random_note

	ResponseInstruction.draw()

	# set random starting frequency/note and start sine-generator 
	freq.value = rnd_tone()
	start_frequency = freq.value
	sine.out()
#	pyoServer.recordOptions(dur=-1, filename="data/" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "/" + str(stage) + "_" + str(trial_num) + ".ogg", fileformat=7, sampletype=0)
#	pyoServer.recstart()

	# send trigger by note 
	if useTrigger:
		Trigger().send(notes_trig[random_note])

	
	myWin.flip()

	# start time measurement
	trialClock.reset()

	# set conditions
	subject_response_finished = 0
	FirstTouch = True
	
	# receive mouse-wheel movement and tune frequency
	while subject_response_finished == 0:
		t = trialClock.getTime()

		# end trial if duration > 15s
		if t >= 15:
			if useTrigger:
				Trigger().send(202)
			sine.stop()
#			pyoServer.recstop()
			time_expired = True
			subject_response_finished = 1
			cross.draw()
			myWin.flip()
			core.wait(3)

		# trigger events for escape key
		for key in event.getKeys():
			if key in ['escape']: 
				sine.stop()
#				pyoServer.recstop()
				myWin.close()
				core.quit()

		# continue with next trial if powermate-button pressed
		if blue:
			# send trigger 
			if useTrigger:
				Trigger().send(201)
			sine.stop()
#			pyoServer.recstop()
			time_expired = False
			cross.draw()
			myWin.flip()
			core.wait(3)
			subject_response_finished = 1
			blue = False


	# write trial data to csv
	trial_num += 1
	thisExp.addData('trial number', trial_num)
	thisExp.addData('start frequency', start_frequency)
	thisExp.addData('time expired', time_expired)
	thisExp.addData('entered frequency', freq.value)
	thisExp.addData('time', t)
	thisExp.addData('target note', random_note)	
	thisExp.nextEntry()

################ end screen ################
notes_count = {'A': 0,'A# / B': 0,'H' : 0,'C' : 0,'C# / Db' : 0,'D' : 0,'D# / Eb' : 0,'E' : 0,'F' : 0,'F# / Gb' : 0,'G' : 0,'G# / Ab': 0}

end_instr = visual.TextStim(win=myWin, name='end_instr',
	text=u'Part finished!\n \nPlease continue by pressing the green button!',
	font='Arial',
	pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);

end_instr.draw()
myWin.flip()

while True:
	if green:
		break

green = False

################ next trials ################

trial_num = 0
stage = 2
blue = False

end = True

random_note = rnd_note("")
ResponseInstruction.text = random_note



while end:
	# exit if trial limit reached
	if trial_num >= 35:
		sine.stop()
		end = False

	# select and draw note
	if trial_num > 0:
		pre_note = random_note
		random_note = rnd_note(pre_note)
		ResponseInstruction.text = random_note

	ResponseInstruction.draw()

	# set random starting frequency/note and start sine-generator 
	freq.value = rnd_tone()
	start_frequency = freq.value
	sine.out()
#	pyoServer.recordOptions(dur=-1, filename="data/" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "/" + str(stage) + "_" + str(trial_num) + ".ogg", fileformat=7, sampletype=0)
#	pyoServer.recstart()

	# send trigger by note 
	if useTrigger:
		Trigger().send(notes_trig[random_note])

	ResponseInstruction = visual.TextStim(myWin, 
						units='norm',height = 0.4,
						pos=(0, 0), text=random_note, 
						font=sans, 
						alignHoriz = 'center',alignVert='center',
						color='white')
	ResponseInstruction.draw()  
	myWin.flip()

	# start time measurement
	trialClock.reset()

	# set conditions
	subject_response_finished = 0
	FirstTouch = True
	
	# receive mouse-wheel movement and tune frequency
	while subject_response_finished == 0:
		t = trialClock.getTime()

		# end trial if duration > 15s
		if t >= 15:
			if useTrigger:
				Trigger().send(202)
			sine.stop()
#			pyoServer.recstop()
			time_expired = True
			subject_response_finished = 1
			cross.draw()
			myWin.flip()
			core.wait(3)

		# trigger events for escape key
		for key in event.getKeys():
			if key in ['escape']: 
				sine.stop()
#				pyoServer.recstop()
				myWin.close()
				core.quit()

		# continue with next trial if powermate-button pressed
		if blue:
			# send trigger 
			if useTrigger:
				Trigger().send(201)
			sine.stop()
#			pyoServer.recstop()
			time_expired = False
			cross.draw()
			myWin.flip()
			core.wait(3)
			subject_response_finished = 1
			blue = False


	# write trial data to csv
	trial_num += 1
	thisExp.addData('trial number', trial_num)
	thisExp.addData('start frequency', start_frequency)
	thisExp.addData('time expired', time_expired)
	thisExp.addData('entered frequency', freq.value)
	thisExp.addData('time', t)
	thisExp.addData('target note', random_note)	
	thisExp.nextEntry()
	
################ end screen ################
notes_count = {'A': 0,'A# / B': 0,'H' : 0,'C' : 0,'C# / Db' : 0,'D' : 0,'D# / Eb' : 0,'E' : 0,'F' : 0,'F# / Gb' : 0,'G' : 0,'G# / Ab': 0}

end_instr = visual.TextStim(win=myWin, name='end_instr',
	text=u'Part finished!\n \nPlease continue by pressing the green button!',
	font='Arial',
	pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);

end_instr.draw()
myWin.flip()

while True:
	if green:
		break

green = False
################ next trials ################

trial_num = 0
stage = 3
blue = False

end = True

random_note = rnd_note("")
ResponseInstruction.text = random_note

while end:
	# exit if trial limit reached
	if trial_num >= 35:
		sine.stop()
		end = False

	# select and draw note
	if trial_num > 0:
		pre_note = random_note
		random_note = rnd_note(pre_note)
		ResponseInstruction.text = random_note

	ResponseInstruction.draw()

	# set random starting frequency/note and start sine-generator 
	freq.value = rnd_tone()
	start_frequency = freq.value
#	pyoServer.recordOptions(dur=-1, filename="data/" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "/" + str(stage) + "_" + str(trial_num) + ".ogg", fileformat=7, sampletype=0)
#	pyoServer.recstart()
	sine.out()

	# send trigger by note 
	if useTrigger:
		Trigger().send(notes_trig[random_note])

	ResponseInstruction = visual.TextStim(myWin, 
						units='norm',height = 0.4,
						pos=(0, 0), text=random_note, 
						font=sans, 
						alignHoriz = 'center',alignVert='center',
						color='white')
	ResponseInstruction.draw()  
	myWin.flip()

	# start time measurement
	trialClock.reset()

	# set conditions
	subject_response_finished = 0
	FirstTouch = True
	
	# receive mouse-wheel movement and tune frequency
	while subject_response_finished == 0:
		t = trialClock.getTime()

		# end trial if duration > 15s
		if t >= 15:
			if useTrigger:
				Trigger().send(202)
			sine.stop()
#			pyoServer.recstop()
			time_expired = True
			subject_response_finished = 1
			cross.draw()
			myWin.flip()
			core.wait(3)

		# trigger events for escape key
		for key in event.getKeys():
			if key in ['escape']: 
				sine.stop()
#				pyoServer.recstop()
				myWin.close()
				core.quit()

		# continue with next trial if powermate-button pressed
		if blue:
			# send trigger 
			if useTrigger:
				Trigger().send(201)
			sine.stop()
#			pyoServer.recstop()
			time_expired = False
			cross.draw()
			myWin.flip()
			core.wait(3)
			subject_response_finished = 1
			blue = False


	# write trial data to csv
	trial_num += 1
	thisExp.addData('trial number', trial_num)
	thisExp.addData('start frequency', start_frequency)
	thisExp.addData('time expired', time_expired)
	thisExp.addData('entered frequency', freq.value)
	thisExp.addData('time', t)
	thisExp.addData('target note', random_note)	
	thisExp.nextEntry()

################ end screen ################


end_instr = visual.TextStim(win=myWin, name='end_instr',
	text=u'Experiment finished.',
	font='Arial',
	pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);

end_instr.draw()
myWin.flip()
pyoServer.recstop()

while True:
	for key in event.getKeys():
		if key in ['return']: 
			myWin.close()
			core.quit()
		if key in ['escape']: 
			myWin.close()
			core.quit()