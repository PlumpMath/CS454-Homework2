import direct.directbase.DirectStart
import random, sys, os, math, time

from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Sequence
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText 


from direct.gui.DirectGui import *
from panda3d.core import *

class Interface():
	def __init__(self):
		self.show_window()
		
	def show_window(self):
		self.window = OnscreenImage(image = "Interface/login_window.png", pos = (0,0,0), scale = (0.5, 1, 0.7) )
		self.window.setTransparency(TransparencyAttrib.MAlpha)

		#add button
		self.usernameButton = DirectEntry(text = "" ,scale=.05, pos = (-0.3, 0, 0.3),
		initialText="Username", numLines = 2,focusInCommand=self.clearText1)

		self.passwordButton = DirectEntry(text = "" ,scale=.05, pos = (-0.3, 0, 0.1),
		initialText="Password", numLines = 2,focusInCommand=self.clearText2)

		self.submitButton = DirectButton(image = "Interface/submit2.png", pos = (-0.05, 0, -0.2),scale = (0.2, 1, 0.07))
		self.submitButton.setTransparency(TransparencyAttrib.MAlpha)
	
	 
	#clear the text
	def clearText1(self):
		self.usernameButton.enterText('')
 
	def clearText2(self):
		self.passwordButton.enterText('')
 





