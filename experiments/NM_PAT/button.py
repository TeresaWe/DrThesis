#!/usr/bin/env python2

'''Creates a buttonff of given width and height
as a special case of a :class:`~psychopy.visual.ShapeStim`'''

# Part of the PsychoPy library
# Copyright (C) 2014 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

import numpy as np
import random

import psychopy  # so we can get the __path__
from psychopy import logging
from psychopy.tools.attributetools import attributeSetter, logAttrib
from psychopy.visual.basevisual import BaseVisualStim
from psychopy.visual.helpers import setColor
from psychopy.visual.rect import Rect
from psychopy.visual.text import TextStim

from layout import GridLayout


class ButtonStyle:

    def __init__(self, fillColor='Black', borderColor='White',
                 textColor='White'):
        self.fillColor = fillColor
        self.borderColor = borderColor
        self.textColor = textColor

    @attributeSetter
    def fillColor(self, color):
        """
        Sets the color of the button fill. See :meth:`psychopy.visual.GratingStim.color`
        for further details of how to use colors.
        """
        setColor(self, color, rgbAttrib='fillRGB', colorAttrib='fillColor')

    @attributeSetter
    def borderColor(self, color):
        """
        Sets the color of the button border. See :meth:`psychopy.visual.GratingStim.color`
        for further details of how to use colors.
        """
        setColor(self, color, rgbAttrib='borderRGB', colorAttrib='borderColor')

    @attributeSetter
    def textColor(self, color):
        """
        Sets the color of the button text. See :meth:`psychopy.visual.GratingStim.color`
        for further details of how to use colors.
        """
        setColor(self, color, rgbAttrib='textRGB', colorAttrib='textColor')


class Button(BaseVisualStim):

    """Creates a button of given width and height, by combining a
    TextStim and a Rect

    (New in version 1.80.99 FIXME)
    """

    def __init__(self, win,
                 text='Hello World',
                 pos=(0.0, 0.0),
                 width=None,
                 height=None,
                 padx=2,
                 pady=2,
                 units="",
                 checked=False,
                 name=None,
                 autoLog=None,
                 autoDraw=False,
                 ):
        """
        Button accepts all input parameters, that
        `~psychopy.visual.BaseVisualStim` accept, except for vertices
        and closeShape.

        :Parameters:

            width : int or float
                Width of the Rectangle (in its respective units, if specified)

            height : int or float
                Height of the Rectangle (in its respective units, if specified)

        """
        # what local vars are defined (these are the init params) for use by
        # __repr__
        self._initParams = dir()
        self._initParams.remove('self')

        super(Button, self).__init__(
            win, units=units, name=name, autoLog=False)

        self.__dict__['pos'] = pos
        self.__dict__['text'] = text

        self.textStim = TextStim(win, text=text, pos=self.pos, wrapWidth=width,
                                 color='Black', units=units, autoLog=autoLog)

        # TODO: expose content_width via TextStim
        autoWidth = (self.textStim._pygletTextObj._layout.content_width +
                     2 * padx)
        autoHeight = self.textStim.height + 2 * pady

        if width is not None and width > autoWidth:
            self.__dict__['width'] = width
        else:
            self.__dict__['width'] = autoWidth

        if height is not None and height > autoHeight:
            self.__dict__['height'] = height
        else:
            self.__dict__['height'] = autoHeight

        self.rectStim = Rect(
            win, pos=self.pos, width=self.width, height=self.height, units=units, autoLog=autoLog)

        self.normalStyle = ButtonStyle()
        self.checkedStyle = ButtonStyle(
            fillColor='#2E2EFE', borderColor='White', textColor='White')

        self.checked = checked  # this will set style

        self.autoDraw = autoDraw

        self.__dict__['autoLog'] = (autoLog or
                                    autoLog is None and self.win.autoLog)
        if self.autoLog:
            logging.exp("Created %s = %s" % (self.name, str(self)))

    def _setStyle(self, style):
        self.rectStim.lineColor = style.borderColor
        self.rectStim.fillColor = style.fillColor
        self.textStim.color = style.textColor

    @attributeSetter
    def text(self, value):
        """Changes the text of the Button"""
        self.__dict__['text'] = value
        # TODO: change this to attributeSetters with 1.80.99
        self.textStim.setText(value)

    @attributeSetter
    def pos(self, value):
        """Changes the position of the Button"""
        self.__dict__['pos'] = value
        self.rectStim.pos = value
        self.textStim.pos = value

    @attributeSetter
    def width(self, value):
        """Changes the width of the Button"""
        self.__dict__['width'] = value
        # TODO: change this to attributeSetters with 1.80.99
        self.rectStim.setWidth(value)
        # this won't work, need to construct new or wait for 1.80.99
        self.textStim.wrapWidth = value

    @attributeSetter
    def height(self, value):
        """Changes the height of the Button"""
        self.__dict__['height'] = value
        # TODO: change this to attributeSetters with 1.80.99
        self.rectStim.setHeight(value)

        # don't set height of text as it will change font size
        # self.textStim.setHeight(value)

    @attributeSetter
    def checked(self, value):
        self.__dict__['checked'] = value
        if self.checked:
            self._setStyle(self.checkedStyle)
        else:
            self._setStyle(self.normalStyle)

    def setColor(self, color, colorSpace=None, operation=''):
        """For Button use :meth:`~Button.fillColor` or
        :meth:`~Button.borderColor` or :meth:`~Button.textColor`
        """
        raise AttributeError('Button does not support setColor method.'
                             'Please use fillColor, borderColor, or textColor')

    def contains(self, x, y=None, units=None):
        return self.rectStim.contains(x, y, units)

    def draw(self, win=None):
        """
        Draw the stimulus in its relevant window. You must call
        this method after every MyWin.flip() if you want the
        stimulus to appear on that frame and then update the screen
        again.

        If win is specified then override the normal window of this stimulus.
        """
        if win is None:
            win = self.win

        self.rectStim.draw(win)
        self.textStim.draw(win)


class ButtonGrid(BaseVisualStim):

    def __init__(self, win, labels=[], pos=(0, 0), rows=1, cols=0, padx=3, pady=3,
                 vgap=10, hgap=10, exclusive=True, autoDraw=True):

        super(ButtonGrid, self).__init__(win, autoLog=False)

        self.labels = labels
        self.__dict__['pos'] = pos
        self.__dict__['exclusive'] = exclusive
        self.checked = []

        self.buttons = []
        self.layout = GridLayout(pos, rows, cols, vgap, hgap)
        for text in labels:
            btn = Button(win=win, text=text, padx=padx, pady=pady, width=100, height=100)
            self.buttons.append(btn)
            self.layout.add(btn)

        self._update()

        self.autoDraw = autoDraw

    def _update(self):
        self.layout.layout()
        self.width = self.layout.width
        self.height = self.layout.height

    def random(self):
	t = []	
	l = len(self.buttons)	
	for a in range(l):
		r = random.randint(0,len(self.buttons) - 1)
		t.append(self.buttons.pop(r))
	self.buttons = t
	self.layout = GridLayout((0,0), 0, 6, 10, 10)
	for btn in self.buttons:
		self.layout.add(btn)
	self._update()
		

    @attributeSetter
    def exclusive(self, value):

        if self.exclusive is True and value is False:
            # TODO: uncheck all but one
            raise NotImplementedError

        self.__dict__['exclusive'] = value

    @attributeSetter
    def pos(self, value):
        self.__dict__['pos'] = value
        self.layout.pos = self.pos
        self._update()

    def click(self, pos):
        clicked = [button for button in self.buttons if button.contains(pos)]
        assert len(clicked) <= 1
        if not clicked:
            return

        if self.exclusive:
            if clicked[0].checked:
                # do nothing, one button has to be checked
                # TODO: perhaps some cases where no response can be given?
                pass
            else:
                for btn in self.buttons:
                    if btn.checked:
                        btn.checked = False
                clicked[0].checked = True
        else:
            clicked[0].checked = not clicked[0].checked

    def checkedLabels(self):
        return [btn.text for btn in self.buttons if btn.checked]

    def reset(self):
        for btn in self.buttons:
            btn.checked = False

    def draw(self):
        for btn in self.buttons:
            btn.draw()
