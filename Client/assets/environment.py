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

class Environment:

	def __init__():
		self.isRotating = False

	def rotatePlanets(self, player, task):
		if (self.isRotating is False and (self.world.planet.getPos() - player.getPos()).length() < 10):
			print("start")
			self.start_rotating = task.time
			self.isRotating = True

		if (self.isRotating is True):
			print("ok")
			do = task.time - self.start_rotating
			self.setH(self.world..getH() + 10)
		return task.cont




class Sun(Environment):

	def __init__(self, world):
		# Create the spheres
		self.world = world

		#The sun
		self.world.planet = loader.loadModel("models/planet_sphere")
		self.world.planet_tex = loader.loadTexture("models/sun_1k_tex.jpg")
		self.world.planet.setTexture(self.world.planet_tex, 1)
		self.world.planet.reparentTo(render)
		self.world.planet.setScale(1.2)
		self.world.planet.setPos(random.randrange(10,15, 2),random.randrange(10, 15, 2),3)
		#self.world.planet.setPos(random.randrange(-30, 30, 2),random.randrange(-30, 30, 2),3)



class Venus(Environment):

	def __init__(self, world):
		# Create the spheres
		self.world = world

		#The venus
		self.world.planet = loader.loadModel("models/planet_sphere")
		self.world.planet_tex = loader.loadTexture("models/venus_1k_tex.jpg")
		self.world.planet.setTexture(self.world.planet_tex, 1)
		self.world.planet.reparentTo(render)
		self.world.planet.setScale(1.2)
		self.world.planet.setPos(random.randrange(10,15, 2),random.randrange(10, 15, 2),3)
		#self.world.planet.setPos(random.randrange(-30, 30, 2),random.randrange(-30, 30, 2),3)



class Earth(Environment):

	def __init__(self, world):
		# Create the spheres
		self.world = world

		#The earth
		self.world.planet = loader.loadModel("models/planet_sphere")
		self.world.planet_tex = loader.loadTexture("models/earth_1k_tex.jpg")
		self.world.planet.setTexture(self.world.planet_tex, 1)
		self.world.planet.reparentTo(render)
		self.world.planet.setScale(1.2)
		self.world.planet.setPos(random.randrange(10,15, 2),random.randrange(10, 15, 2),3)
		#self.world.planet.setPos(random.randrange(-30, 30, 2),random.randrange(-30, 30, 2),3)




