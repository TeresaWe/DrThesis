#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Do 11 Mai 2017 16:26:14 CEST
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
expName = 'AGLT'  # from the Builder filename that created this script
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
main_geninstr = visual.TextStim(win=win, name='main_geninstr',
    #text=u'In diesem Experiment h\xf6ren Sie eine Reihe von Melodien, die jeweils aus 9 T\xf6nen in Gruppen aus 3 T\xf6nen bestehen. \nIhre Aufgabe ist es, bei jeder Melodie korrekt und so schnell wie m\xf6glich zu entscheiden ob\n\n- die Melodie als Ganzes (in der globalen Bedingung) oder \n- die T\xf6ne der 3-Ton-Gruppierungen (in der lokalen Bedingung) \n\nsteigen oder fallen. Es gibt vier verschiedene Melodieverl\xe4ufe (siehe Grafik). Das Experiment besteht aus einem globalen und einem lokalen Block. Zuvor gibt es jeweils ein paar \xdcbungsdurchg\xe4nge. \n\n\n\n',
    text=u'In this experiment, you will hear several melodies consisting of 9 tones which are grouped as triplets. \nYour task is to decide for each melody as fast and as correctly as possible whether\n\n- the melody as a whole (in the global condition) or \n- the notes of the triplets (in the local condition) \n\n are rising or falling. There are four different types of melodic motions (see graphics below). The experiment consists of one global and one local section. Before, there will be a few practice trials for each condition. \n\n\n\n', 
    font='Arial',
    pos=(0, 0), height=0.065, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
foot_geninstr = visual.TextStim(win=win, name='foot_geninstr',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
melodiesGL = visual.ImageStim(
    win=win, name='melodiesGL',
    image='Paradigms/auditory global local/Bilder/melodies_white.png', mask=None,
    ori=0, pos=(0, -0.5), size=(1.698, 0.438),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
head_geninstr = visual.TextStim(win=win, name='head_geninstr',
    #text='Herzlich Willkommen!',
    text='Welcome!',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "example_2"
example_2Clock = core.Clock()
example = visual.TextStim(win=win, name='example',
    #text='Beispiel',
    text='Example',
    font='Arial',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
textloop = visual.TextStim(win=win, name='textloop',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, -0.2), size=(0.454, 0.432),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "locinstr"
locinstrClock = core.Clock()
head_locinstr = visual.TextStim(win=win, name='head_locinstr',
    #text='3-Ton-Gruppen',
    text='Triplets!',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_locinstr = visual.TextStim(win=win, name='main_locinstr',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_locinstr = visual.TextStim(win=win, name='foot_locinstr',
    #text='Weiter mit der grünen Taste!',
    text = 'Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "instr_practiceL"
instr_practiceLClock = core.Clock()
head_practiceloc = visual.TextStim(win=win, name='head_practiceloc',
    #text=u'\xdcbung!',
    text=u'Practice session!',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_practiceloc = visual.TextStim(win=win, name='main_practiceloc',
    #text=u'Konzentrieren Sie sich auf die 3-Ton-Gruppierungen!\n\n<Rechte Taste> = 3-Ton-Gruppierung steigt in sich, \n<Linke Taste> = 3-Ton-Gruppierung f\xe4llt in sich\n\nVersuchen Sie keine Fehler zu machen und so schnell wie m\xf6glich zu reagieren!\n\n\n\n',
    text=u'Concentrate on the triplets! \n\n<Right Key> = Triplets are rising, \n<Left Key> = Triplets are falling \n\nTry to avoid mistakes and react as fast as possible!\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_practiceloc = visual.TextStim(win=win, name='foot_practiceloc',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Isi"
IsiClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "Trails_L"
Trails_LClock = core.Clock()
Listen_L = visual.TextStim(win=win, name='Listen_L',
    #text='Achtung!',
    text='Attention!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
local_sound = sound.Sound('A', secs=-1)
local_sound.setVolume(1)
ISI_L = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L')

# Initialize components for Routine "feedbackL"
feedbackLClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!


head_feedbackL = visual.TextStim(win=win, name='head_feedbackL',
    #text=u'\xdcbung beendet!',
    text=u'Practice session completed!',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
main_feedbackL = visual.TextStim(win=win, name='main_feedbackL',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
foot_feedbackL = visual.TextStim(win=win, name='foot_feedbackL',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "instr_realL"
instr_realLClock = core.Clock()
head_locreal = visual.TextStim(win=win, name='head_locreal',
    #text='Beginn des Experiments',
    text='Start of the experiment',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_locreal = visual.TextStim(win=win, name='main_locreal',
    #text=u'Sie sind nun gut vorbereitet, um mit dem Experiment zu beginnen! Wenn etwas unklar ist, fragen Sie bitte jetzt den/die Versuchsleiter/-in.\n\nBitte versuchen Sie so schnell und korrekt wie m\xf6glich zu antworten!\n\nAchten Sie auf die 3-Ton-Gruppierungen! \n\n<Rechte Taste> = 3-Ton-Gruppen steigen in sich\n<Linke Taste> = 3-Ton-Gruppen fallen in sich.\n\n',
    text=u'You are now well prepared to start the actual experiment! If something is unclear, ask your test director now. \n\nPlease try to answer as fast and as correctly as possible! \n\nConcentrate on the Triplets!\n\nRight key = Triplets are rising \nLeft Key = Triplets are falling. \n\n',
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

# Initialize components for Routine "Isi"
IsiClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "Trails_L"
Trails_LClock = core.Clock()
Listen_L = visual.TextStim(win=win, name='Listen_L',
    #text='Achtung!',
    text='Attention!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
local_sound = sound.Sound('A', secs=-1)
local_sound.setVolume(1)
ISI_L = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_L')

# Initialize components for Routine "Trials_Pause"
Trials_PauseClock = core.Clock()
head_globreal_2 = visual.TextStim(win=win, name='head_globreal_2',
    #text='Kurze Pause',
    text='Short break',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_globreal_2 = visual.TextStim(win=win, name='main_globreal_2',
    #text=u'Dr\xfccken Sie die grüne Taste um mit dem Experiment fortzuf\xfchren!',
    text=u'Press the green key when you are ready to continue the experiment!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "globinstr"
globinstrClock = core.Clock()
head_globinstr = visual.TextStim(win=win, name='head_globinstr',
    #text='Melodie als Ganzes!',
    text='Melody as a whole!',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_globinstr = visual.TextStim(win=win, name='main_globinstr',
    #text=u'Bitte konzentrieren Sie sich nun auf die Melodie als Ganzes!\nBitte geben Sie so schnell und korrekt wie m\xf6glich an, ob die Melodie als Ganzes \n\n- steigt, indem Sie die rechte Taste auf der Tastatur dr\xfccken, \n- oder f\xe4llt, indem Sie die linke Taste dr\xfccken.\n\n\n\nEs folgt nun eine kurze \xdcbung!\n',
    text=u'Please concentrate on the melody as a whole! \nPlease answer correctly and as fast as possible whether the melody as a whole is \n\n- rising by pressing the right key on your console, \n- or falling by pressing the left key on your console. \n\n\n\nThere will be a short practice session now!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_globinstr = visual.TextStim(win=win, name='foot_globinstr',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "instr_practiceG"
instr_practiceGClock = core.Clock()
head_practiceglob = visual.TextStim(win=win, name='head_practiceglob',
    #text=u'\xdcbung!',
    text='Practice session!',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_practiceglob = visual.TextStim(win=win, name='main_practiceglob',
    #text=u'Konzentrieren Sie sich auf die Melodie als Ganzes!\n\n<Rechte Taste> = Melodie steigt, \n<Linke Taste> = Melodie f\xe4llt\n\nVersuchen Sie keine Fehler zu machen und so schnell wie m\xf6glich zu reagieren!\n\n\n\n',
    text=u'Please concentrate on the melody as a whole! \n\n<Right Key> = Melody is rising, \n<Left Key> = Melody is falling\n\nTry to avoid mistakes and react as fast as possible!\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_practiceglob = visual.TextStim(win=win, name='foot_practiceglob',
    #text='Weiter mit der grünen Taste!',
    text='Press the green key to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Isi"
IsiClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "Trials_G"
Trials_GClock = core.Clock()
Listen_G = visual.TextStim(win=win, name='Listen_G',
    #text='Achtung!',
    text='Attention!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI_G = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_G')
sound_global = sound.Sound('A', secs=-1)
sound_global.setVolume(1)

# Initialize components for Routine "feedbackG"
feedbackGClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
head_feedbackG = visual.TextStim(win=win, name='head_feedbackG',
    #text=u'\xdcbung beendet!',
    text=u'Practice session completed!',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
main_feedbackG = visual.TextStim(win=win, name='main_feedbackG',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
foot_feedbackG = visual.TextStim(win=win, name='foot_feedbackG',
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
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_globreal = visual.TextStim(win=win, name='main_globreal',
    #text=u'Sie sind nun gut vorbereitet, um mit dem Experiment zu beginnen! Wenn etwas unklar ist, fragen Sie bitte jetzt den/die Versuchsleiter/-in.\n\nBitte versuchen Sie so schnell und korrekt wie m\xf6glich zu antworten!\n\nAchten Sie auf die Melodie als Ganzes!\n\nRechte Taste = Melodie als Ganzes steigt \nLinke Taste = Melodie als Ganzes f\xe4llt.\n\n',
    text=u'You are now well prepared to start the actual experiment! If something is unclear, ask your test director now. \n\nPlease try to answer as fast and as correctly as possible! \n\nConcentrate on the melody as a whole!\n\nRight key = Melody as a whole is rising \nLeft Key = Melody as a whole is falling. \n\n',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
foot_globreal = visual.TextStim(win=win, name='foot_globreal',
    #text=u'Dr\xfccken Sie die grüne Taste um mit dem Experiment zu beginnen!',
    text=u'Press the green key to start the experiment!',
    font='Arial',
    pos=(0, -0.9), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Isi"
IsiClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "Trials_G"
Trials_GClock = core.Clock()
Listen_G = visual.TextStim(win=win, name='Listen_G',
    #text='Achtung!',
    text='Attention!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI_G = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_G')
sound_global = sound.Sound('A', secs=-1)
sound_global.setVolume(1)

# Initialize components for Routine "Trials_Pause"
Trials_PauseClock = core.Clock()
head_globreal_2 = visual.TextStim(win=win, name='head_globreal_2',
    #text='Kurze Pause',
    text='Short break',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
main_globreal_2 = visual.TextStim(win=win, name='main_globreal_2',
    #text=u'Dr\xfccken Sie die grüne Taste um mit dem Experiment fortzuf\xfchren!',
    text=u'Press the green key when you are ready to continue the experiment!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "end_question"
end_questionClock = core.Clock()
main_quest = visual.TextStim(win=win, name='main_quest',
    #text=u'Sie haben nun beide Bedingungen erfolgreich beendet!\n\nEs folgen nun noch wenige abschlie\xdfende Fragen\n\nVerwenden Sie dafür die PC-Maus unter dem Tisch.',
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
    #text=u'Wie schwierig fanden Sie das Experiment grunds\xe4tzlich? (0 = sehr einfach; 1= sehr schwierig)',
    text=u'How difficult was the experiment for you in general? (0 =  very easy; 1 = very difficult)',
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating1 = visual.RatingScale(win=win, name='rating1', marker='triangle', size=1, pos=[0.0, -0.2], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "question2"
question2Clock = core.Clock()
main_question2 = visual.TextStim(win=win, name='main_question2',
    #text='Wie schwierig fanden Sie es, sich auf die Melodie als Ganzes zu konzentrieren? (0 = sehr einfach; 1= sehr schwierig)',
    text='How difficult was it for you to concentrate on the melody as a whole? (0 = very easy; 1 = very difficult)',
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=1, pos=[0.0, -0.2], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "question3"
question3Clock = core.Clock()
main_question3 = visual.TextStim(win=win, name='main_question3',
    #text='Wie schwierig fanden Sie es, sich auf die 3-Ton-Gruppierungen zu konzentrieren? (0 = sehr einfach; 1= sehr schwierig)',
    text='How difficult was it for you to concentrate on the triplets? (0 = very easy; 1 = very difficult)',
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating3 = visual.RatingScale(win=win, name='rating3', marker='triangle', size=1, pos=[0.0, -0.2], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "question4"
question4Clock = core.Clock()
main_question4 = visual.TextStim(win=win, name='main_question4',
    #text=u'Manchmal waren Melodien im Experiment inkongruent, d.h. die Melodie steigt auf der 9-Ton-Ebene aber die 3 Ton-Gruppen fallen, oder umgekehrt. \nFanden Sie es grunds\xe4tzlich schwieriger, sich auf die Melodie als Ganzes (=0), oder die 3-Ton-Melodien (=1) zu konzentrieren? \n(Mitte= beide Bedingungen waren f\xfcr mich gleich schwierig)',
    text=u'Some melodies in this experiment were incongruent, which means that the melody as a whole was rising but the triplets themselves were falling, or the other way around. \nWas it generally more difficult for you to concentrate on the melodies as a whole (= 0), or to concentrate on the triplets (=1)? \n(Middle = both conditions were equally difficult to me)', 
    font='Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rating4 = visual.RatingScale(win=win, name='rating4', marker='triangle', size=1, pos=[0.0, -0.2], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')

# Initialize components for Routine "feedback_final"
feedback_finalClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
head_feedback_final = visual.TextStim(win=win, name='head_feedback_final',
    text='Feedback!',
    font='Comic Sans',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
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
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
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
geninstrComponents = [main_geninstr, foot_geninstr, key_read1, melodiesGL, head_geninstr]
for thisComponent in geninstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "geninstr"-------
while continueRoutine:
    # get current time
    t = geninstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
				continueRoutine = False
		
		
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *melodiesGL* updates
    if t >= 0.0 and melodiesGL.status == NOT_STARTED:
        # keep track of start time/frame for later
        melodiesGL.tStart = t
        melodiesGL.frameNStart = frameN  # exact frame index
        melodiesGL.setAutoDraw(True)
    
    # *head_geninstr* updates
    if t >= 0.0 and head_geninstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        head_geninstr.tStart = t
        head_geninstr.frameNStart = frameN  # exact frame index
        head_geninstr.setAutoDraw(True)
    
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

# set up handler to look after randomisation of conditions etc
examples = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Paradigms/auditory global local/examples_eng.csv'),
    seed=None, name='examples')
thisExp.addLoop(examples)  # add the loop to the experiment
thisExample = examples.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExample.rgb)
if thisExample != None:
    for paramName in thisExample.keys():
        exec(paramName + '= thisExample.' + paramName)

for thisExample in examples:
    currentLoop = examples
    # abbreviate parameter names if possible (e.g. rgb = thisExample.rgb)
    if thisExample != None:
        for paramName in thisExample.keys():
            exec(paramName + '= thisExample.' + paramName)
    
    # ------Prepare to start Routine "example_2"-------
    t = 0
    example_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    textloop.setText(text)
    sound_1.setSound(GL_fileName, secs=-1)
    image.setImage(bild)
    # keep track of which components have finished
    example_2Components = [example, textloop, sound_1, image]
    for thisComponent in example_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "example_2"-------
    while continueRoutine:
        # get current time
        t = example_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *example* updates
        if t >= 0.0 and example.status == NOT_STARTED:
            # keep track of start time/frame for later
            example.tStart = t
            example.frameNStart = frameN  # exact frame index
            example.setAutoDraw(True)
        if example.status == STARTED and bool(sound_1.status==FINISHED):
            example.setAutoDraw(False)
        
        # *textloop* updates
        if t >= 0.0 and textloop.status == NOT_STARTED:
            # keep track of start time/frame for later
            textloop.tStart = t
            textloop.frameNStart = frameN  # exact frame index
            textloop.setAutoDraw(True)
        if textloop.status == STARTED and bool(sound_1.status==FINISHED):
            textloop.setAutoDraw(False)
        # start/stop sound_1
        if t >= 5 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and bool(sound_1.status==FINISHED):
            image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in example_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "example_2"-------
    for thisComponent in example_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # the Routine "example_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'examples'

# get names of stimulus parameters
if examples.trialList in ([], [None], None):
    params = []
else:
    params = examples.trialList[0].keys()
# save data for this loop
examples.saveAsText(filename + 'examples.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
    key_read2 = event.BuilderKeyResponse()#

    ButtonBox.con.flush_input()
    ButtonBox.clear_response_queue()

    # keep track of which components have finished
    locinstrComponents = [head_locinstr, main_locinstr, foot_locinstr, key_read2]
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
            #main_locinstr.setText(u'Bitte konzentrieren Sie sich nun auf die 3-Ton-Gruppierungen der Melodien! \nBitte geben Sie so schnell und korrekt wie m\xf6glich an, ob die 3-Ton-Gruppierungen in sich \n\n- steigen, indem Sie die rechte Taste auf der Tastatur dr\xfccken, \n- oder fallen, indem Sie die linke Taste dr\xfccken. \nDr\xfccken Sie die Taste so schnell wie m\xf6glich, d.h. sobald Sie sich sicher sind. SIe brauchen nicht warten, bis die Melodie zu Ende gespielt ist. \n\n\n\nEs folgt nun eine kurze \xdcbung!\n', log=False)
            main_locinstr.setText(u'Please concentrate on the Triplets! \nPlease answer correctly and as fast as possible whether the triplets are \n\n- rising by pressing the right key on your console, \n- or falling by pressing the left key on your console. \nPlease press the key as fast as possible, as soon as you are sure about your answer. You do not have to wait until the melody is over. \n\n\n\nThere will be a short practice session now!\n', log=False)

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
    
    # ------Prepare to start Routine "instr_practiceL"-------
    t = 0
    instr_practiceLClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_read3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instr_practiceLComponents = [head_practiceloc, main_practiceloc, foot_practiceloc, key_read3]
    for thisComponent in instr_practiceLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr_practiceL"-------
    while continueRoutine:
        # get current time
        t = instr_practiceLClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *head_practiceloc* updates
        if t >= 0.0 and head_practiceloc.status == NOT_STARTED:
            # keep track of start time/frame for later
            head_practiceloc.tStart = t
            head_practiceloc.frameNStart = frameN  # exact frame index
            head_practiceloc.setAutoDraw(True)
        
        # *main_practiceloc* updates
        if t >= 0.0 and main_practiceloc.status == NOT_STARTED:
            # keep track of start time/frame for later
            main_practiceloc.tStart = t
            main_practiceloc.frameNStart = frameN  # exact frame index
            main_practiceloc.setAutoDraw(True)
        
        # *foot_practiceloc* updates
        if t >= 0.0 and foot_practiceloc.status == NOT_STARTED:
            # keep track of start time/frame for later
            foot_practiceloc.tStart = t
            foot_practiceloc.frameNStart = frameN  # exact frame index
            foot_practiceloc.setAutoDraw(True)
        
        # *key_read3* updates
        if t >= 0.0 and key_read3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_read3.tStart = t
            key_read3.frameNStart = frameN  # exact frame index
            key_read3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_read3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            ButtonBox.poll_for_response()
            if ButtonBox.response_queue_size() > 0:
                response = ButtonBox.get_next_response()
                if response['pressed'] == True:
                    if response['key'] == 7:
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
        for thisComponent in instr_practiceLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_practiceL"-------
    for thisComponent in instr_practiceLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr_practiceL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Isi"-------
    t = 0
    IsiClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    IsiComponents = [ISI]
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IsiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IsiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Isi"-------
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    practice_local = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Paradigms/auditory global local/conditions_local_train.csv'),
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
        
        # ------Prepare to start Routine "Trails_L"-------
        t = 0
        Trails_LClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        nextRound = False
        # update component parameters for each repeat
        local_sound.setSound(GL_fileName, secs=-1)
        KeyL = event.BuilderKeyResponse()
        # keep track of which components have finished
        Trails_LComponents = [Listen_L, local_sound, KeyL, ISI_L]
        for thisComponent in Trails_LComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trails_L"-------
        while continueRoutine:
            # get current time
            t = Trails_LClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Listen_L* updates
            if t >= 1.0 and Listen_L.status == NOT_STARTED:
                # keep track of start time/frame for later
                Listen_L.tStart = t
                Listen_L.frameNStart = frameN  # exact frame index
                Listen_L.setAutoDraw(True)
            frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Listen_L.status == STARTED and t >= frameRemains:
                Listen_L.setAutoDraw(False)
            # start/stop local_sound
            if t >= 2.0 and local_sound.status == NOT_STARTED:
                # keep track of start time/frame for later
                local_sound.tStart = t
                local_sound.frameNStart = frameN  # exact frame index
                local_sound.play()  # start the sound (it finishes automatically)
            
            # *KeyL* updates
            if t >= 1.0 and KeyL.status == NOT_STARTED:
                # keep track of start time/frame for later
                KeyL.tStart = t
                KeyL.frameNStart = frameN  # exact frame index
                KeyL.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(KeyL.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
				#Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
            	ButtonBox.con.flush_input()
                ButtonBox.clear_response_queue()

				
            if t >= 6.0 and KeyL.status == STARTED:
                KeyL.status = STOPPED
            if KeyL.status == STARTED:
                theseKeys = event.getKeys(keyList=['up', 'down'])

                ButtonBox.poll_for_response()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if ButtonBox.response_queue_size() > 0: # at least one key was pressed
                    if KeyL.keys == []:  # then this was the first keypress
                        response = ButtonBox.get_next_response()

                        if response['pressed'] == True:
                            translated= 'y' #random wrong character for the case another button gets pressed
                            if response['key'] == 3:
                                translated = 'up'
                            if response['key'] == 2:
                                translated = 'down'
                            KeyL.keys = translated # just the first key pressed
                            KeyL.rt = KeyL.clock.getTime()
                            # was this 'correct'?
                            if (KeyL.keys == str(corrAns)) or (KeyL.keys == corrAns):
                                KeyL.corr = 1
                                #global totalCorrect_local #bzw. totalcorrect_global
                                #totalCorrect_local += 1
                                #print "CORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                            else:
                                KeyL.corr = 0
                                #print "INCORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                            nextRound = True


            # *ISI_L* period
            if t >= 0 and ISI_L.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_L.tStart = t
                ISI_L.frameNStart = frameN  # exact frame index
                ISI_L.start(1.0)
            elif ISI_L.status == STARTED:  # one frame should pass before updating params and completing
                ISI_L.complete()  # finish the static period
            
            # check if all components have finished
            if nextRound == True:  # a component has requested a forced-end of Routine
                if local_sound.status == STOPPED:
                    nextRound = False
                    break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trails_LComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trails_L"-------
        for thisComponent in Trails_LComponents:
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
        # the Routine "Trails_L" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
    
    # ------Prepare to start Routine "feedbackL"-------
    t = 0
    feedbackLClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    nCorr = practice_local.data['KeyL.corr'].sum() #.std(), .mean() also available
    meanRt = practice_local.data['KeyL.rt'].mean()
    #msg = "Sie haben %i trials richtig beantwortet \n (reaction time=%.2f s)" %(nCorr,meanRt)
    msg = "You have answered %i trials correctly \n (reaction time=%.2f s)" %(nCorr,meanRt)
    main_feedbackL.setText(msg)
    key_read4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    feedbackLComponents = [head_feedbackL, main_feedbackL, foot_feedbackL, key_read4]
    for thisComponent in feedbackLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedbackL"-------
    while continueRoutine:
        # get current time
        t = feedbackLClock.getTime()
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
        
        # *foot_feedbackL* updates
        if t >= 0.0 and foot_feedbackL.status == NOT_STARTED:
            # keep track of start time/frame for later
            foot_feedbackL.tStart = t
            foot_feedbackL.frameNStart = frameN  # exact frame index
            foot_feedbackL.setAutoDraw(True)
        
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
        for thisComponent in feedbackLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackL"-------
    for thisComponent in feedbackLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "feedbackL" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Isi"-------
    t = 0
    IsiClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    IsiComponents = [ISI]
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IsiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IsiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Isi"-------
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    batch_local = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='batch_local')
    thisExp.addLoop(batch_local)  # add the loop to the experiment
    thisBatch_local = batch_local.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBatch_local.rgb)
    if thisBatch_local != None:
        for paramName in thisBatch_local.keys():
            exec(paramName + '= thisBatch_local.' + paramName)
    
    for thisBatch_local in batch_local:
        currentLoop = batch_local
        # abbreviate parameter names if possible (e.g. rgb = thisBatch_local.rgb)
        if thisBatch_local != None:
            for paramName in thisBatch_local.keys():
                exec(paramName + '= thisBatch_local.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        exp_local = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Paradigms/auditory global local/conditions_local_test.csv'),
            seed=None, name='exp_local')
        thisExp.addLoop(exp_local)  # add the loop to the experiment
        thisExp_local = exp_local.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExp_local.rgb)
        if thisExp_local != None:
            for paramName in thisExp_local.keys():
                exec(paramName + '= thisExp_local.' + paramName)
        
        for thisExp_local in exp_local:
            currentLoop = exp_local
            # abbreviate parameter names if possible (e.g. rgb = thisExp_local.rgb)
            if thisExp_local != None:
                for paramName in thisExp_local.keys():
                    exec(paramName + '= thisExp_local.' + paramName)
            
            # ------Prepare to start Routine "Trails_L"-------
            t = 0
            Trails_LClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            nextRound = True
            # update component parameters for each repeat
            local_sound.setSound(GL_fileName, secs=-1)
            KeyL = event.BuilderKeyResponse()
            # keep track of which components have finished
            Trails_LComponents = [Listen_L, local_sound, KeyL, ISI_L]
            for thisComponent in Trails_LComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Trails_L"-------
            while continueRoutine:
                # get current time
                t = Trails_LClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Listen_L* updates
                if t >= 1.0 and Listen_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Listen_L.tStart = t
                    Listen_L.frameNStart = frameN  # exact frame index
                    Listen_L.setAutoDraw(True)
                frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Listen_L.status == STARTED and t >= frameRemains:
                    Listen_L.setAutoDraw(False)
                # start/stop local_sound
                if t >= 2.0 and local_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    local_sound.tStart = t
                    local_sound.frameNStart = frameN  # exact frame index
                    local_sound.play()  # start the sound (it finishes automatically)
                
                # *KeyL* updates
                if t >= 1.0 and KeyL.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    KeyL.tStart = t
                    KeyL.frameNStart = frameN  # exact frame index
                    KeyL.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(KeyL.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
					#Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()
                    ButtonBox.clear_response_queue()
					
                if t >= 6.0 and KeyL.status == STARTED:
                    KeyL.status = STOPPED
                if KeyL.status == STARTED:
                    theseKeys = event.getKeys(keyList=['up', 'down'])

                    ButtonBox.poll_for_response()
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0: # at least one key was pressed
                        if KeyL.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'up'
                                if response['key'] == 2:
                                    translated = 'down'
                                KeyL.keys = translated # just the first key pressed
                                KeyL.rt = KeyL.clock.getTime()
                                # was this 'correct'?
                                if (KeyL.keys == str(corrAns)) or (KeyL.keys == corrAns):
                                    KeyL.corr = 1
                                    totalCorrect_local #bzw. totalcorrect_global
                                    totalCorrect_local += 1
                                    #print "CORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    KeyL.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(KeyL.keys) + " y la respuesta era" + repr(corrAns) + "."
                                nextRound = True
                # *ISI_L* period
                if t >= 0 and ISI_L.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_L.tStart = t
                    ISI_L.frameNStart = frameN  # exact frame index
                    ISI_L.start(1.0)
                elif ISI_L.status == STARTED:  # one frame should pass before updating params and completing
                    ISI_L.complete()  # finish the static period
                
                # check if all components have finished
                if nextRound == True:  # a component has requested a forced-end of Routine
                    if local_sound.status == STOPPED:
                        nextRound = False
                        break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trails_LComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trails_L"-------
            for thisComponent in Trails_LComponents:
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
            # store data for exp_local (TrialHandler)
            exp_local.addData('KeyL.keys',KeyL.keys)
            exp_local.addData('KeyL.corr', KeyL.corr)
            if KeyL.keys != None:  # we had a response
                exp_local.addData('KeyL.rt', KeyL.rt)
            # the Routine "Trails_L" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'exp_local'
        
        # get names of stimulus parameters
        if exp_local.trialList in ([], [None], None):
            params = []
        else:
            params = exp_local.trialList[0].keys()
        # save data for this loop
        exp_local.saveAsText(filename + 'exp_local.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "Trials_Pause"-------
        t = 0
        Trials_PauseClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_read9_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        Trials_PauseComponents = [head_globreal_2, main_globreal_2, key_read9_2]
        for thisComponent in Trials_PauseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trials_Pause"-------
        while continueRoutine:
            # get current time
            t = Trials_PauseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_globreal_2* updates
            if t >= 0.0 and head_globreal_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_globreal_2.tStart = t
                head_globreal_2.frameNStart = frameN  # exact frame index
                head_globreal_2.setAutoDraw(True)
            
            # *main_globreal_2* updates
            if t >= 0.0 and main_globreal_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_globreal_2.tStart = t
                main_globreal_2.frameNStart = frameN  # exact frame index
                main_globreal_2.setAutoDraw(True)
            
            # *key_read9_2* updates
            if t >= 0.0 and key_read9_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read9_2.tStart = t
                key_read9_2.frameNStart = frameN  # exact frame index
                key_read9_2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read9_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
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
            for thisComponent in Trials_PauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trials_Pause"-------
        for thisComponent in Trials_PauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Trials_Pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'batch_local'
    
    # get names of stimulus parameters
    if batch_local.trialList in ([], [None], None):
        params = []
    else:
        params = batch_local.trialList[0].keys()
    # save data for this loop
    batch_local.saveAsText(filename + 'batch_local.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'local_Block'

# get names of stimulus parameters
if local_Block.trialList in ([], [None], None):
    params = []
else:
    params = local_Block.trialList[0].keys()
# save data for this loop
local_Block.saveAsText(filename + 'local_Block.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
    globinstrComponents = [head_globinstr, main_globinstr, foot_globinstr, key_read6]
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
    
    # ------Prepare to start Routine "instr_practiceG"-------
    t = 0
    instr_practiceGClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_read7 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instr_practiceGComponents = [head_practiceglob, main_practiceglob, foot_practiceglob, key_read7]
    for thisComponent in instr_practiceGComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr_practiceG"-------
    while continueRoutine:
        # get current time
        t = instr_practiceGClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *head_practiceglob* updates
        if t >= 0.0 and head_practiceglob.status == NOT_STARTED:
            # keep track of start time/frame for later
            head_practiceglob.tStart = t
            head_practiceglob.frameNStart = frameN  # exact frame index
            head_practiceglob.setAutoDraw(True)
        
        # *main_practiceglob* updates
        if t >= 0.0 and main_practiceglob.status == NOT_STARTED:
            # keep track of start time/frame for later
            main_practiceglob.tStart = t
            main_practiceglob.frameNStart = frameN  # exact frame index
            main_practiceglob.setAutoDraw(True)
        
        # *foot_practiceglob* updates
        if t >= 0.0 and foot_practiceglob.status == NOT_STARTED:
            # keep track of start time/frame for later
            foot_practiceglob.tStart = t
            foot_practiceglob.frameNStart = frameN  # exact frame index
            foot_practiceglob.setAutoDraw(True)
        
        # *key_read7* updates
        if t >= 0.0 and key_read7.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_read7.tStart = t
            key_read7.frameNStart = frameN  # exact frame index
            key_read7.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_read7.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            ButtonBox.poll_for_response()
            if ButtonBox.response_queue_size() > 0:
                response = ButtonBox.get_next_response()
                if response['pressed'] == True:
                    if response['key'] == 7:
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
        for thisComponent in instr_practiceGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_practiceG"-------
    for thisComponent in instr_practiceGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr_practiceG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Isi"-------
    t = 0
    IsiClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    IsiComponents = [ISI]
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IsiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IsiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Isi"-------
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    practice_global = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Paradigms/auditory global local/conditions_global_train.csv'),
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
        nextRound = False
        # update component parameters for each repeat
        sound_global.setSound(GL_fileName, secs=-1)
        keyG = event.BuilderKeyResponse()
        # keep track of which components have finished
        Trials_GComponents = [Listen_G, ISI_G, sound_global, keyG]
        for thisComponent in Trials_GComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trials_G"-------
        while continueRoutine:
            # get current time
            t = Trials_GClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Listen_G* updates
            if t >= 1.0 and Listen_G.status == NOT_STARTED:
                # keep track of start time/frame for later
                Listen_G.tStart = t
                Listen_G.frameNStart = frameN  # exact frame index
                Listen_G.setAutoDraw(True)
            frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Listen_G.status == STARTED and t >= frameRemains:
                Listen_G.setAutoDraw(False)
            # start/stop sound_global
            if t >= 2.0 and sound_global.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_global.tStart = t
                sound_global.frameNStart = frameN  # exact frame index
                sound_global.play()  # start the sound (it finishes automatically)
            
            # *keyG* updates
            if t >= 1.0 and keyG.status == NOT_STARTED:
                # keep track of start time/frame for later
                keyG.tStart = t
                keyG.frameNStart = frameN  # exact frame index
                keyG.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(keyG.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
				#Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
            	ButtonBox.con.flush_input()
                ButtonBox.clear_response_queue()
				
            if t >= 6.0 and keyG.status == STARTED:
                keyG.status = STOPPED
            if keyG.status == STARTED:
                theseKeys = event.getKeys(keyList=['up', 'down'])

                ButtonBox.poll_for_response()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if ButtonBox.response_queue_size() > 0: # at least one key was pressed
                    if keyG.keys == []:  # then this was the first keypress
                        response = ButtonBox.get_next_response()

                        if response['pressed'] == True:
                            translated= 'y' #random wrong character for the case another button gets pressed
                            if response['key'] == 3:
                                translated = 'up'
                            if response['key'] == 2:
                                translated = 'down'
                            keyG.keys = translated # just the first key pressed
                            keyG.rt = keyG.clock.getTime()
                            # was this 'correct'?
                            if (keyG.keys == str(corrAns)) or (keyG.keys == corrAns):
                                keyG.corr = 1
                                #global totalCorrect_global #bzw. totalcorrect_global
                                #totalCorrect_global += 1
                                #print "CORRECTO: Ha apretado " + repr(keyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                            else:
                                keyG.corr = 0
                                #print "INCORRECTO: Ha apretado " + repr(keyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                            nextRound = True

            # *ISI_G* period
            if t >= 0 and ISI_G.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_G.tStart = t
                ISI_G.frameNStart = frameN  # exact frame index
                ISI_G.start(1.0)
            elif ISI_G.status == STARTED:  # one frame should pass before updating params and completing
                ISI_G.complete()  # finish the static period
            
            # check if all components have finished
            if nextRound == True:  # a component has requested a forced-end of routine
                if sound_global.status == STOPPED:
                    nextRound = False
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
        sound_global.stop()  # ensure sound has stopped at end of routine
        # check responses
        if keyG.keys in ['', [], None]:  # No response was made
            keyG.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               keyG.corr = 1  # correct non-response
            else:
               keyG.corr = 0  # failed to respond (incorrectly)
        # store data for practice_global (TrialHandler)
        practice_global.addData('keyG.keys',keyG.keys)
        practice_global.addData('keyG.corr', keyG.corr)
        if keyG.keys != None:  # we had a response
            practice_global.addData('keyG.rt', keyG.rt)
        # the Routine "Trials_G" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
    
    # ------Prepare to start Routine "feedbackG"-------
    t = 0
    feedbackGClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    nCorr = practice_global.data['keyG.corr'].sum() #.std(), .mean() also available
    meanRt = practice_global.data['keyG.rt'].mean()
    #msg = "Sie haben %i trials richtig beantwortet \n (reaction time=%.2f s)" %(nCorr,meanRt)
    msg = "You have answered %i trials correctly \n (reaction time =%.2f s)" %(nCorr,meanRt)
    main_feedbackG.setText(msg)
    key_read8 = event.BuilderKeyResponse()
    # keep track of which components have finished
    feedbackGComponents = [head_feedbackG, main_feedbackG, foot_feedbackG, key_read8]
    for thisComponent in feedbackGComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedbackG"-------
    while continueRoutine:
        # get current time
        t = feedbackGClock.getTime()
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
        
        # *foot_feedbackG* updates
        if t >= 0.0 and foot_feedbackG.status == NOT_STARTED:
            # keep track of start time/frame for later
            foot_feedbackG.tStart = t
            foot_feedbackG.frameNStart = frameN  # exact frame index
            foot_feedbackG.setAutoDraw(True)
        
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
        for thisComponent in feedbackGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackG"-------
    for thisComponent in feedbackGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "feedbackG" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Isi"-------
    t = 0
    IsiClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    IsiComponents = [ISI]
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IsiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IsiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Isi"-------
    for thisComponent in IsiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    batch_global = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='batch_global')
    thisExp.addLoop(batch_global)  # add the loop to the experiment
    thisBatch_global = batch_global.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBatch_global.rgb)
    if thisBatch_global != None:
        for paramName in thisBatch_global.keys():
            exec(paramName + '= thisBatch_global.' + paramName)
    
    for thisBatch_global in batch_global:
        currentLoop = batch_global
        # abbreviate parameter names if possible (e.g. rgb = thisBatch_global.rgb)
        if thisBatch_global != None:
            for paramName in thisBatch_global.keys():
                exec(paramName + '= thisBatch_global.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        exp_global = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Paradigms/auditory global local/conditions_global_test.csv'),
            seed=None, name='exp_global')
        thisExp.addLoop(exp_global)  # add the loop to the experiment
        thisExp_global = exp_global.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExp_global.rgb)
        if thisExp_global != None:
            for paramName in thisExp_global.keys():
                exec(paramName + '= thisExp_global.' + paramName)
        
        for thisExp_global in exp_global:
            currentLoop = exp_global
            # abbreviate parameter names if possible (e.g. rgb = thisExp_global.rgb)
            if thisExp_global != None:
                for paramName in thisExp_global.keys():
                    exec(paramName + '= thisExp_global.' + paramName)
            
            # ------Prepare to start Routine "Trials_G"-------
            t = 0
            Trials_GClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            nextRound = False
            # update component parameters for each repeat
            sound_global.setSound(GL_fileName, secs=-1)
            keyG = event.BuilderKeyResponse()
            # keep track of which components have finished
            Trials_GComponents = [Listen_G, ISI_G, sound_global, keyG]
            for thisComponent in Trials_GComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Trials_G"-------
            while continueRoutine:
                # get current time
                t = Trials_GClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Listen_G* updates
                if t >= 1.0 and Listen_G.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Listen_G.tStart = t
                    Listen_G.frameNStart = frameN  # exact frame index
                    Listen_G.setAutoDraw(True)
                frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if Listen_G.status == STARTED and t >= frameRemains:
                    Listen_G.setAutoDraw(False)
                # start/stop sound_global
                if t >= 2.0 and sound_global.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    sound_global.tStart = t
                    sound_global.frameNStart = frameN  # exact frame index
                    sound_global.play()  # start the sound (it finishes automatically)
                
                # *keyG* updates
                if t >= 1.0 and keyG.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    keyG.tStart = t
                    keyG.frameNStart = frameN  # exact frame index
                    keyG.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(keyG.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
					#Clear ButtonBox Device queue (to correct excessive or out-of-time pressings)
                    ButtonBox.con.flush_input()
                    ButtonBox.clear_response_queue()
				
                if t >= 6.0 and keyG.status == STARTED :
                    keyG.status = STOPPED
                if keyG.status == STARTED:
                    theseKeys = event.getKeys(keyList=['up', 'down'])

                    ButtonBox.poll_for_response()
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if ButtonBox.response_queue_size() > 0: # at least one key was pressed
                        if keyG.keys == []:  # then this was the first keypress
                            response = ButtonBox.get_next_response()

                            if response['pressed'] == True:
                                translated= 'y' #random wrong character for the case another button gets pressed
                                if response['key'] == 3:
                                    translated = 'up'
                                if response['key'] == 2:
                                    translated = 'down'
                                keyG.keys = translated # just the first key pressed
                                keyG.rt = keyG.clock.getTime()
                                # was this 'correct'?
                                if (keyG.keys == str(corrAns)) or (keyG.keys == corrAns):
                                    keyG.corr = 1
                                    totalCorrect_global #bzw. totalcorrect_global
                                    totalCorrect_global += 1
                                    #print "CORRECTO: Ha apretado " + repr(keyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                else:
                                    keyG.corr = 0
                                    #print "INCORRECTO: Ha apretado " + repr(keyG.keys) + " y la respuesta era" + repr(corrAns) + "."
                                nextRound = True

                # *ISI_G* period
                if t >= 0 and ISI_G.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI_G.tStart = t
                    ISI_G.frameNStart = frameN  # exact frame index
                    ISI_G.start(1.0)
                elif ISI_G.status == STARTED:  # one frame should pass before updating params and completing
                    ISI_G.complete()  # finish the static period
                
                # check if all components have finished
                if nextRound == True:  # a component has requested a forced-end of Routine
                    if sound_global.status == STOPPED:
                        nextRound = False
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
            sound_global.stop()  # ensure sound has stopped at end of routine
            # check responses
            if keyG.keys in ['', [], None]:  # No response was made
                keyG.keys=None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   keyG.corr = 1  # correct non-response
                else:
                   keyG.corr = 0  # failed to respond (incorrectly)
            # store data for exp_global (TrialHandler)
            exp_global.addData('keyG.keys',keyG.keys)
            exp_global.addData('keyG.corr', keyG.corr)
            if keyG.keys != None:  # we had a response
                exp_global.addData('keyG.rt', keyG.rt)
            # the Routine "Trials_G" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'exp_global'
        
        # get names of stimulus parameters
        if exp_global.trialList in ([], [None], None):
            params = []
        else:
            params = exp_global.trialList[0].keys()
        # save data for this loop
        exp_global.saveAsText(filename + 'exp_global.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "Trials_Pause"-------
        t = 0
        Trials_PauseClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_read9_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        Trials_PauseComponents = [head_globreal_2, main_globreal_2, key_read9_2]
        for thisComponent in Trials_PauseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trials_Pause"-------
        while continueRoutine:
            # get current time
            t = Trials_PauseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *head_globreal_2* updates
            if t >= 0.0 and head_globreal_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                head_globreal_2.tStart = t
                head_globreal_2.frameNStart = frameN  # exact frame index
                head_globreal_2.setAutoDraw(True)
            
            # *main_globreal_2* updates
            if t >= 0.0 and main_globreal_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_globreal_2.tStart = t
                main_globreal_2.frameNStart = frameN  # exact frame index
                main_globreal_2.setAutoDraw(True)
            
            # *key_read9_2* updates
            if t >= 0.0 and key_read9_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_read9_2.tStart = t
                key_read9_2.frameNStart = frameN  # exact frame index
                key_read9_2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_read9_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                ButtonBox.poll_for_response()
                if ButtonBox.response_queue_size() > 0:
                    response = ButtonBox.get_next_response()
                    if response['pressed'] == True:
                        if response['key'] == 7:
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
            for thisComponent in Trials_PauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trials_Pause"-------
        for thisComponent in Trials_PauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Trials_Pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'batch_global'
    
    # get names of stimulus parameters
    if batch_global.trialList in ([], [None], None):
        params = []
    else:
        params = batch_global.trialList[0].keys()
    # save data for this loop
    batch_global.saveAsText(filename + 'batch_global.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'global_block'

# get names of stimulus parameters
if global_block.trialList in ([], [None], None):
    params = []
else:
    params = global_block.trialList[0].keys()
# save data for this loop
global_block.saveAsText(filename + 'global_block.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
#nCorr = exp_global.data['keyG.corr'].sum() #.std(), .mean() also available
#meanRt = exp_global.data['keyG.rt'].mean()
#msg = "Melody as a whole: You got %i trials correct \n (reaction time=%.2f s)" %(nCorr,meanRt)
#msg = "Melodie als ganzes: Sie haben %i Stimuli richtig beantwortet \n" %(totalCorrect_global)
msg = "Melody as a whole: You have answered %i trials correctly \n" %(totalCorrect_global)
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
#msg = "3-tone-groups: You got %i trials correct \n (reaction time =%.2f s)" %(nCorr,meanRt)
#msg = "3-Ton-Gruppen: Sie haben %i Stimuli richtig beantwortet \n" %(totalCorrect_local)
msg = "Triplets: You have answered %i trials correctly \n" %(totalCorrect_local)
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
