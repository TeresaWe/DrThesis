#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Di 16 Mai 2017 17:48:08 CEST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import pyxid

reload(sys)  
sys.setdefaultencoding('utf8')


#Start ButtonBox
ButtonBox = pyxid.get_xid_devices()[0]
ButtonBox.reset_base_timer()
ButtonBox.reset_rt_timer()

#Global variables for Feedback at the end of the run
totalCorrect_global = 0
totalCorrect_local = 0

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Navon'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1200), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=False)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "geninstr"
geninstrClock = core.Clock()
head_geninstr = visual.TextStim(win=win, name='head_geninstr',
    #text='Herzlich Willkommen!',
    text='Welcome!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_geninstr = visual.TextStim(win=win, name='main_geninstr',
    #text=u'Bei dieser Aufgabe sehen Sie Buchstaben, die selbst aus Buchstaben aufgebaut sind.\n\n\n\n\n\n\n\nDie Buchstaben (z.B. H) k\xf6nnen aus dem selben Buchstaben (z.B. H) oder einem anderen (z.B. ein gro\xdfes S aus kleinen H) bestehen.\n\nIn einer Bedingung werden Sie aufgefordert, die \xfcbergeordnete, globale Form des Buchstabens zu identifizieren; \nin einem anderen Durchgang werden Sie gefragt, die individuellen Buchstabenelemente auf lokaler Ebene zu identifizieren. ',
    text=u'In this experiment you will see big letters which are made out of small letters. \n\n\n\n\n\n\n\nThe letters (e.g. H) can be made out of the same letter (e.g. H) or can be made out of a different letter (e.g. a big S made out of small H). \n\nIn one condition you have to identify the big, global shape of the letters; \n in other trials you will be asked to identify the small letters .',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_geninstr = visual.TextStim(win=win, name='foot_geninstr',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
Instr_HH = visual.ImageStim(
    win=win, name='Instr_HH',
    image='Grafiken/HH.png', mask=None,
    ori=0, pos=(-0.4, 0.3), size=(0.194, 0.300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Instr_SH = visual.ImageStim(
    win=win, name='Instr_SH',
    image='Grafiken/SH.png', mask=None,
    ori=0, pos=(0.4, 0.3), size=(0.194,0.300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "geninstr_2"
geninstr_2Clock = core.Clock()
head_geninstr_2 = visual.TextStim(win=win, name='head_geninstr_2',
    #text='Ablauf',
    text='Procedure',
    font='Arial',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_geninstr2 = visual.TextStim(win=win, name='main_geninstr2',
    #text=u'1. Blicken Sie auf das Fixationskreuz in der Mitte des Bildschirms.\n2. Ein Warnton bereitet Sie vor.\n3. Der Buchstabe erscheint zuf\xe4llig in einem der vier Quadranten des Bildschirms f\xfcr eine kurze Zeit, und wird daraufhin bedeckt.\n4. Dr\xfccken Sie so schnell es geht die linke oder rechte Taste, abh\xe4ngig von der Aufgabenstellung. \n5. Nach einer kurzen Pause startet der n\xe4chste Trial automatisch.\n\nUm Ihre Reaktionszeiten zu optimieren, legen Sie bitte Ihre beiden Zeigefinger bereits vor den Trials auf die Tasten.  Nun folgt zun\xe4chst die Instruktion f\xfcr die erste der zwei Aufgaben.',
    text=u'1. Please look at the fixation cross in the centre of the screen. \n2. A signal tone will announce the next trial and help you prepare. \n3. A letter will appear in one of the quadrants of the screen for a short period of time and will be then covered. \n4. Press either the left or the right key depending on the instructions as fast as possible. \n5. After a short break the next trial will begin automatically. \n\nTo optimize your reaction time, please rest both of your index fingers on the console before the trial begins. The instructions for the first of the two tasks will follow now.',
    font='Arial',
    pos=(0,0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text = visual.TextStim(win=win, name='text',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "locinstr"
locinstrClock = core.Clock()
head_locinstr = visual.TextStim(win=win, name='head_locinstr',
    #text='Form der lokalen Buchstaben (Elemente)',
    text='Local shape (elements)',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_locinstr = visual.TextStim(win=win, name='main_locinstr',
    #text='Bitte reagieren Sie in der folgenden Aufgabe auf die lokalen Buchstaben, d.h. die kleinen Buchstaben, aus welchen die großen bestehen . Dieser kleine Buchstabe kann entweder H oder S sein. Bitte drücken Sie so schnell es geht die entsprechende Taste (Links="S" oder Rechts= "H").\n\nBeispiel:\n\n\n\n\n\n\n\n\n           Bsp: Rechte Taste drücken                                        Bsp: Rechte Taste drücken\n\nDie Stimuli werden nur für eine kurze Zeit päsentiert. Bitte versuchen Sie so schnell es geht zu antworten, jedoch möglichst wenig Fehler zu machen.\n\nEs folgt nun eine kurze Übung! ',
    text=u'Now, please react to the local shape of the letters (the small letters). The small letters can be a H or a S. Please press the correct key as fast as possible (Left = "S" or Right = "H"). \n\nExample: \n\n\n\n\n\n\n\n\n             e.g.: Press Right key                                       e.g.: Press Right key\n\n The stimuli will only appear for a short period of time. Please try to react as fast as possible while avoiding making mistakes. There will be a short practice session now!',
    font='Arial',
    pos=(0, 0), height=0.060, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_locinstr = visual.TextStim(win=win, name='foot_locinstr',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
H = visual.ImageStim(
    win=win, name='H',
    image='Grafiken/HH.png', mask=None,
    ori=0, pos=(-0.4, 0), size=(0.194, 0.300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
S = visual.ImageStim(
    win=win, name='S',
    image='Grafiken/SH.png', mask=None,
    ori=0, pos=(0.4,0), size=(0.194, 0.300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "Trials_L"
Trials_LClock = core.Clock()
Fixation_L = visual.TextStim(win=win, name='Fixation_L',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
local_sound = sound.Sound('A', secs=-1)
local_sound.setVolume(1)
ISI_L = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L')
local_stim = visual.ImageStim(
    win=win, name='local_stim',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
maske = visual.ImageStim(
    win=win, name='maske',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "feedbackL_train"
feedbackL_trainClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!


head_feedbackL_2 = visual.TextStim(win=win, name='head_feedbackL_2',
    #text=u'\xdcbung beendet!',
    text=u'Practice session completed!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
main_feedbackL_2 = visual.TextStim(win=win, name='main_feedbackL_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
foot_feedbackL_2 = visual.TextStim(win=win, name='foot_feedbackL_2',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "instr_realL"
instr_realLClock = core.Clock()
head_locreal = visual.TextStim(win=win, name='head_locreal',
    #text='Beginn des Experiments ',
    text='Start of the experiment',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_locreal = visual.TextStim(win=win, name='main_locreal',
    #text=u'Sie sind nun bereit f\xfcr das Experiment! Bitte fragen Sie jetzt den/die Versuchsleiter/in wenn etwas unklar ist.\n\nBitte versuchen Sie so schnell wie m\xf6glich zu reagieren und m\xf6glichst wenig Fehler zu machen!\n\nLegen Sie bitte nun bereits Ihre Zeigefinger auf die Tasten!\n\n',
    text=u'You are now well prepared to start the actual experiment! If something is unclear, ask your test director now. \n\nPlease try to answer as fast and as correctly as possible!\n\n Please put both of your index fingers on the console, now!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_locreal = visual.TextStim(win=win, name='foot_locreal',
    #text=u'Dr\xfccken Sie die grüne Taste um mit dem Experiment zu beginnen!',
    text=u'Press the green key to start the experiment!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Trials_L"
Trials_LClock = core.Clock()
Fixation_L = visual.TextStim(win=win, name='Fixation_L',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
local_sound = sound.Sound('A', secs=-1)
local_sound.setVolume(1)
ISI_L = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L')
local_stim = visual.ImageStim(
    win=win, name='local_stim',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
maske = visual.ImageStim(
    win=win, name='maske',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "pause_L"
pause_LClock = core.Clock()
head_feedbackL = visual.TextStim(win=win, name='head_feedbackL',
    #text='Kurze Pause!',
    text='Short break!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_feedbackL = visual.TextStim(win=win, name='main_feedbackL',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Trials_L"
Trials_LClock = core.Clock()
Fixation_L = visual.TextStim(win=win, name='Fixation_L',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
local_sound = sound.Sound('A', secs=-1)
local_sound.setVolume(1)
ISI_L = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L')
local_stim = visual.ImageStim(
    win=win, name='local_stim',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
maske = visual.ImageStim(
    win=win, name='maske',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "globinstr"
globinstrClock = core.Clock()
head_globinstr = visual.TextStim(win=win, name='head_globinstr',
    #text=u'\xdcbergeordnete (globale) Form des Buchstaben!',
    text=u'Global shape of the letter!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_globinstr = visual.TextStim(win=win, name='main_globinstr',
    #text=u'Bitte reagieren Sie in der folgenden Aufgabe auf die \xfcbergeordnete, d.h. globale Form der Buchstaben, also den Buchstaben, welcher aus den kleinen Elementen entsteht. Dieser gro\xdfe Buchstabe kann entweder H oder S sein. Bitte dr\xfccken Sie so schnell es geht die entsprechende Taste (Links="S" oder Rechts="H").\n\nBeispiel:\n\n\n\n\n\n\n\n\n		 	Bsp: Rechte Taste dr\xfccken                                 		Bsp: Linke Taste dr\xfccken\n\nDie Stimuli werden nur f\xfcr eine kurze Zeit pr\xe4sentiert. Bitte versuchen Sie so schnell es geht zu antworten, jedoch m\xf6glichst wenig Fehler zu machen.\n\nEs folgt nun eine kurze \xdcbung! ',
    text=u'Now, please react to the superordinate, global shape of the letters (the big letter). The letter can be a H or a S. Please press the correct key as fast as possible (Left = "S" or Right = "H"). \n\nExample: \n\n\n\n\n\n\n\n\n             e.g.: Press Right key                                       e.g.: Press Left key\n\n The stimuli will only appear for a short period of time. Please try to react as fast as possible while avoiding making mistakes. There will be a short practice session now!',
    font='Arial',
    pos=(0, 0), height=0.060, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_globinstr = visual.TextStim(win=win, name='foot_globinstr',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
Hglo = visual.ImageStim(
    win=win, name='Hglo',
    image='Grafiken/HH.png', mask=None,
    ori=0, pos=(-0.4,0), size=(0.194,0.300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Sglo = visual.ImageStim(
    win=win, name='Sglo',
    image='Grafiken/SH.png', mask=None,
    ori=0, pos=(0.4, 0), size=(0.194, 0.300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "Trials_G"
Trials_GClock = core.Clock()
Fixation_G = visual.TextStim(win=win, name='Fixation_G',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
global_sound = sound.Sound('A', secs=-1)
global_sound.setVolume(1)
ISI_L_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L_2')
global_stim = visual.ImageStim(
    win=win, name='global_stim',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
maske_g = visual.ImageStim(
    win=win, name='maske_g',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "feedbackG_train"
feedbackG_trainClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
head_feedbackG_2 = visual.TextStim(win=win, name='head_feedbackG_2',
    #text=u'\xdcbung beendet!',
    text=u'Practice session completed!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
main_feedbackG_2 = visual.TextStim(win=win, name='main_feedbackG_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
foot_feedbackG_2 = visual.TextStim(win=win, name='foot_feedbackG_2',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "instr_realG"
instr_realGClock = core.Clock()
head_globreal = visual.TextStim(win=win, name='head_globreal',
    #text='Beginn des Experiments',
    text='Start of the experiment',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_globreal = visual.TextStim(win=win, name='main_globreal',
    #text=u'Sie sind nun bereit f\xfcr das Experiment! Bitte fragen Sie jetzt den/die Versuchsleiter/in wenn etwas unklar ist. \n\nBitte versuchen Sie so schnell wie m\xf6glich zu reagieren und m\xf6glichst wenig Fehler zu machen!\n\nLegen Sie bitte nun bereits Ihre Zeigefinger auf die Tasten!',
    text=u'You are now well prepared to start the actual experiment! If something is unclear, ask your test director now. \n\nPlease try to answer as fast and as correctly as possible!\n\n Please put both of your index fingers on the console, now!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_globreal = visual.TextStim(win=win, name='foot_globreal',
    #text=u'Dr\xfccke Sie die grüne Taste um mit dem Experiment zu beginnen!',
    text=u'Press the green key to start the experiment!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Trials_G"
Trials_GClock = core.Clock()
Fixation_G = visual.TextStim(win=win, name='Fixation_G',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
global_sound = sound.Sound('A', secs=-1)
global_sound.setVolume(1)
ISI_L_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L_2')
global_stim = visual.ImageStim(
    win=win, name='global_stim',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
maske_g = visual.ImageStim(
    win=win, name='maske_g',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "pause_G"
pause_GClock = core.Clock()
head_feedbackG = visual.TextStim(win=win, name='head_feedbackG',
    #text='Kurze Pause!',
    text='Short break!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_feedbackG = visual.TextStim(win=win, name='main_feedbackG',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Trials_G"
Trials_GClock = core.Clock()
Fixation_G = visual.TextStim(win=win, name='Fixation_G',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
global_sound = sound.Sound('A', secs=-1)
global_sound.setVolume(1)
ISI_L_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L_2')
global_stim = visual.ImageStim(
    win=win, name='global_stim',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
maske_g = visual.ImageStim(
    win=win, name='maske_g',units='deg', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=4.67,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "end_question"
end_questionClock = core.Clock()
main_quest = visual.TextStim(win=win, name='main_quest',
    #text=u'Sie haben nun beide Varianten der Aufgabe erfolgreich beendet! \n\nWir w\xfcrden Sie nun bitten, uns noch ein paar letzte Fragen zu beantworten!Verwenden Sie dafür die PC-Maus unter dem Tisch.\n',
    text=u'You have now completed both conditions successfully! \n\nPlease answer the following questions. \n\nUse the mouse located under the table for this.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
foot_quest = visual.TextStim(win=win, name='foot_quest',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.90), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "question1"
question1Clock = core.Clock()
main_question1 = visual.TextStim(win=win, name='main_question1',
    #text=u'Wie schwierig fanden Sie das Experiment grunds\xe4tzlich? \n(0 = sehr einfach; 1= sehr schwierig)',
    text=u'How difficult was the experiment for you in general? (0 =  very easy; 1 = very difficult)',
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating1 = visual.RatingScale(win=win, name='rating1', marker='triangle', size=1, pos=[0.0, -0.3], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "question2"
question2Clock = core.Clock()
main_question2 = visual.TextStim(win=win, name='main_question2',
    #text=u'Wie schwierig fanden Sie es, sich auf die \xfcbergeordneten Buchstaben zu konzentrieren? \n(0 = sehr einfach; 1= sehr schwierig)',
    text=u'How difficult was it for you to concentrate on the global, superordinate letters? \n(0 = very easy; 1 = very difficult)',
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=1, pos=[0.0, -0.3], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "question3"
question3Clock = core.Clock()
main_question3 = visual.TextStim(win=win, name='main_question3',
    #text='Wie schwierig fanden Sie es, sich auf die elementaren Buchstaben auf lokaler Ebene zu konzentrieren? \n(0 = sehr einfach; 1= sehr schwierig)',
    text='How difficult was it for you to concentrate on the local, small letters? \n(0 = very easy; 1 = very difficult)',
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating3 = visual.RatingScale(win=win, name='rating3', marker='triangle', size=1, pos=[0.0, -0.3], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "question4"
question4Clock = core.Clock()
main_question4 = visual.TextStim(win=win, name='main_question4',
    #text=u'Manchmal waren die Buchstaben im Experiment inkongruent, d.h. die der Buchstabe auf globaler Ebene war nicht der selbe wie auf lokaler Ebene. \nFanden Sie es grunds\xe4tzlich schwieriger, sich auf den \xfcbergeordneten Buchstaben (=0), oder die elementaren Buchstaben auf lokaler Ebene (=1) zu konzentrieren? \n(Mitte= beide Bedingungen waren f\xfcr mich gleich schwierig)',
    text=u'Sometimes the letters in this experiment were incongruent which means that the local, small letters and the global, superordinate letter were not the same. \nWas it generally more difficult for you to concentrate on the big, global letter (= 0), or to concentrate on the small, local letters (=1)? \n(Middle = both conditions were equally difficult to me)', 
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating4 = visual.RatingScale(win=win, name='rating4', marker='triangle', size=1, pos=[0.0, -0.3], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "feedback_final"
feedback_finalClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
head_feedback_final = visual.TextStim(win=win, name='head_feedback_final',
    text='Feedback!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
main_feedback_final = visual.TextStim(win=win, name='main_feedback_final',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
foot_feedback_final = visual.TextStim(win=win, name='foot_feedback_final',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "feedback_final2"
feedback_final2Clock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
head_feedback_final_2 = visual.TextStim(win=win, name='head_feedback_final_2',
    text='Feedback!',
    font='Comic Sans',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
main_feedback_final_2 = visual.TextStim(win=win, name='main_feedback_final_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
foot_feedback_final_2 = visual.TextStim(win=win, name='foot_feedback_final_2',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Thank_you"
Thank_youClock = core.Clock()
main_thanks = visual.TextStim(win=win, name='main_thanks',
    #text=u'Herzlichen Dank f\xfcr Ihre Teilnahme!\n\nDer/Die Studienleiter/-in wird Sie jetzt durch die weiteren Bestandteile der Sitzung f\xfchren.',
    text=u'Thank you very much for your participation!\n\nThe test director will now give you further instructions.',

    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "geninstr"-------
t = 0
geninstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_read1 = event.BuilderKeyResponse()
# keep track of which components have finished
geninstrComponents = [head_geninstr, main_geninstr, foot_geninstr, key_read1, Instr_HH, Instr_SH]
for thisComponent in geninstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "geninstr"-------
while continueRoutine:
    # get current time
    t = geninstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *head_geninstr* updates
    if t >= 0.0 and head_geninstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        head_geninstr.tStart = t
        head_geninstr.frameNStart = frameN  # exact frame index
        head_geninstr.setAutoDraw(True)
    
    # *main_geninstr* updates
    if t >= 0.0 and main_geninstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_geninstr.tStart = t
        main_geninstr.frameNStart = frameN  # exact frame index
        main_geninstr.setAutoDraw(True)
    
    # *foot_geninstr* updates
    if t >= 0.0 and foot_geninstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        foot_geninstr.tStart = t
        foot_geninstr.frameNStart = frameN  # exact frame index
        foot_geninstr.setAutoDraw(True)
    
    # *key_read1* updates
    if t >= 0.0 and key_read1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_read1.tStart = t
        key_read1.frameNStart = frameN  # exact frame index
        key_read1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_read1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *Instr_HH* updates
    if t >= 0.0 and Instr_HH.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_HH.tStart = t
        Instr_HH.frameNStart = frameN  # exact frame index
        Instr_HH.setAutoDraw(True)
    
    # *Instr_SH* updates
    if t >= 0.0 and Instr_SH.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_SH.tStart = t
        Instr_SH.frameNStart = frameN  # exact frame index
        Instr_SH.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in geninstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "geninstr"-------
for thisComponent in geninstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "geninstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "geninstr_2"-------
t = 0
geninstr_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_readinstr_2 = event.BuilderKeyResponse()
# keep track of which components have finished
geninstr_2Components = [head_geninstr_2, main_geninstr2, text, key_readinstr_2]
for thisComponent in geninstr_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "geninstr_2"-------
while continueRoutine:
    # get current time
    t = geninstr_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *head_geninstr_2* updates
    if t >= 0.0 and head_geninstr_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        head_geninstr_2.tStart = t
        head_geninstr_2.frameNStart = frameN  # exact frame index
        head_geninstr_2.setAutoDraw(True)
    
    # *main_geninstr2* updates
    if t >= 0.0 and main_geninstr2.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_geninstr2.tStart = t
        main_geninstr2.frameNStart = frameN  # exact frame index
        main_geninstr2.setAutoDraw(True)
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_readinstr_2* updates
    if t >= 0.0 and key_readinstr_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_readinstr_2.tStart = t
        key_readinstr_2.frameNStart = frameN  # exact frame index
        key_readinstr_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_readinstr_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_readinstr_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_readinstr_2.keys = theseKeys[-1]  # just the last key pressed
            key_readinstr_2.rt = key_readinstr_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in geninstr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "geninstr_2"-------
for thisComponent in geninstr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_readinstr_2.keys in ['', [], None]:  # No response was made
    key_readinstr_2.keys=None
thisExp.addData('key_readinstr_2.keys',key_readinstr_2.keys)
if key_readinstr_2.keys != None:  # we had a response
    thisExp.addData('key_readinstr_2.rt', key_readinstr_2.rt)
thisExp.nextEntry()
# the Routine "geninstr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block_select = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Block_select')
thisExp.addLoop(Block_select)  # add the loop to the experiment
thisBlock_select = Block_select.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_select.rgb)
if thisBlock_select != None:
    for paramName in thisBlock_select.keys():
        exec(paramName + '= thisBlock_select.' + paramName)

for thisBlock_select in Block_select:
    currentLoop = Block_select
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_select.rgb)
    if thisBlock_select != None:
        for paramName in thisBlock_select.keys():
            exec(paramName + '= thisBlock_select.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    local_Block = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='local_Block')
    thisExp.addLoop(local_Block)  # add the loop to the experiment
    thisLocal_Block = local_Block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLocal_Block.rgb)
    if thisLocal_Block != None:
        for paramName in thisLocal_Block.keys():
            exec(paramName + '= thisLocal_Block.' + paramName)
    
    for thisLocal_Block in local_Block:
        currentLoop = local_Block
        # abbreviate parameter names if possible (e.g. rgb = thisLocal_Block.rgb)
        if thisLocal_Block != None:
            for paramName in thisLocal_Block.keys():
                exec(paramName + '= thisLocal_Block.' + paramName)
        
        # ------Prepare to start Routine "locinstr"-------
        t = 0
        locinstrClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_read2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        locinstrComponents = [head_locinstr, main_locinstr, foot_locinstr, key_read2, H, S]
        for thisComponent in locinstrComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "locinstr"-------
        while continueRoutine:
            # get current time
            t = locinstrClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_locinstr* updates
            if t >= 0.0 and head_locinstr.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_locinstr.tStart = t
                head_locinstr.frameNStart = frameN  # exact frame index
                head_locinstr.setAutoDraw(True)
            
            # *main_locinstr* updates
            if t >= 0.0 and main_locinstr.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_locinstr.tStart = t
                main_locinstr.frameNStart = frameN  # exact frame index
                main_locinstr.setAutoDraw(True)
            if main_locinstr.status == STARTED:  # only update if drawing
               #main_locinstr.setText(u'Bitte reagieren Sie in der folgenden Aufgabe auf die Form der lokalen Buchstaben, also denen, aus welchen die gr\xf6\xdferen Buchstaben gebaut sind. Diese Elementarbausteine k\xf6nnen entweder "H" oder "S" sein. Bitte dr\xfccken Sie so schnell es geht die entsprechende Taste auf der Tastatur (Links oder Rechts).\n\nBeispiel:\n\n\n\n\n\n\n			Bsp: Rechte Taste dr\xfccken               	              	Bsp: Rechte Taste dr\xfccken\n\nDie Stimuli werden nur f\xfcr eine kurze Zeit pr\xe4sentiert. Bitte versuchen Sie so schnell es geht zu antworten, jedoch m\xf6glichst wenig Fehler zu machen.\n\nEs folgt nun eine kurze \xdcbung! ', log=False)
                main_locinstr.setText(u'Now, please react to the local shape of the letters (the small letters). The small letters can be a H or a S. Please press the correct key as fast as possible (Left = "S" or Right = "H"). \n\nExample: \n\n\n\n\n\n\n\n\n             e.g.: Press Right key                                       e.g.: Press Right key\n\n The stimuli will only appear for a short period of time. Please try to react as fast as possible while avoiding making mistakes. There will be a short practice session now!',log=False)

            # *foot_locinstr* updates
            if t >= 0.0 and foot_locinstr.status == NOT_STARTED:
                # keep track of start time/frame for later
                foot_locinstr.tStart = t
                foot_locinstr.frameNStart = frameN  # exact frame index
                foot_locinstr.setAutoDraw(True)
            
            # *key_read2* updates
            if t >= 0.0 and key_read2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read2.tStart = t
                key_read2.frameNStart = frameN  # exact frame index
                key_read2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # *H* updates
            if t >= 0.0 and H.status == NOT_STARTED:
                # keep track of start time/frame for later
                H.tStart = t
                H.frameNStart = frameN  # exact frame index
                H.setAutoDraw(True)
            
            # *S* updates
            if t >= 0.0 and S.status == NOT_STARTED:
                # keep track of start time/frame for later
                S.tStart = t
                S.frameNStart = frameN  # exact frame index
                S.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in locinstrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "locinstr"-------
        for thisComponent in locinstrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "locinstr" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_local = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions_training_local_Navon.csv'),
            seed=None, name='practice_local')
        thisExp.addLoop(practice_local)  # add the loop to the experiment
        thisPractice_local = practice_local.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_local.rgb)
        if thisPractice_local != None:
            for paramName in thisPractice_local.keys():
                exec(paramName + '= thisPractice_local.' + paramName)
        
        for thisPractice_local in practice_local:
            currentLoop = practice_local
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_local.rgb)
            if thisPractice_local != None:
                for paramName in thisPractice_local.keys():
                    exec(paramName + '= thisPractice_local.' + paramName)
            
            # ------Prepare to start Routine "Trials_L"-------
            t = 0
            Trials_LClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(4.500000)
            # update component parameters for each repeat
            local_sound.setSound('Grafiken/Signal.wav', secs=0.075)
            KeyL = event.BuilderKeyResponse()


            # keep track of which components have finished
            Trials_LComponents = [Fixation_L, local_sound, KeyL, ISI_L, local_stim, maske]
            for thisComponent in Trials_LComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED


            # -------Start Routine "Trials_L"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Trials_LClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *Fixation_L* updates
                if t >= 2.0 and Fixation_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Fixation_L.tStart = t
                    Fixation_L.frameNStart = frameN  # exact frame index
                    Fixation_L.setAutoDraw(True)
                    #print "Fixation_L"
                frameRemains = 2.0 + 0.500- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Fixation_L.status == STARTED and t >= frameRemains:
                    Fixation_L.setAutoDraw(False)
                # start/stop local_sound
                if t >= 2 and local_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    local_sound.tStart = t
                    local_sound.frameNStart = frameN  # exact frame index
                    local_sound.play()  # start the sound (it finishes automatically)
                    #print "Start Sound"
                frameRemains = 2 + 0.075- win.monitorFramePeriod * 0.75  # most of one frame period left
                if local_sound.status == STARTED and t >= frameRemains:
                    local_sound.stop()  # stop the sound (if longer than duration)
                    #print "Stop Sound"
                
                # *KeyL* updates
                if t >= 2.5 and KeyL.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    KeyL.tStart = t
                    KeyL.frameNStart = frameN  # exact frame index
                    KeyL.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(KeyL.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                    #Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()


                frameRemains = 2.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if KeyL.status == STARTED and t >= frameRemains:
                    KeyL.status = STOPPED


                if KeyL.status == STARTED:
                    theseKeys = event.getKeys(keyList=['h', 's'])
                    
                    #print "Start Answer Processing"

                    ButtonBox.poll_for_response()

                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0:
                        if KeyL.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'h'
                                if response['key'] == 2:
                                    translated = 's'
                                KeyL.keys = translated # just the first key pressed
                                KeyL.rt = KeyL.clock.getTime()
                                #print "CONTROL: Ha apretado " + repr(KeyL.keys) + "."
                                # was this 'correct'?
                                if (KeyL.keys == str(corrAns)) or (KeyL.keys == corrAns):
                                    KeyL.corr = 1
                                    #print "CORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    KeyL.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                # a response ends the routine
                                continueRoutine = False
                
                # *local_stim* updates
                if t >= 2.5 and local_stim.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    local_stim.tStart = t
                    local_stim.frameNStart = frameN  # exact frame index
                    local_stim.setAutoDraw(True)
                    #print "Draw Stim"
                frameRemains = 2.5 + 0.100- win.monitorFramePeriod * 0.75  # most of one frame period left
                if local_stim.status == STARTED and t >= frameRemains:
                    local_stim.setAutoDraw(False)
                
                # *maske* updates
                if t >= 2.6 and maske.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    maske.tStart = t
                    maske.frameNStart = frameN  # exact frame index
                    maske.setAutoDraw(True)
                    #print "Draw Mask"
                frameRemains = 2.6 + 1.9- win.monitorFramePeriod * 0.75  # most of one frame period left
                if maske.status == STARTED and t >= frameRemains:
                    maske.setAutoDraw(False)
                # *ISI_L* period
                if t >= 0 and ISI_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_L.tStart = t
                    ISI_L.frameNStart = frameN  # exact frame index
                    ISI_L.start(2-t)
                    #print "Start ISI_L"
                elif ISI_L.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI_L*
                    local_stim.setPos(position)
                    local_stim.setImage(GL_fileName)
                    maske.setPos(position)
                    maske.setImage('Grafiken/Mask.png')
                    # component updates done
                    ISI_L.complete()  # finish the static period
                    #print "Finish ISI_L"
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trials_LComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trials_L"-------

            for thisComponent in Trials_LComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            local_sound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if KeyL.keys in ['', [], None]:  # No response was made
                KeyL.keys=None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   KeyL.corr = 1  # correct non-response
                else:
                   KeyL.corr = 0  # failed to respond (incorrectly)
            # store data for practice_local (TrialHandler)
            practice_local.addData('KeyL.keys',KeyL.keys)
            practice_local.addData('KeyL.corr', KeyL.corr)
            if KeyL.keys != None:  # we had a response
                practice_local.addData('KeyL.rt', KeyL.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'practice_local'
        
        # get names of stimulus parameters
        if practice_local.trialList in ([], [None], None):
            params = []
        else:
            params = practice_local.trialList[0].keys()
        # save data for this loop
        practice_local.saveAsText(filename + 'practice_local.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "feedbackL_train"-------
        t = 0
        feedbackL_trainClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        nCorr = practice_local.data['KeyL.corr'].sum() #.std(), .mean() also available
        meanRt = practice_local.data['KeyL.rt'].mean()
        #msg = "Sie haben %i Stimuli richtig beantwortet \n (Reaktionszeit=%.2f s)" %(nCorr,meanRt)
        msg = "You have answered %i trials correctly \n (reaction time = %.2f s)" %(nCorr,meanRt)
        
        main_feedbackL_2.setText(msg)
        key_read4_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        feedbackL_trainComponents = [head_feedbackL_2, main_feedbackL_2, foot_feedbackL_2, key_read4_2]
        for thisComponent in feedbackL_trainComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedbackL_train"-------
        while continueRoutine:
            # get current time
            t = feedbackL_trainClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *head_feedbackL_2* updates
            if t >= 0.0 and head_feedbackL_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_feedbackL_2.tStart = t
                head_feedbackL_2.frameNStart = frameN  # exact frame index
                head_feedbackL_2.setAutoDraw(True)
            
            # *main_feedbackL_2* updates
            if t >= 0.0 and main_feedbackL_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_feedbackL_2.tStart = t
                main_feedbackL_2.frameNStart = frameN  # exact frame index
                main_feedbackL_2.setAutoDraw(True)
            
            # *foot_feedbackL_2* updates
            if t >= 0.0 and foot_feedbackL_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                foot_feedbackL_2.tStart = t
                foot_feedbackL_2.frameNStart = frameN  # exact frame index
                foot_feedbackL_2.setAutoDraw(True)
            
            # *key_read4_2* updates
            if t >= 0.0 and key_read4_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read4_2.tStart = t
                key_read4_2.frameNStart = frameN  # exact frame index
                key_read4_2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read4_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackL_trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackL_train"-------
        for thisComponent in feedbackL_trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "feedbackL_train" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "instr_realL"-------
        t = 0
        instr_realLClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_read5 = event.BuilderKeyResponse()
        # keep track of which components have finished
        instr_realLComponents = [head_locreal, main_locreal, foot_locreal, key_read5]
        for thisComponent in instr_realLComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instr_realL"-------
        while continueRoutine:
            # get current time
            t = instr_realLClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_locreal* updates
            if t >= 0.0 and head_locreal.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_locreal.tStart = t
                head_locreal.frameNStart = frameN  # exact frame index
                head_locreal.setAutoDraw(True)
            
            # *main_locreal* updates
            if t >= 0.0 and main_locreal.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_locreal.tStart = t
                main_locreal.frameNStart = frameN  # exact frame index
                main_locreal.setAutoDraw(True)
            
            # *foot_locreal* updates
            if t >= 0.0 and foot_locreal.status == NOT_STARTED:
                # keep track of start time/frame for later
                foot_locreal.tStart = t
                foot_locreal.frameNStart = frameN  # exact frame index
                foot_locreal.setAutoDraw(True)
            
            # *key_read5* updates
            if t >= 0.0 and key_read5.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read5.tStart = t
                key_read5.frameNStart = frameN  # exact frame index
                key_read5.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read5.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instr_realLComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instr_realL"-------
        for thisComponent in instr_realLComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "instr_realL" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        exp_local_1 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'conditions_local_Navon_Part1.csv'),
            seed=None, name='exp_local_1')
        thisExp.addLoop(exp_local_1)  # add the loop to the experiment
        thisExp_local_1 = exp_local_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExp_local_1.rgb)
        if thisExp_local_1 != None:
            for paramName in thisExp_local_1.keys():
                exec(paramName + '= thisExp_local_1.' + paramName)
        
        for thisExp_local_1 in exp_local_1:
            currentLoop = exp_local_1
            # abbreviate parameter names if possible (e.g. rgb = thisExp_local_1.rgb)
            if thisExp_local_1 != None:
                for paramName in thisExp_local_1.keys():
                    exec(paramName + '= thisExp_local_1.' + paramName)
            
            # ------Prepare to start Routine "Trials_L"-------
            t = 0
            Trials_LClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(4.500000)
            # update component parameters for each repeat
            local_sound.setSound('Grafiken/Signal.wav', secs=0.075)
            KeyL = event.BuilderKeyResponse()
            # keep track of which components have finished
            Trials_LComponents = [Fixation_L, local_sound, KeyL, ISI_L, local_stim, maske]
            for thisComponent in Trials_LComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Trials_L"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Trials_LClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation_L* updates
                if t >= 2.0 and Fixation_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Fixation_L.tStart = t
                    Fixation_L.frameNStart = frameN  # exact frame index
                    Fixation_L.setAutoDraw(True)
                frameRemains = 2.0 + 0.500- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Fixation_L.status == STARTED and t >= frameRemains:
                    Fixation_L.setAutoDraw(False)
                # start/stop local_sound
                if t >= 2 and local_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    local_sound.tStart = t
                    local_sound.frameNStart = frameN  # exact frame index
                    local_sound.play()  # start the sound (it finishes automatically)
                frameRemains = 2 + 0.075- win.monitorFramePeriod * 0.75  # most of one frame period left
                if local_sound.status == STARTED and t >= frameRemains:
                    local_sound.stop()  # stop the sound (if longer than duration)

                # *KeyL* updates
                if t >= 2.5 and KeyL.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    KeyL.tStart = t
                    KeyL.frameNStart = frameN  # exact frame index
                    KeyL.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(KeyL.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                    #Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()
                
                    
                frameRemains = 2.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if KeyL.status == STARTED and t >= frameRemains:
                    KeyL.status = STOPPED
                   
                if KeyL.status == STARTED:
                    theseKeys = event.getKeys(keyList=['h', 's'])
                    

                    ButtonBox.poll_for_response()

                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0:
                        if KeyL.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'h'
                                if response['key'] == 2:
                                    translated = 's'
                                KeyL.keys = translated # just the first key pressed
                                KeyL.rt = KeyL.clock.getTime()
                                #print "CONTROL: Ha apretado " + repr(KeyL.keys) + "."
                                # was this 'correct'?
                                if (KeyL.keys == str(corrAns)) or (KeyL.keys == corrAns):
                                    KeyL.corr = 1
                                    totalCorrect_local += 1
                                    #print "CORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    KeyL.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                # a response ends the routine
                                continueRoutine = False
                
                # *local_stim* updates
                if t >= 2.5 and local_stim.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    local_stim.tStart = t
                    local_stim.frameNStart = frameN  # exact frame index
                    local_stim.setAutoDraw(True)
                frameRemains = 2.5 + 0.100- win.monitorFramePeriod * 0.75  # most of one frame period left
                if local_stim.status == STARTED and t >= frameRemains:
                    local_stim.setAutoDraw(False)
                
                # *maske* updates
                if t >= 2.6 and maske.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    maske.tStart = t
                    maske.frameNStart = frameN  # exact frame index
                    maske.setAutoDraw(True)
                frameRemains = 2.6 + 1.9- win.monitorFramePeriod * 0.75  # most of one frame period left
                if maske.status == STARTED and t >= frameRemains:
                    maske.setAutoDraw(False)
                # *ISI_L* period
                if t >= 0 and ISI_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_L.tStart = t
                    ISI_L.frameNStart = frameN  # exact frame index
                    ISI_L.start(2-t)
                elif ISI_L.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI_L*
                    local_stim.setPos(position)
                    local_stim.setImage(GL_fileName)
                    maske.setPos(position)
                    maske.setImage('Grafiken/Mask.png')
                    # component updates done
                    ISI_L.complete()  # finish the static period
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trials_LComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trials_L"-------

            for thisComponent in Trials_LComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            local_sound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if KeyL.keys in ['', [], None]:  # No response was made
                KeyL.keys=None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   KeyL.corr = 1  # correct non-response
                else:
                   KeyL.corr = 0  # failed to respond (incorrectly)
            # store data for exp_local_1 (TrialHandler)
            exp_local_1.addData('KeyL.keys',KeyL.keys)
            exp_local_1.addData('KeyL.corr', KeyL.corr)
            if KeyL.keys != None:  # we had a response
                exp_local_1.addData('KeyL.rt', KeyL.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'exp_local_1'
        
        # get names of stimulus parameters
        if exp_local_1.trialList in ([], [None], None):
            params = []
        else:
            params = exp_local_1.trialList[0].keys()
        # save data for this loop
        exp_local_1.saveAsText(filename + 'exp_local_1.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "pause_L"-------
        t = 0
        pause_LClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        #main_feedbackL.setText(u'Dr\xfccken Sie grüne Taste wenn Sie bereit sind, den Test fortzuf\xfchren.')
        main_feedbackL.setText(u'Press the green key when you are ready to continue the experiment.')
        key_read4 = event.BuilderKeyResponse()
        # keep track of which components have finished
        pause_LComponents = [head_feedbackL, main_feedbackL, key_read4]
        for thisComponent in pause_LComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "pause_L"-------
        while continueRoutine:
            # get current time
            t = pause_LClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_feedbackL* updates
            if t >= 0.0 and head_feedbackL.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_feedbackL.tStart = t
                head_feedbackL.frameNStart = frameN  # exact frame index
                head_feedbackL.setAutoDraw(True)
            
            # *main_feedbackL* updates
            if t >= 0.0 and main_feedbackL.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_feedbackL.tStart = t
                main_feedbackL.frameNStart = frameN  # exact frame index
                main_feedbackL.setAutoDraw(True)
            
            # *key_read4* updates
            if t >= 0.0 and key_read4.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read4.tStart = t
                key_read4.frameNStart = frameN  # exact frame index
                key_read4.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read4.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pause_LComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pause_L"-------
        for thisComponent in pause_LComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "pause_L" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        exp_local_2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'conditions_local_Navon_Part2.csv'),
            seed=None, name='exp_local_2')
        thisExp.addLoop(exp_local_2)  # add the loop to the experiment
        thisExp_local_2 = exp_local_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExp_local_2.rgb)
        if thisExp_local_2 != None:
            for paramName in thisExp_local_2.keys():
                exec(paramName + '= thisExp_local_2.' + paramName)
        
        for thisExp_local_2 in exp_local_2:
            currentLoop = exp_local_2
            # abbreviate parameter names if possible (e.g. rgb = thisExp_local_2.rgb)
            if thisExp_local_2 != None:
                for paramName in thisExp_local_2.keys():
                    exec(paramName + '= thisExp_local_2.' + paramName)
            
            # ------Prepare to start Routine "Trials_L"-------
            t = 0
            Trials_LClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(4.500000)
            # update component parameters for each repeat
            local_sound.setSound('Grafiken/Signal.wav', secs=0.075)
            KeyL = event.BuilderKeyResponse()
            # keep track of which components have finished
            Trials_LComponents = [Fixation_L, local_sound, KeyL, ISI_L, local_stim, maske]
            for thisComponent in Trials_LComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Trials_L"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Trials_LClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation_L* updates
                if t >= 2.0 and Fixation_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Fixation_L.tStart = t
                    Fixation_L.frameNStart = frameN  # exact frame index
                    Fixation_L.setAutoDraw(True)
                frameRemains = 2.0 + 0.500- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Fixation_L.status == STARTED and t >= frameRemains:
                    Fixation_L.setAutoDraw(False)
                # start/stop local_sound
                if t >= 2 and local_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    local_sound.tStart = t
                    local_sound.frameNStart = frameN  # exact frame index
                    local_sound.play()  # start the sound (it finishes automatically)
                frameRemains = 2 + 0.075- win.monitorFramePeriod * 0.75  # most of one frame period left
                if local_sound.status == STARTED and t >= frameRemains:
                    local_sound.stop()  # stop the sound (if longer than duration)
                
                # *KeyL* updates
                if t >= 2.5 and KeyL.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    KeyL.tStart = t
                    KeyL.frameNStart = frameN  # exact frame index
                    KeyL.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(KeyL.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                    #Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()


                frameRemains = 2.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if KeyL.status == STARTED and t >= frameRemains:
                    KeyL.status = STOPPED
                   
                if KeyL.status == STARTED:
                    theseKeys = event.getKeys(keyList=['h', 's'])
                    

                    ButtonBox.poll_for_response()

                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0:
                        if KeyL.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'h'
                                if response['key'] == 2:
                                    translated = 's'
                                KeyL.keys = translated # just the first key pressed
                                KeyL.rt = KeyL.clock.getTime()
                                #print "CONTROL: Ha apretado " + repr(KeyL.keys) + "."
                                # was this 'correct'?
                                if (KeyL.keys == str(corrAns)) or (KeyL.keys == corrAns):
                                    KeyL.corr = 1
                                    totalCorrect_local += 1
                                    #print "CORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    KeyL.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                # a response ends the routine
                                continueRoutine = False
                
                # *local_stim* updates
                if t >= 2.5 and local_stim.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    local_stim.tStart = t
                    local_stim.frameNStart = frameN  # exact frame index
                    local_stim.setAutoDraw(True)
                frameRemains = 2.5 + 0.100- win.monitorFramePeriod * 0.75  # most of one frame period left
                if local_stim.status == STARTED and t >= frameRemains:
                    local_stim.setAutoDraw(False)
                
                # *maske* updates
                if t >= 2.6 and maske.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    maske.tStart = t
                    maske.frameNStart = frameN  # exact frame index
                    maske.setAutoDraw(True)
                frameRemains = 2.6 + 1.9- win.monitorFramePeriod * 0.75  # most of one frame period left
                if maske.status == STARTED and t >= frameRemains:
                    maske.setAutoDraw(False)
                # *ISI_L* period
                if t >= 0 and ISI_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_L.tStart = t
                    ISI_L.frameNStart = frameN  # exact frame index
                    ISI_L.start(2-t)
                elif ISI_L.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI_L*
                    local_stim.setPos(position)
                    local_stim.setImage(GL_fileName)
                    maske.setPos(position)
                    maske.setImage('Grafiken/Mask.png')
                    # component updates done
                    ISI_L.complete()  # finish the static period
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trials_LComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trials_L"-------
            for thisComponent in Trials_LComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            local_sound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if KeyL.keys in ['', [], None]:  # No response was made
                KeyL.keys=None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   KeyL.corr = 1  # correct non-response
                else:
                   KeyL.corr = 0  # failed to respond (incorrectly)
            # store data for exp_local_2 (TrialHandler)
            exp_local_2.addData('KeyL.keys',KeyL.keys)
            exp_local_2.addData('KeyL.corr', KeyL.corr)
            if KeyL.keys != None:  # we had a response
                exp_local_2.addData('KeyL.rt', KeyL.rt)
            thisExp.nextEntry()
            
        # completed  repeats of 'exp_local_2'
        
        # get names of stimulus parameters
        if exp_local_2.trialList in ([], [None], None):
            params = []
        else:
            params = exp_local_2.trialList[0].keys()
        # save data for this loop
        exp_local_2.saveAsText(filename + 'exp_local_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
    # completed 1 repeats of 'local_Block'
    
    
    # set up handler to look after randomisation of conditions etc
    global_block = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='global_block')
    thisExp.addLoop(global_block)  # add the loop to the experiment
    thisGlobal_block = global_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGlobal_block.rgb)
    if thisGlobal_block != None:
        for paramName in thisGlobal_block.keys():
            exec(paramName + '= thisGlobal_block.' + paramName)
    
    for thisGlobal_block in global_block:
        currentLoop = global_block
        # abbreviate parameter names if possible (e.g. rgb = thisGlobal_block.rgb)
        if thisGlobal_block != None:
            for paramName in thisGlobal_block.keys():
                exec(paramName + '= thisGlobal_block.' + paramName)
        
        # ------Prepare to start Routine "globinstr"-------
        t = 0
        globinstrClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_read6 = event.BuilderKeyResponse()
        # keep track of which components have finished
        globinstrComponents = [head_globinstr, main_globinstr, foot_globinstr, key_read6, Hglo, Sglo]
        for thisComponent in globinstrComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "globinstr"-------
        while continueRoutine:
            # get current time
            t = globinstrClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_globinstr* updates
            if t >= 0.0 and head_globinstr.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_globinstr.tStart = t
                head_globinstr.frameNStart = frameN  # exact frame index
                head_globinstr.setAutoDraw(True)
            
            # *main_globinstr* updates
            if t >= 0.0 and main_globinstr.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_globinstr.tStart = t
                main_globinstr.frameNStart = frameN  # exact frame index
                main_globinstr.setAutoDraw(True)
            
            # *foot_globinstr* updates
            if t >= 0.0 and foot_globinstr.status == NOT_STARTED:
                # keep track of start time/frame for later
                foot_globinstr.tStart = t
                foot_globinstr.frameNStart = frameN  # exact frame index
                foot_globinstr.setAutoDraw(True)
            
            # *key_read6* updates
            if t >= 0.0 and key_read6.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read6.tStart = t
                key_read6.frameNStart = frameN  # exact frame index
                key_read6.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read6.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # *Hglo* updates
            if t >= 0.0 and Hglo.status == NOT_STARTED:
                # keep track of start time/frame for later
                Hglo.tStart = t
                Hglo.frameNStart = frameN  # exact frame index
                Hglo.setAutoDraw(True)
            
            # *Sglo* updates
            if t >= 0.0 and Sglo.status == NOT_STARTED:
                # keep track of start time/frame for later
                Sglo.tStart = t
                Sglo.frameNStart = frameN  # exact frame index
                Sglo.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in globinstrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "globinstr"-------
        for thisComponent in globinstrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "globinstr" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_global = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions_training_global_Navon.csv'),
            seed=None, name='practice_global')
        thisExp.addLoop(practice_global)  # add the loop to the experiment
        thisPractice_global = practice_global.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_global.rgb)
        if thisPractice_global != None:
            for paramName in thisPractice_global.keys():
                exec(paramName + '= thisPractice_global.' + paramName)
        
        for thisPractice_global in practice_global:
            currentLoop = practice_global
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_global.rgb)
            if thisPractice_global != None:
                for paramName in thisPractice_global.keys():
                    exec(paramName + '= thisPractice_global.' + paramName)
            
            # ------Prepare to start Routine "Trials_G"-------
            t = 0
            Trials_GClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(4.500000)
            # update component parameters for each repeat
            global_sound.setSound('Grafiken/Signal.wav', secs=0.075)
            KeyG = event.BuilderKeyResponse()
            # keep track of which components have finished
            Trials_GComponents = [Fixation_G, global_sound, KeyG, ISI_L_2, global_stim, maske_g]
            for thisComponent in Trials_GComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Trials_G"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Trials_GClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation_G* updates
                if t >= 2.0 and Fixation_G.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Fixation_G.tStart = t
                    Fixation_G.frameNStart = frameN  # exact frame index
                    Fixation_G.setAutoDraw(True)
                frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Fixation_G.status == STARTED and t >= frameRemains:
                    Fixation_G.setAutoDraw(False)
                # start/stop global_sound
                if t >= 2 and global_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    global_sound.tStart = t
                    global_sound.frameNStart = frameN  # exact frame index
                    global_sound.play()  # start the sound (it finishes automatically)
                frameRemains = 2 + 0.075- win.monitorFramePeriod * 0.75  # most of one frame period left
                if global_sound.status == STARTED and t >= frameRemains:
                    global_sound.stop()  # stop the sound (if longer than duration)
                
                # *KeyG* updates
                if t >= 2.5 and KeyG.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    KeyG.tStart = t
                    KeyG.frameNStart = frameN  # exact frame index
                    KeyG.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(KeyG.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                    #Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()

                frameRemains = 2.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if KeyG.status == STARTED and t >= frameRemains:
                    KeyG.status = STOPPED

                if KeyG.status == STARTED:
                    theseKeys = event.getKeys(keyList=['h', 's'])
                    
                    ButtonBox.poll_for_response()

                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0:
                        if KeyG.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'h'
                                if response['key'] == 2:
                                    translated = 's'
                                KeyG.keys = translated # just the first key pressed
                                KeyG.rt = KeyG.clock.getTime()
                                #print "CONTROL: Ha apretado " + repr(KeyG.keys) + "."
                                # was this 'correct'?
                                if (KeyG.keys == str(corrAns)) or (KeyG.keys == corrAns):
                                    KeyG.corr = 1
                                    ##print "CORRECTO: Ha apretado " + repr(KeyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    KeyG.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(KeyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                # a response ends the routine
                                continueRoutine = False
                
                # *global_stim* updates
                if t >= 2.500 and global_stim.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    global_stim.tStart = t
                    global_stim.frameNStart = frameN  # exact frame index
                    global_stim.setAutoDraw(True)
                frameRemains = 2.500 + 0.100- win.monitorFramePeriod * 0.75  # most of one frame period left
                if global_stim.status == STARTED and t >= frameRemains:
                    global_stim.setAutoDraw(False)
                
                # *maske_g* updates
                if t >= 2.6 and maske_g.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    maske_g.tStart = t
                    maske_g.frameNStart = frameN  # exact frame index
                    maske_g.setAutoDraw(True)
                frameRemains = 2.6 + 1.9- win.monitorFramePeriod * 0.75  # most of one frame period left
                if maske_g.status == STARTED and t >= frameRemains:
                    maske_g.setAutoDraw(False)
                # *ISI_L_2* period
                if t >= 0 and ISI_L_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_L_2.tStart = t
                    ISI_L_2.frameNStart = frameN  # exact frame index
                    ISI_L_2.start(2.0)
                elif ISI_L_2.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI_L_2*
                    global_stim.setPos(position)
                    global_stim.setImage(GL_fileName)
                    maske_g.setPos(position)
                    maske_g.setImage('Grafiken/Mask.png')
                    # component updates done
                    ISI_L_2.complete()  # finish the static period
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trials_GComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trials_G"-------
            for thisComponent in Trials_GComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            global_sound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if KeyG.keys in ['', [], None]:  # No response was made
                KeyG.keys=None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   KeyG.corr = 1  # correct non-response
                else:
                   KeyG.corr = 0  # failed to respond (incorrectly)
            # store data for practice_global (TrialHandler)
            practice_global.addData('KeyG.keys',KeyG.keys)
            practice_global.addData('KeyG.corr', KeyG.corr)
            if KeyG.keys != None:  # we had a response
                practice_global.addData('KeyG.rt', KeyG.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'practice_global'
        
        # get names of stimulus parameters
        if practice_global.trialList in ([], [None], None):
            params = []
        else:
            params = practice_global.trialList[0].keys()
        # save data for this loop
        practice_global.saveAsText(filename + 'practice_global.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "feedbackG_train"-------
        t = 0
        feedbackG_trainClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        nCorr = practice_global.data['KeyG.corr'].sum() #.std(), .mean() also available
        meanRt = practice_global.data['KeyG.rt'].mean()
        #msg = "Sie haben %i Stimuli richtig beantwortet \n (Reaktionszeit=%.2f s)" %(nCorr,meanRt)
        msg = "You have answered %i trials correctly \n (reaction time = %.2f s)" %(nCorr,meanRt)
        main_feedbackG_2.setText(msg)
        key_read8_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        feedbackG_trainComponents = [head_feedbackG_2, main_feedbackG_2, foot_feedbackG_2, key_read8_2]
        for thisComponent in feedbackG_trainComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedbackG_train"-------
        while continueRoutine:
            # get current time
            t = feedbackG_trainClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *head_feedbackG_2* updates
            if t >= 0.0 and head_feedbackG_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_feedbackG_2.tStart = t
                head_feedbackG_2.frameNStart = frameN  # exact frame index
                head_feedbackG_2.setAutoDraw(True)
            
            # *main_feedbackG_2* updates
            if t >= 0.0 and main_feedbackG_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_feedbackG_2.tStart = t
                main_feedbackG_2.frameNStart = frameN  # exact frame index
                main_feedbackG_2.setAutoDraw(True)
            
            # *foot_feedbackG_2* updates
            if t >= 0.0 and foot_feedbackG_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                foot_feedbackG_2.tStart = t
                foot_feedbackG_2.frameNStart = frameN  # exact frame index
                foot_feedbackG_2.setAutoDraw(True)
            
            # *key_read8_2* updates
            if t >= 0.0 and key_read8_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read8_2.tStart = t
                key_read8_2.frameNStart = frameN  # exact frame index
                key_read8_2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read8_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackG_trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackG_train"-------
        for thisComponent in feedbackG_trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "feedbackG_train" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "instr_realG"-------
        t = 0
        instr_realGClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_read9 = event.BuilderKeyResponse()
        # keep track of which components have finished
        instr_realGComponents = [head_globreal, main_globreal, foot_globreal, key_read9]
        for thisComponent in instr_realGComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instr_realG"-------
        while continueRoutine:
            # get current time
            t = instr_realGClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_globreal* updates
            if t >= 0.0 and head_globreal.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_globreal.tStart = t
                head_globreal.frameNStart = frameN  # exact frame index
                head_globreal.setAutoDraw(True)
            
            # *main_globreal* updates
            if t >= 0.0 and main_globreal.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_globreal.tStart = t
                main_globreal.frameNStart = frameN  # exact frame index
                main_globreal.setAutoDraw(True)
            
            # *foot_globreal* updates
            if t >= 0.0 and foot_globreal.status == NOT_STARTED:
                # keep track of start time/frame for later
                foot_globreal.tStart = t
                foot_globreal.frameNStart = frameN  # exact frame index
                foot_globreal.setAutoDraw(True)
            
            # *key_read9* updates
            if t >= 0.0 and key_read9.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read9.tStart = t
                key_read9.frameNStart = frameN  # exact frame index
                key_read9.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read9.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instr_realGComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instr_realG"-------
        for thisComponent in instr_realGComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "instr_realG" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        exp_global_1 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions_global_Navon_Part1.csv'),
            seed=None, name='exp_global_1')
        thisExp.addLoop(exp_global_1)  # add the loop to the experiment
        thisExp_global_1 = exp_global_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExp_global_1.rgb)
        if thisExp_global_1 != None:
            for paramName in thisExp_global_1.keys():
                exec(paramName + '= thisExp_global_1.' + paramName)
        
        for thisExp_global_1 in exp_global_1:
            currentLoop = exp_global_1
            # abbreviate parameter names if possible (e.g. rgb = thisExp_global_1.rgb)
            if thisExp_global_1 != None:
                for paramName in thisExp_global_1.keys():
                    exec(paramName + '= thisExp_global_1.' + paramName)
            
            # ------Prepare to start Routine "Trials_G"-------
            t = 0
            Trials_GClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(4.500000)
            # update component parameters for each repeat
            global_sound.setSound('Grafiken/Signal.wav', secs=0.075)
            KeyG = event.BuilderKeyResponse()
            # keep track of which components have finished
            Trials_GComponents = [Fixation_G, global_sound, KeyG, ISI_L_2, global_stim, maske_g]
            for thisComponent in Trials_GComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Trials_G"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Trials_GClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation_G* updates
                if t >= 2.0 and Fixation_G.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Fixation_G.tStart = t
                    Fixation_G.frameNStart = frameN  # exact frame index
                    Fixation_G.setAutoDraw(True)
                frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Fixation_G.status == STARTED and t >= frameRemains:
                    Fixation_G.setAutoDraw(False)
                # start/stop global_sound
                if t >= 2 and global_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    global_sound.tStart = t
                    global_sound.frameNStart = frameN  # exact frame index
                    global_sound.play()  # start the sound (it finishes automatically)
                frameRemains = 2 + 0.075- win.monitorFramePeriod * 0.75  # most of one frame period left
                if global_sound.status == STARTED and t >= frameRemains:
                    global_sound.stop()  # stop the sound (if longer than duration)
                
                # *KeyG* updates
                if t >= 2.5 and KeyG.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    KeyG.tStart = t
                    KeyG.frameNStart = frameN  # exact frame index
                    KeyG.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(KeyG.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                    #Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()


                frameRemains = 2.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if KeyG.status == STARTED and t >= frameRemains:
                    KeyG.status = STOPPED

                if KeyG.status == STARTED:
                    theseKeys = event.getKeys(keyList=['h', 's'])
                    
                    ButtonBox.poll_for_response()

                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0:
                        if KeyG.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'h'
                                if response['key'] == 2:
                                    translated = 's'
                                KeyG.keys = translated # just the first key pressed
                                KeyG.rt = KeyG.clock.getTime()
                                #print "CONTROL: Ha apretado " + repr(KeyG.keys) + "."
                                # was this 'correct'?
                                if (KeyG.keys == str(corrAns)) or (KeyG.keys == corrAns):
                                    KeyG.corr = 1
                                    totalCorrect_global += 1
                                    #print "CORRECTO: Ha apretado " + repr(KeyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    KeyG.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(KeyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                # a response ends the routine
                                continueRoutine = False
                
                # *global_stim* updates
                if t >= 2.500 and global_stim.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    global_stim.tStart = t
                    global_stim.frameNStart = frameN  # exact frame index
                    global_stim.setAutoDraw(True)
                frameRemains = 2.500 + 0.100- win.monitorFramePeriod * 0.75  # most of one frame period left
                if global_stim.status == STARTED and t >= frameRemains:
                    global_stim.setAutoDraw(False)
                
                # *maske_g* updates
                if t >= 2.6 and maske_g.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    maske_g.tStart = t
                    maske_g.frameNStart = frameN  # exact frame index
                    maske_g.setAutoDraw(True)
                frameRemains = 2.6 + 1.9- win.monitorFramePeriod * 0.75  # most of one frame period left
                if maske_g.status == STARTED and t >= frameRemains:
                    maske_g.setAutoDraw(False)
                # *ISI_L_2* period
                if t >= 0 and ISI_L_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_L_2.tStart = t
                    ISI_L_2.frameNStart = frameN  # exact frame index
                    ISI_L_2.start(2.0)
                elif ISI_L_2.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI_L_2*
                    global_stim.setPos(position)
                    global_stim.setImage(GL_fileName)
                    maske_g.setPos(position)
                    maske_g.setImage('Grafiken/Mask.png')
                    # component updates done
                    ISI_L_2.complete()  # finish the static period
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trials_GComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trials_G"-------
            for thisComponent in Trials_GComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            global_sound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if KeyG.keys in ['', [], None]:  # No response was made
                KeyG.keys=None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   KeyG.corr = 1  # correct non-response
                else:
                   KeyG.corr = 0  # failed to respond (incorrectly)
            # store data for exp_global_1 (TrialHandler)
            exp_global_1.addData('KeyG.keys',KeyG.keys)
            exp_global_1.addData('KeyG.corr', KeyG.corr)
            if KeyG.keys != None:  # we had a response
                exp_global_1.addData('KeyG.rt', KeyG.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'exp_global_1'
        
        # get names of stimulus parameters
        if exp_global_1.trialList in ([], [None], None):
            params = []
        else:
            params = exp_global_1.trialList[0].keys()
        # save data for this loop
        exp_global_1.saveAsText(filename + 'exp_global_1.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "pause_G"-------
        t = 0
        pause_GClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        #main_feedbackG.setText(u'Dr\xfccken Sie grüne Taste wenn Sie bereit sind, den Test fortzuf\xfchren.')
        main_feedbackG.setText(u'Press the green key when you are ready to continue the experiment.')

        key_read8 = event.BuilderKeyResponse()
        # keep track of which components have finished
        pause_GComponents = [head_feedbackG, main_feedbackG, key_read8]
        for thisComponent in pause_GComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "pause_G"-------
        while continueRoutine:
            # get current time
            t = pause_GClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_feedbackG* updates
            if t >= 0.0 and head_feedbackG.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_feedbackG.tStart = t
                head_feedbackG.frameNStart = frameN  # exact frame index
                head_feedbackG.setAutoDraw(True)
            
            # *main_feedbackG* updates
            if t >= 0.0 and main_feedbackG.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_feedbackG.tStart = t
                main_feedbackG.frameNStart = frameN  # exact frame index
                main_feedbackG.setAutoDraw(True)
            
            # *key_read8* updates
            if t >= 0.0 and key_read8.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read8.tStart = t
                key_read8.frameNStart = frameN  # exact frame index
                key_read8.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read8.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
                            #print("green button pressed")
                            continueRoutine = False
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pause_GComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pause_G"-------
        for thisComponent in pause_GComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "pause_G" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        exp_global_2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'conditions_global_Navon_Part2.csv'),
            seed=None, name='exp_global_2')
        thisExp.addLoop(exp_global_2)  # add the loop to the experiment
        thisExp_global_2 = exp_global_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExp_global_2.rgb)
        if thisExp_global_2 != None:
            for paramName in thisExp_global_2.keys():
                exec(paramName + '= thisExp_global_2.' + paramName)
        
        for thisExp_global_2 in exp_global_2:
            currentLoop = exp_global_2
            # abbreviate parameter names if possible (e.g. rgb = thisExp_global_2.rgb)
            if thisExp_global_2 != None:
                for paramName in thisExp_global_2.keys():
                    exec(paramName + '= thisExp_global_2.' + paramName)
            
            # ------Prepare to start Routine "Trials_G"-------
            t = 0
            Trials_GClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(4.500000)
            # update component parameters for each repeat
            global_sound.setSound('Grafiken/Signal.wav', secs=0.075)
            KeyG = event.BuilderKeyResponse()
            # keep track of which components have finished
            Trials_GComponents = [Fixation_G, global_sound, KeyG, ISI_L_2, global_stim, maske_g]
            for thisComponent in Trials_GComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Trials_G"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Trials_GClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation_G* updates
                if t >= 2.0 and Fixation_G.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Fixation_G.tStart = t
                    Fixation_G.frameNStart = frameN  # exact frame index
                    Fixation_G.setAutoDraw(True)
                frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Fixation_G.status == STARTED and t >= frameRemains:
                    Fixation_G.setAutoDraw(False)
                # start/stop global_sound
                if t >= 2 and global_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    global_sound.tStart = t
                    global_sound.frameNStart = frameN  # exact frame index
                    global_sound.play()  # start the sound (it finishes automatically)
                frameRemains = 2 + 0.075- win.monitorFramePeriod * 0.75  # most of one frame period left
                if global_sound.status == STARTED and t >= frameRemains:
                    global_sound.stop()  # stop the sound (if longer than duration)
                
                # *KeyG* updates
                if t >= 2.5 and KeyG.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    KeyG.tStart = t
                    KeyG.frameNStart = frameN  # exact frame index
                    KeyG.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(KeyG.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                    #Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()
                    
                frameRemains = 2.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if KeyG.status == STARTED and t >= frameRemains:
                    KeyG.status = STOPPED

                if KeyG.status == STARTED:
                    theseKeys = event.getKeys(keyList=['h', 's'])
                    
                    ButtonBox.poll_for_response()

                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0:
                        if KeyG.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'h'
                                if response['key'] == 2:
                                    translated = 's'
                                KeyG.keys = translated # just the first key pressed
                                KeyG.rt = KeyG.clock.getTime()
                                #print "CONTROL: Ha apretado " + repr(KeyG.keys) + "."
                                # was this 'correct'?
                                if (KeyG.keys == str(corrAns)) or (KeyG.keys == corrAns):
                                    KeyG.corr = 1
                                    totalCorrect_global += 1
                                    #print "CORRECTO: Ha apretado " + repr(KeyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    KeyG.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(KeyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                # a response ends the routine
                                continueRoutine = False
                
                # *global_stim* updates
                if t >= 2.500 and global_stim.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    global_stim.tStart = t
                    global_stim.frameNStart = frameN  # exact frame index
                    global_stim.setAutoDraw(True)
                frameRemains = 2.500 + 0.100- win.monitorFramePeriod * 0.75  # most of one frame period left
                if global_stim.status == STARTED and t >= frameRemains:
                    global_stim.setAutoDraw(False)
                
                # *maske_g* updates
                if t >= 2.6 and maske_g.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    maske_g.tStart = t
                    maske_g.frameNStart = frameN  # exact frame index
                    maske_g.setAutoDraw(True)
                frameRemains = 2.6 + 1.9- win.monitorFramePeriod * 0.75  # most of one frame period left
                if maske_g.status == STARTED and t >= frameRemains:
                    maske_g.setAutoDraw(False)
                # *ISI_L_2* period
                if t >= 0 and ISI_L_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_L_2.tStart = t
                    ISI_L_2.frameNStart = frameN  # exact frame index
                    ISI_L_2.start(2.0)
                elif ISI_L_2.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI_L_2*
                    global_stim.setPos(position)
                    global_stim.setImage(GL_fileName)
                    maske_g.setPos(position)
                    maske_g.setImage('Grafiken/Mask.png')
                    # component updates done
                    ISI_L_2.complete()  # finish the static period
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trials_GComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trials_G"-------
            for thisComponent in Trials_GComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            global_sound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if KeyG.keys in ['', [], None]:  # No response was made
                KeyG.keys=None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   KeyG.corr = 1  # correct non-response
                else:
                   KeyG.corr = 0  # failed to respond (incorrectly)
            # store data for exp_global_2 (TrialHandler)
            exp_global_2.addData('KeyG.keys',KeyG.keys)
            exp_global_2.addData('KeyG.corr', KeyG.corr)
            if KeyG.keys != None:  # we had a response
                exp_global_2.addData('KeyG.rt', KeyG.rt)
            thisExp.nextEntry()
            
        # completed  repeats of 'exp_global_2'
        
        # get names of stimulus parameters
        if exp_global_2.trialList in ([], [None], None):
            params = []
        else:
            params = exp_global_2.trialList[0].keys()
        # save data for this loop
        exp_global_2.saveAsText(filename + 'exp_global_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
    # completed 1 repeats of 'global_block'
    
# completed 1 repeats of 'Block_select'


# ------Prepare to start Routine "end_question"-------
t = 0
end_questionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_read10 = event.BuilderKeyResponse()
# keep track of which components have finished
end_questionComponents = [main_quest, foot_quest, key_read10]
for thisComponent in end_questionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_question"-------
while continueRoutine:
    # get current time
    t = end_questionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_quest* updates
    if t >= 0.0 and main_quest.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_quest.tStart = t
        main_quest.frameNStart = frameN  # exact frame index
        main_quest.setAutoDraw(True)
    
    # *foot_quest* updates
    if t >= 0.0 and foot_quest.status == NOT_STARTED:
        # keep track of start time/frame for later
        foot_quest.tStart = t
        foot_quest.frameNStart = frameN  # exact frame index
        foot_quest.setAutoDraw(True)
    
    # *key_read10* updates
    if t >= 0.0 and key_read10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_read10.tStart = t
        key_read10.frameNStart = frameN  # exact frame index
        key_read10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_read10.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_question"-------
for thisComponent in end_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "question1"-------
t = 0
question1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating1.reset()
key_finish1 = event.BuilderKeyResponse()
# keep track of which components have finished
question1Components = [main_question1, rating1, key_finish1]
for thisComponent in question1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "question1"-------
while continueRoutine:
    # get current time
    t = question1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_question1* updates
    if t >= 0.0 and main_question1.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_question1.tStart = t
        main_question1.frameNStart = frameN  # exact frame index
        main_question1.setAutoDraw(True)
    # *rating1* updates
    if t >= 0.0 and rating1.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating1.tStart = t
        rating1.frameNStart = frameN  # exact frame index
        rating1.setAutoDraw(True)
    continueRoutine &= rating1.noResponse  # a response ends the trial
    
    # *key_finish1* updates
    if t >= 0.0 and key_finish1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_finish1.tStart = t
        key_finish1.frameNStart = frameN  # exact frame index
        key_finish1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_finish1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question1"-------
for thisComponent in question1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating1.response', rating1.getRating())
thisExp.nextEntry()
# the Routine "question1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "question2"-------
t = 0
question2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating2.reset()
key_finish2 = event.BuilderKeyResponse()
# keep track of which components have finished
question2Components = [main_question2, rating2, key_finish2]
for thisComponent in question2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "question2"-------
while continueRoutine:
    # get current time
    t = question2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_question2* updates
    if t >= 0.0 and main_question2.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_question2.tStart = t
        main_question2.frameNStart = frameN  # exact frame index
        main_question2.setAutoDraw(True)
    # *rating2* updates
    if t >= 0.0 and rating2.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating2.tStart = t
        rating2.frameNStart = frameN  # exact frame index
        rating2.setAutoDraw(True)
    continueRoutine &= rating2.noResponse  # a response ends the trial
    
    # *key_finish2* updates
    if t >= 0.0 and key_finish2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_finish2.tStart = t
        key_finish2.frameNStart = frameN  # exact frame index
        key_finish2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_finish2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question2"-------
for thisComponent in question2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating2.response', rating2.getRating())
thisExp.nextEntry()
# the Routine "question2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "question3"-------
t = 0
question3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating3.reset()
key_finish3 = event.BuilderKeyResponse()
# keep track of which components have finished
question3Components = [main_question3, rating3, key_finish3]
for thisComponent in question3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "question3"-------
while continueRoutine:
    # get current time
    t = question3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_question3* updates
    if t >= 0.0 and main_question3.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_question3.tStart = t
        main_question3.frameNStart = frameN  # exact frame index
        main_question3.setAutoDraw(True)
    # *rating3* updates
    if t >= 0.0 and rating3.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating3.tStart = t
        rating3.frameNStart = frameN  # exact frame index
        rating3.setAutoDraw(True)
    continueRoutine &= rating3.noResponse  # a response ends the trial
    
    # *key_finish3* updates
    if t >= 0.0 and key_finish3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_finish3.tStart = t
        key_finish3.frameNStart = frameN  # exact frame index
        key_finish3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_finish3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question3"-------
for thisComponent in question3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating3.response', rating3.getRating())
thisExp.nextEntry()
# the Routine "question3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "question4"-------
t = 0
question4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating4.reset()
key_finish4 = event.BuilderKeyResponse()
# keep track of which components have finished
question4Components = [main_question4, rating4, key_finish4]
for thisComponent in question4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "question4"-------
while continueRoutine:
    # get current time
    t = question4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_question4* updates
    if t >= 0.0 and main_question4.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_question4.tStart = t
        main_question4.frameNStart = frameN  # exact frame index
        main_question4.setAutoDraw(True)
    # *rating4* updates
    if t >= 0.0 and rating4.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating4.tStart = t
        rating4.frameNStart = frameN  # exact frame index
        rating4.setAutoDraw(True)
    continueRoutine &= rating4.noResponse  # a response ends the trial
    
    # *key_finish4* updates
    if t >= 0.0 and key_finish4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_finish4.tStart = t
        key_finish4.frameNStart = frameN  # exact frame index
        key_finish4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_finish4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question4"-------
for thisComponent in question4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating4.response', rating4.getRating())
thisExp.nextEntry()
# the Routine "question4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedback_final"-------
t = 0
feedback_finalClock.reset()  # clock
frameN = -1
continueRoutine = True

# update component parameters for each repeat
#nCorr = exp_global.data['KeyG.corr'].sum() #.std(), .mean() also available
#meanRt = exp_global.data['KeyG.rt'].mean()
#msg = "Globaler Buchstabe: Sie haben %i Stimuli richtig beantwortet \n (Reaktionszeit=%.2f s)" %(nCorr,meanRt)
#msg = "Globaler Buchstabe: Sie haben %i Stimuli richtig beantwortet \n" %(totalCorrect_global)
msg = "Global letter: You have answered %i trials correctly \n" %(totalCorrect_global)
main_feedback_final.setText(msg)
key_read_final = event.BuilderKeyResponse()
# keep track of which components have finished
feedback_finalComponents = [head_feedback_final, main_feedback_final, foot_feedback_final, key_read_final]
for thisComponent in feedback_finalComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "feedback_final"-------
while continueRoutine:
    # get current time
    t = feedback_finalClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *head_feedback_final* updates
    if t >= 0.0 and head_feedback_final.status == NOT_STARTED:
        # keep track of start time/frame for later
        head_feedback_final.tStart = t
        head_feedback_final.frameNStart = frameN  # exact frame index
        head_feedback_final.setAutoDraw(True)
    
    # *main_feedback_final* updates
    if t >= 0.0 and main_feedback_final.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_feedback_final.tStart = t
        main_feedback_final.frameNStart = frameN  # exact frame index
        main_feedback_final.setAutoDraw(True)
    
    # *foot_feedback_final* updates
    if t >= 0.0 and foot_feedback_final.status == NOT_STARTED:
        # keep track of start time/frame for later
        foot_feedback_final.tStart = t
        foot_feedback_final.frameNStart = frameN  # exact frame index
        foot_feedback_final.setAutoDraw(True)
    
    # *key_read_final* updates
    if t >= 0.0 and key_read_final.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_read_final.tStart = t
        key_read_final.frameNStart = frameN  # exact frame index
        key_read_final.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_read_final.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback_final"-------
for thisComponent in feedback_finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "feedback_final" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedback_final2"-------
t = 0
feedback_final2Clock.reset()  # clock
frameN = -1
continueRoutine = True

# update component parameters for each repeat
#nCorr = exp_local.data['KeyL.corr'].sum() #.std(), .mean() also available
#meanRt = exp_local.data['KeyL.rt'].mean()
#msg = "Lokale Buchstaben (Elemente): Sie haben %i Stimuli richtig beantwortet \n (Reaktionszeit=%.2f s)" %(nCorr,meanRt)
#msg = "Lokale Buchstaben (Elemente): Sie haben %i Stimuli richtig beantwortet \n" %(totalCorrect_local)
msg = "Local letters (elements): You have answered %i trials correctly \n" %(totalCorrect_local)

main_feedback_final_2.setText(msg)
key_read_final_2 = event.BuilderKeyResponse()
# keep track of which components have finished
feedback_final2Components = [head_feedback_final_2, main_feedback_final_2, foot_feedback_final_2, key_read_final_2]
for thisComponent in feedback_final2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "feedback_final2"-------
while continueRoutine:
    # get current time
    t = feedback_final2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *head_feedback_final_2* updates
    if t >= 0.0 and head_feedback_final_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        head_feedback_final_2.tStart = t
        head_feedback_final_2.frameNStart = frameN  # exact frame index
        head_feedback_final_2.setAutoDraw(True)
    
    # *main_feedback_final_2* updates
    if t >= 0.0 and main_feedback_final_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_feedback_final_2.tStart = t
        main_feedback_final_2.frameNStart = frameN  # exact frame index
        main_feedback_final_2.setAutoDraw(True)
    
    # *foot_feedback_final_2* updates
    if t >= 0.0 and foot_feedback_final_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        foot_feedback_final_2.tStart = t
        foot_feedback_final_2.frameNStart = frameN  # exact frame index
        foot_feedback_final_2.setAutoDraw(True)
    
    # *key_read_final_2* updates
    if t >= 0.0 and key_read_final_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_read_final_2.tStart = t
        key_read_final_2.frameNStart = frameN  # exact frame index
        key_read_final_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_read_final_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        ButtonBox.poll_for_response()
        if ButtonBox.response_queue_size() > 0:
            response = ButtonBox.get_next_response()
            if response['pressed'] == True:
                if response['key'] == 7:
                    #print("green button pressed")
                    continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_final2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback_final2"-------
for thisComponent in feedback_final2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "feedback_final2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Thank_you"-------
t = 0
Thank_youClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
Thank_youComponents = [main_thanks]
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thank_you"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Thank_youClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_thanks* updates
    if t >= 0.0 and main_thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_thanks.tStart = t
        main_thanks.frameNStart = frameN  # exact frame index
        main_thanks.setAutoDraw(True)
    frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if main_thanks.status == STARTED and t >= frameRemains:
        main_thanks.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_you"-------
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
