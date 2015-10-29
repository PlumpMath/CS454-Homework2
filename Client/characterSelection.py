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
from common.Constants import Constants
from panda3d.core import NodePath

class characterSelection(DirectObject):

	frame = DirectFrame()
	textObject = OnscreenText()

	def __init__(self,world):
		self.world = world
		# self.set1 = ModelSet("set1")
		# self.set1.reparentTo(self.render)
		frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
		frameSize=(-1, 1, -1, 1),#(Left,Right,Bottom,Top)
		pos=(-0.5, 0, 0.5))
		self.createSelectWindow()
	# def createLoginWindow(self):

	def ModelSet(name="set1"):
		return NodePath(name)

	def createSelectWindow(self):
		print self.world.welcome, self.world.userList
		list = self.world.userList
		self.user =self.world.welcome.split(" ")
		z = 0.40
		charlist =["Car","Ralph","Panda1","Panda2"]
		usedlist =[]
		self.SelectChar =""
		self.window = OnscreenImage(image = "Interface/login_window.png", pos = (0,0,0), scale = (2, 1, 2) )
		self.window.setTransparency(TransparencyAttrib.MAlpha)
		
		bk_text = self.world.welcome
		self.textObject = OnscreenText(text = bk_text, pos = (-0.85,0.90),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Connected Players"
		self.textObject = OnscreenText(text = bk_text, pos = (0,0.75),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Player ID"
		self.textObject = OnscreenText(text = bk_text, pos = (-0.65,0.55),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Players Name"
		self.textObject = OnscreenText(text = bk_text, pos = (-0.05,0.55),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		bk_text = "Players Charactor"
		self.textObject = OnscreenText(text = bk_text, pos = (0.65,0.55),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		for l in list :
			pl = l[1].split(",")
			usedlist.append(pl[1])
			charlist.remove(pl[1])
			self.textObject = OnscreenText(text = str(l[0]), pos = (-0.65,z),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
			self.textObject = OnscreenText(text = pl[0], pos = (-0.05,z),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
			self.textObject = OnscreenText(text = pl[1], pos = (0.65,z),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
			z= z - 0.2

		def itemSel(arg):
			output = "Item Selected is: "+arg
			self.textObject.setText(output)

		output = ""
		self.textObject = OnscreenText(text = output, pos = (0.95,-0.5),scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
		print "usedlist", usedlist
		print "charlist", charlist

		self.textObject = OnscreenText(text = "Select Charactor:", pos = (-0.90, -0.50), scale = 0.05,fg=(0,0,0.2,1),align=TextNode.ALeft,mayChange=0)
		# # Create a frame
		# menu = DirectOptionMenu(text="options", scale=0.1,items=charlist,initialitem=2,highlightColor=(0.65,0.65,0.65,1),command=itemSel)

		v = [0]
		# Add some text
		bk_text = "This is my Demo"
		self.textObject = OnscreenText(text = bk_text, pos = (0.95,-0.95),
		scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)

		# Callback function to set  text
		def setText(status=None):
			self.SelectChar = "%s"%v
			self.SelectChar=self.SelectChar[2:-2]
			print "You pressed Selected", self.SelectChar
			self.textObject.setText(bk_text)

		# Add button
		buttons = []
		pos = -0.3
		for i in charlist:
			print i
			buttons.append(DirectRadioButton(text = i, variable=v, value=[i], scale=0.05, pos=(pos,0,-0.5), command=setText))
			pos = pos + 0.3

		for button in buttons:
			button.setOthers(buttons)

		self.start = DirectButton(image = "Interface/submitBtn.png", command=self.clickedStart, pos = (0.8, 0, -0.7),scale = (0.1, 1, 0.07)).setTransparency(TransparencyAttrib.MAlpha)

		self.logout = DirectButton(image = "Interface/submitBtn.png", command=self.clickedLogout, pos = (-0.8, 0, -0.7),scale = (0.1, 1, 0.07)).setTransparency(TransparencyAttrib.MAlpha)


	def clickedStart(self):
		if(self.SelectChar is not ""):
			print "You pressed Start", self.SelectChar
			self.world.cManager.sendRequest(Constants.CMSG_CREATE_CHARACTER, self.user[1]+" "+self.SelectChar);

	def clickedLogout(self):
		self.world.cManager.sendRequest(Constants.CMSG_DISCONNECT, self.user[1]);




	def processingCreateResponse(self, data):
		self.msg1 = data.getInt32()
		if self.msg1:
			self.pl_list = []
			self.name = data.getString()
			self.char = data.getString()
			self.pl_count = data.getInt32()
			for num in range (0,self.pl_count):
				self.pl_list.append([num+1,data.getString()])
				print self.pl_list
			# self.pl_count = data.getInt32()
			# print "ResponseCreate name - ", self.name
			# print "ResponseCreate char- ", self.char
			# for num in range (0,self.pl_count):
			# 	self.pl_list.append([num+1,data.getString()])
			# 	print self.pl_list
			# 	#h(self,self.welcome,self.pl_list)
			self.destroyWindow()


			# self.world.Game(self.name,self.char,self.pl_count,self.pl_list)

			# self.world.CharSelect(self.welcome,self.pl_list)
		else :
			print "Create error"

	def destroyWindow(self):
		self.frame.destroy()
		self.textObject.destroy()
		self.window.destroy()
		# for m in self.set1.getChildren():
		# 	m.destroy()
		# 	self.set1.removeNode()
