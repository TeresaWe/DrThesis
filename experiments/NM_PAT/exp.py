#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from psychopy import core, event, iohub, visual, gui, data
import time, random, os, sys, glob, threading
from pyo import *
from powermate import PowerMateBase, LedEvent, MAX_BRIGHTNESS
from parallel_helper import Trigger
import pyxid
from pit import PIT 
from lern import LernPhase


#myWin = visual.Window([1920, 1200], units='pix', fullscr=True, color=[-1, -1, -1], winType='pyglet', blendMode='avg', colorSpace='rgb')




expName = u'Non-musician PIT'  
expInfo = {'participant name':'', 'session':'001', 'use trigger':True, u'condition type': ['A', 'B']}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
	core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  
expInfo['expName'] = expName

global useTrigger
useTrigger = False

if expInfo['use trigger']:
	useTrigger = True

# set filename
filename = u"data_PIT/NM_" + expInfo['participant name'] + "_" + expInfo['date'] + "_PIT/" + expName
os.makedirs("data_PIT/NM_" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "_PIT/")

# psychopy experiment handlera
thisExp = data.ExperimentHandler(name=expName, version='',
	extraInfo=expInfo, runtimeInfo=None,
	originPath=None,
	savePickle=True, saveWideText=True,
	dataFileName=filename)

myWin = visual.Window(size=(1920, 1200), units='pix', fullscr=True, color=[-1, -1, -1], winType='pyglet', blendMode='avg', colorSpace='rgb')

buttons = ["C", "Dis", "Fis", "A", "Cis", "E", "G", "B", "D", "F", "Gis", "H"]

pyoServer = Server().boot()
pyoServer.start()

expName = u'Non-musician PAT'
expInfo['expName'] = expName
filename = u"data_PAT/NM_" + expInfo['participant name'] + "_" + expInfo['date'] + "_PAT/" + expName
os.makedirs("data_PAT/NM_" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "_PAT/") 
thisExpPat = data.ExperimentHandler(name=expName, version='',
	extraInfo=expInfo, runtimeInfo=None,
	originPath=None,
	savePickle=True, saveWideText=True,
	dataFileName=filename)

#############################################
def rnd_tone():
	return random.randrange(261, 440, 1)

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

# set up fonts
sans = ['Gill Sans MT', 'Arial','Helvetica','Verdana'] 

# set up trial_num and first stimulus window
trial_num = 0

# set up notes
notes_trig = {'A': 101,'B': 102,'H' : 103,'C' : 104,'Cis' : 105,'D' : 106,'Dis' : 107,'E' : 108,'F' : 109,'Fis' : 110,'G' : 111,'Gis': 112}

# boot sound engine and initialize sine-generator

freq = SigTo(value=440, time=0.001, init=440)
sine = SineLoop(freq=[freq, freq], feedback=0.08, mul=.3)

# boot powermate and response pad
global FirstTouch, green, blue 
FirstTouch = False
green = False
blue = False
StartPowerMate()
rp = threading.Thread(target=StartResponsePad)
rp.daemon = True
rp.start()

###############################################
def text(head, main, foot):
	global green

	head_geninstr = visual.TextStim(win=myWin, name='head_geninstr',
	text=head,
	font='Arial',
	pos=(0, 500), height=40, 
	color='white');
	main_geninstr = visual.TextStim(win=myWin, name='main_geninstr',
	text=main,
	font='Arial',
	pos=(0, 200), height=35,
	color='white', wrapWidth=1200);
	foot_geninstr = visual.TextStim(win=myWin, name='foot_geninstr',
	text=foot,
	font='Arial',
	pos=(0, -500), height=35,
	color='white');

	head_geninstr.setAutoDraw(True)
	main_geninstr.setAutoDraw(True)
	foot_geninstr.setAutoDraw(True)
	
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

	head_geninstr.setAutoDraw(False)
	main_geninstr.setAutoDraw(False)
	foot_geninstr.setAutoDraw(False)

def PATTrial(notes, rep):
	global FirstTouch, green, blue 
	cross = visual.TextStim(myWin, 
						units='norm',height = 0.4,
						pos=(0, 0), text="+", 
						font=sans, 
						alignHoriz = 'center',alignVert='center',
						color='white')

	end = True
	trialClock = core.Clock()

	len_notes = len(notes)
	trial_num = 0
	counter = rep * len_notes
	cross.draw()
	myWin.flip()
	core.wait(3)
	while end:
		random_note = random.choice(notes)
		notes.remove(random_note)

		if useTrigger:
			Trigger().send(notes_trig[random_note])

		# set random starting frequency/note and start sine-generator 
		freq.value = rnd_tone()
		start_freq = freq.value
 	
		sine.out()

		ResponseInstruction = visual.TextStim(myWin, 
							units='norm',height = 0.4,
							pos=(0, 0), text=random_note, 
							font=sans, 
							alignHoriz = 'center',alignVert='center',
							color='white')
		ResponseInstruction.draw()  
		myWin.flip()

		# set conditions
		subject_response_finished = 0
		trialClock.reset()
		FirstTouch = True
		pause = 0
		
		time_expired='False'
		# receive mouse-wheel movement and tune frequency
		while subject_response_finished == 0:
			t = trialClock.getTime()

			# end trial if duration > 15s
			if t + pause >= 15:
				if useTrigger:
					Trigger().send(202)
				sine.stop()
				cross.draw()
				myWin.flip()
				core.wait(3)
				subject_response_finished = 1
				time_expired = 'True'
				trial_num += 1
				if trial_num >= len_notes:
					sine.stop()
					end = False


			# trigger events for escape key
			for key in event.getKeys():
				if key in ['escape']: 
					sine.stop()
					myWin.close()
					core.quit()
				if key in ['p']:
					sine.stop()
					pause = pause + t
					while True:
						if 'p' in event.getKeys():
							break;
					sine.out()
					trialClock.reset()

			# continue with next trial if powermate-button pressed
			if blue:
				if useTrigger:
					Trigger().send(201)				
				sine.stop()
				cross.draw()
				myWin.flip()
				core.wait(3)
				subject_response_finished = 1
				blue = False
				trial_num += 1
				if trial_num >= len_notes:
					sine.stop()
					end = False
		a = counter + trial_num
		thisExpPat.addData('trial number', a)
		thisExpPat.addData('start frequency', start_freq)
		thisExpPat.addData('time expired', time_expired)
		thisExpPat.addData('entered frequency', freq.value)
		thisExpPat.addData('time', t)
		thisExpPat.addData('target note', random_note)	
		thisExpPat.nextEntry()


# Anzahl pro Block
N = 12 # Anzahl Lernphase "Hören"
N2 = 3 # Anzahl Lernphase "Pit/Pat"


# first instruction
head = "Welcome!"
main = "In this Experiment, our goal is to find out how good you are in remembering unique tones. You are going to hear different tones und learn how they are named. Every tone gets a name e.g. A, C, Fis or Des. \n \nYou are going to learn 12 tones in total which are seperated in 2 blocks (each with 6 tones). Afer each block, a small excercise follows. At the end of the experiment we would like to check, how good you are in remembering the names of the notes. Furthermore we want to find out, if you are able to adjust a tone to the right pitch by using a pitch-wheel."
foot = u"Continue by pressing the green button!"
text(head, main, foot)

main = "Let's start with the first six tones and their names. Try to memorize the sound and name of the tone as good as possible. Every tone is shown to you multiple times. Just listen carefully to the sounds."
text("", main, foot)


# 1. block
lern = LernPhase(4, myWin)
main_h = "Now you are going to hear the tones you have just learned. Please use the pc-mouse to click on the box with the right name of the tone. You have 5 seconds to make your choice. After you have clicked we will start with the next tone. So you can not change your tone after you clicked the first time!"
main_r = "Now it is getting more difficult. Can you use the pitch-wheel to adjust the tone correctly? You are going to see the name of a known tone and hear a random start-tone. Try to use the wheel to adjust the pitch, so that the tone sounds like the displayed one. If you keep pressing the wheel while turning, you are able to adjust the pitch more precisely. You can confirm your tone by pressing the big button. You have 15 seconds to make your choice. Attention: Please do not sing, buzz or try to gain an advantage in any other way!"
if expInfo['condition type'] == "A":
	i = 0
	while i < N:
		lern.TrialHandler(["C", "D", "E", "Fis", "Gis", "B"], 6)
		i += 1

	head = "Learning-phase finished!"
	text(head, main_h, foot)

	i = 0
	pit = PIT(0, 6, ["C", "D", "E", "Fis", "Gis", "B"], 5, myWin, thisExp)
	while i < N2:
		pit.TrialHandler(["C", "D", "E", "Fis", "Gis", "B"], 6)
		i += 1
	pit.io.quit()

	head = "Part finished!"
	text(head, main_r, foot)
	i = 0
	pyoServer.recordOptions(dur=-1, filename="data_PAT/NM_" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "_PAT/NM_TrainPat1_condition" + expInfo['condition type'] + ".ogg", fileformat=7, 						sampletype=0)
	pyoServer.recstart()	
	while i < N2:
		PATTrial(["C", "D", "E", "Fis", "Gis", "B"], i)
		i += 1
	pyoServer.recstop()
else:
	i = 0
	while i < N:
		lern.TrialHandler(["Cis", "Dis", "F", "G", "A", "H"], 6)
		i += 1
	head = "Learning-phase finished!"
	text(head, main_h, foot)
	i = 0
	pit = PIT(0, 6, ["Cis", "Dis", "F", "G", "A", "H"], 5, myWin, thisExp)
	while i < N2:
		pit.TrialHandler(["Cis", "Dis", "F", "G", "A", "H"], 6)
		i += 1
	pit.io.quit()

	head = "Part finished!"
	text(head, main_r, foot)
	i = 0
	pyoServer.recordOptions(dur=-1, filename="data_PAT/NM_" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "_PAT/NM_TrainPat1_condition" + expInfo['condition type'] + ".ogg", fileformat=7, 						sampletype=0)
	pyoServer.recstart()	
	while i < N2:
		PATTrial(["Cis", "Dis", "F", "G", "A", "H"], i)
		i += 1
	pyoServer.recstop()


head = "Part finished!"
main = "You have finished the first part. The next step is to repeat the procedure with six new tones."
text(head, main, foot)


# 2. block
main = "Let's start with the next six tones and their names. Try to memorize the sound and name of the tone as good as possible. Every tone is shown to you multiple times. Just listen carefully to the sounds."
text("", main, foot)

if expInfo['condition type'] == "A":
	i = 0
	while i < N:
		lern.TrialHandler(["Cis", "Dis", "F", "G", "A", "H"], 6)
		i += 1
	head = "Learning-phase finished!"
	text(head, main_h, foot)
	i = 0
	pit = PIT(0, 6, ["Cis", "Dis", "F", "G", "A", "H"], 5, myWin, thisExp)
	while i < N2:
		pit.TrialHandler(["Cis", "Dis", "F", "G", "A", "H"], 6)
		i += 1
	pit.io.quit()

	head = "Part finished!"
	text(head, main_r, foot)
	i = 0
	pyoServer.recordOptions(dur=-1, filename="data_PAT/NM_" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "_PAT/NM_TrainPat2_condition" + expInfo['condition type'] + ".ogg", fileformat=7, 						sampletype=0)
	pyoServer.recstart()		
	while i < N2:
		PATTrial(["Cis", "Dis", "F", "G", "A", "H"], i)
		i += 1
	pyoServer.recstop()
else:
	i = 0
	while i < N:
		lern.TrialHandler(["C", "D", "E", "Fis", "Gis", "B"], 6)
		i += 1

	head = "Learning-phase finished!"
	text(head, main_h, foot)

	i = 0
	pit = PIT(0, 6, ["C", "D", "E", "Fis", "Gis", "B"], 5, myWin, thisExp)
	while i < N2:
		pit.TrialHandler(["C", "D", "E", "Fis", "Gis", "B"], 6)
		i += 1
	pit.io.quit()

	head = "Part finished!"
	text(head, main_r, foot)
	i = 0
	pyoServer.recordOptions(dur=-1, filename="data_PAT/NM_" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "_PAT/NM_TrainPat2_condition" + expInfo['condition type'] + ".ogg", fileformat=7, 						sampletype=0)
	pyoServer.recstart()		
	while i < N2:
		PATTrial(["C", "D", "E", "Fis", "Gis", "B"], i)
		i += 1
	pyoServer.recstop()




head = "Part finished!"
main = "You have finished the whole learning phase. For the second part we install the EEG. You can take a pause and relax a little bit."

head_geninstr = visual.TextStim(win=myWin, name='head_geninstr',
	text=head,
	font='Arial',
	pos=(0, 500), height=40, 
	color='white');
main_geninstr = visual.TextStim(win=myWin, name='main_geninstr',
	text=main,
	font='Arial',
	pos=(0, 200), height=25,
	color='white');

head_geninstr.setAutoDraw(True)
main_geninstr.setAutoDraw(True)
	
myWin.flip()

end = True
while end:
	for key in event.getKeys():
		if key in ['escape']: 
			myWin.close()
			core.quit()
		if key in ['space']:
			end = False

head_geninstr.setAutoDraw(False)
main_geninstr.setAutoDraw(False)




main = "Can you remember the tones from the beginning? In the following excercises we want to find out, how many of the 12 tones from the learning-phase you can remember or adjust. This excercise is more difficult and therefore requires more concentration and time. "
text("", main, foot)

##################### PIT ###################################
main = "Now you are going to hear the tones you have just learned. Please use the pc-mouse to click on the box with the right name of the tone. You have 10 seconds to make your choice. After you have clicked we will start with the next tone. So you can not change your tone after you clicked the first time!"
text("", main, foot)

i = 0
pit = PIT(0, 4, buttons, 10, myWin, thisExp)
while i < 3:
	pit.TrialHandler(["C", "Dis", "Fis", "A", "Cis", "E", "G", "B", "D", "F", "Gis", "H"], 12)
	i += 1

head = "Part finished!"
main = "You have successfully finished the first experiment. Now, there will be following instructions for the next experiment."
text(head, main, foot)


########################### PAT ###############################
main = "You are now going to see different names of notes one at a time. It is your task to modify the pitch (with the wheel) so that it matches the tone shown to you at the display. We are using the german tone-names. Please confirm your choice by pressing the big button on the right-hand side of the pad. The test automatically continues after 15 seconds, even if you have not confirmed your choice, so do not think too long about it. The most important aspect is to adjust the pitch as exactly as possible. Remember: You can modify the pitch in steps of 1/100 halftones by pressing the pitch-wheel while turning."
text("", main, foot)
foot_exp = "Please press the green button to proceed to the experiment."
main = "Do you have any questions? Please ask the supervisor. Please concentrate on tuning the pitch as exactly as possible. You have 15 seconds for every tone. Confirm by pressing the big button as soon as you are confident in your choice. Attention: Please do not sing, buzz or try to gain an advantage in any other way!"
text("", main, foot_exp)

j = 0
pyoServer.recordOptions(dur=-1, filename="data_PAT/NM_" + unicode(expInfo['participant name']) + "_" + expInfo['date'] + "_PAT/NM_BigPat.ogg", fileformat=7, 						sampletype=0)
pyoServer.recstart()
while j < 3:
	i = 0
	while i < 3:
		patName = "BigPat_%d_%d" %(j,i)
		PATTrial(["C", "Dis", "Fis", "A", "Cis", "E", "G", "B", "D", "F", "Gis", "H"], i)
		i += 1
	j += 1
	head = "Part finished!"
	if(j < 3):		
		main = "You have successfully finished the %d. part. We will continue with the %d. part." %(j,j+1)
	else:
		main = "You have successfully finished the %d. part." %j
	text(head, main, foot)
pyoServer.recstop()

corpus = "Experiment finished. Please report to the supervisor."
text("", corpus, "")


