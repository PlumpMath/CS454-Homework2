import direct.directbase.DirectStart
import random, sys, os, math, time

from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Point3
from panda3d.core import Vec3,Vec4,BitMask32

from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Sequence
from direct.showbase.DirectObject import DirectObject

class User:
	def __init__(self, username, world, x, y, z, h, isMoving, modelName):
		self.username = username
		self.world = world
		self.x = x
		self.y = y
		self.z = z
		self.h = h;
		self.isMoving = isMoving
		self.modelName = modelName

	def loadUser(self):
		
		if modelName = "ralph" or "Ralph":
			self.user = Actor("models/ralph",
                                 {"run":"models/ralph-run",
                                  "walk":"models/ralph-walk"})
		if modelName = "Panda" or "panda":
			self.user = Actor("models/panda-model",
                                {"run": "models/panda-walk4"})

		if modelName = "Car" or "car":
			self.user = Actor("models/T-SM3")


        self.user.reparentTo(render)
        self.user.setScale(0.003)
        self.user.setPos(random.randrange(-30, 30, 2),random.randrange(-30, 30, 2),0)

    #def updateUserPos(self, username, x, y, z, h, isMoving):





