#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from psychopy import visual, event, core
from parallel_helper import Trigger
import threading


sans = ['Gill Sans MT', 'Arial','Helvetica','Verdana'] 
myWin = visual.Window(size=(1920,1200), fullscr=True, allowGUI=False,winType='pyglet',
	monitor='testMonitor', screen=0, color=[-1.000,-1.000,-1.000], colorSpace='rgb',
	blendMode='avg',)


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

global green
green = False

rp = threading.Thread(target=StartResponsePad)
rp.daemon = True
rp.start()


trialClock = core.Clock()
### EO

head_geninstr = visual.TextStim(win=myWin, name='head_geninstr',
	text='Herzlich Willkommen!',
	font='Comic Sans',
	pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
	color='white', colorSpace='rgb', opacity=1,
	depth=0.0);
main_geninstr = visual.TextStim(win=myWin, name='main_geninstr',
	text=u'Bitte versuchen Sie, in den folgenden 5 Minuten so entspannt und still wie möglich mit offenen Augen da zu sitzen und Ihren Gedanken freien Lauf zu lassen.\nBetrachten Sie dabei einfach entspannt das Fixationskreuz in der Mitte des Bildschirms.',
	font='Arial',
	pos=(0, 0.3), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);
foot_geninstr = visual.TextStim(win=myWin, name='foot_geninstr',
	text=u'Bitte drücken Sie die grüne Taste erst, wenn Sie der/die Versuchsleiter/in dazu auffordert!',
	font='Arial',
	pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);


head_geninstr.draw()
main_geninstr.draw()
foot_geninstr.draw()
	
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

trialClock.reset()


cross = visual.TextStim(myWin, 
	units='norm',height = 0.4,
	pos=(0, 0), text="+", 
	font=sans, 
	alignHoriz = 'center',alignVert='center',
	color='white')

cross.draw()
myWin.flip()

trigger1 = True
trigger2 = True
end = True

while end:
	t = trialClock.getTime()
	if t >= 15 and trigger1:
		Trigger().send(33)
		trigger1 = False
		trialClock.reset()


	if t >= 300 and trigger2:
		Trigger().send(66)
		trigger2 = False
		end = False

	for key in event.getKeys():
		if key in ['escape']: 
			myWin.close()
			core.quit()
		if key in ['return']: 
			myWin.close()
			core.quit()


main_geninstr = visual.TextStim(win=myWin, name='main_geninstr',
	text=u'Bitte versuchen Sie, in den folgenden 5 Minuten so entspannt und still wie möglich mit geschlossenen Augen da zu sitzen und Ihren Gedanken freien Lauf zu lassen.',
	font='Arial',
	pos=(0, 0.3), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);
foot_geninstr = visual.TextStim(win=myWin, name='foot_geninstr',
	text=u'Bitte drücken Sie die grüne Taste erst, wenn Sie der/die Versuchsleiter/in dazu auffordert und schließen Sie dann bereits die Augen!',
	font='Arial',
	pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);


main_geninstr.draw()
foot_geninstr.draw()
	
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

trialClock.reset()

cross.draw()
myWin.flip()

trigger1 = True
trigger2 = True
end = True

while end:
	t = trialClock.getTime()
	if t >= 15 and trigger1:
		Trigger().send(22)
		trigger1 = False
		trialClock.reset()


	if t >= 300 and trigger2:
		Trigger().send(55)
		trigger2 = False
		end = False

	for key in event.getKeys():
		if key in ['escape']: 
			myWin.close()
			core.quit()
		if key in ['return']: 
			myWin.close()
			core.quit()


main_geninstr = visual.TextStim(win=myWin, name='main_geninstr',
	text=u'Vielen Dank. Experiment beendet.',
	font='Arial',
	pos=(0, 0.3), height=0.05, wrapWidth=1.5, ori=0,
	color='white', colorSpace='rgb', opacity=1,
	depth=-1.0);

main_geninstr.draw()

myWin.flip()

while True:
	for key in event.getKeys():
		if key in ['escape']: 
			myWin.close()
			core.quit()
		if key in ['return']: 
			myWin.close()
			core.quit()