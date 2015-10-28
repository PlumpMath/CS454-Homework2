import __builtin__

""" Python Imports """
from hashlib import md5
from sys import exit
from time import strftime
import random, sys

""" Panda3D Imports """
from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import Texture
from panda3d.core import WindowProperties
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Sequence

class characterSelection(DirectObject):

	def __init__(self,world):
		self.world = world
		self.window = OnscreenImage(image = "Interface/login_window.png", pos = (0,0,0), scale = (2, 1, 2) )
		self.window.setTransparency(TransparencyAttrib.MAlpha)
		self.createSelectWindow()
	# def createLoginWindow(self):

	def createSelectWindow(self):
		print self.world.welcome, self.world.userList
		list = self.world.userList
		z = 0.40
		charlist =["Car","Ralph","Panda1","Panda2"]
		usedlist =[]
		
		bk_text = self.world.welcome
		textObject = OnscreenText(text = bk_text, pos = (-0.85,0.90),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Connected Players"
		textObject = OnscreenText(text = bk_text, pos = (0,0.75),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Player ID"
		textObject = OnscreenText(text = bk_text, pos = (-0.65,0.55),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Players Name"
		textObject = OnscreenText(text = bk_text, pos = (-0.05,0.55),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Players Charactor"
		textObject = OnscreenText(text = bk_text, pos = (0.65,0.55),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		for l in list :
			pl = l[1].split(",")
			usedlist.append(pl[1])
			charlist.remove(pl[1])
			textObject = OnscreenText(text = str(l[0]), pos = (-0.65,z),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
			textObject = OnscreenText(text = pl[0], pos = (-0.05,z),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
			textObject = OnscreenText(text = pl[1], pos = (0.65,z),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
			z= z - 0.2

		def itemSel(arg):
			output = "Item Selected is: "+arg
			textObject.setText(output)

		output = ""
		textObject = OnscreenText(text = output, pos = (0.95,-0.5),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		print "usedlist", usedlist
		print "charlist", charlist
		# Create a frame
		menu = DirectOptionMenu(text="options", scale=0.1,items=charlist,initialitem=2,highlightColor=(0.65,0.65,0.65,1),command=itemSel)

