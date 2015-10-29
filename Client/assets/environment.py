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

	def rotatePlanets(self, planet, player, task):
		if (self.isRotating is False and (planet.getPos() - player.getPos()).length() < 5):
			print("start")
			self.start_rotating = task.time
			self.isRotating = True

		if (self.isRotating is True):
			do = task.time - self.start_rotating
			planet.setH(planet.getH() + 5)

		if (self.isRotating is True and (planet.getPos() - player.getPos()).length() > 5):
			self.isRotating = False
		return task.cont


	'''
	def rotatePlanets(self, planet, player, task):
		if (self.isRotating is False and isClose(self, planet, player, users):
			print("start")
			self.start_rotating = task.time
			self.isRotating = True

		if (self.isRotating is True):
			do = task.time - self.start_rotating
			planet.setH(planet.getH() + 5)

		if (self.isRotating is True and not isClose(self, planet, player, users) ):
			self.isRotating = False
		return task.cont


	def isClose(self, planet, player, users):
		print('')
		for user in users:
			if (planet.getPos() - user.getPos()).length() < 5:
				return True

		if (planet.getPos() - player.getPos()).length() < 5:
			return True

		else return False
		'''



class Sun(Environment):

	def __init__(self, world):
		# Create the spheres
		self.isRotating= False
		self.world = world

		#The sun
		self.world.sun = loader.loadModel("models/planet_sphere")
		self.world.sun_tex = loader.loadTexture("models/sun_1k_tex.jpg")
		self.world.sun.setTexture(self.world.sun_tex, 1)
		self.world.sun.reparentTo(render)
		self.world.sun.setScale(1.2)
		self.world.sun.setPos(random.randrange(-30, 30, 2),random.randrange(-30, 30, 2),3)

	'''def isClose(self, player, users):



	def rotatePlanets(self, player, task):
		if (self.isRotating is False and (self.world.sun.getPos() - player.getPos()).length() < 5):
			print("start")
			self.start_rotating = task.time
			self.isRotating = True

		if (self.isRotating is True):
			do = task.time - self.start_rotating
			self.world.sun.setH(self.world.sun.getH() + 5)

		if (self.isRotating is True and (self.world.sun.getPos() - player.getPos()).length() > 5):
			self.isRotating = False
		return task.cont'''

class Venus(Environment):

	def __init__(self, world):
		self.isRotating= False
		# Create the spheres
		self.world = world

		#The venus
		self.world.venus = loader.loadModel("models/planet_sphere")
		self.world.venus_tex = loader.loadTexture("models/venus_1k_tex.jpg")
		self.world.venus.setTexture(self.world.venus_tex, 1)
		self.world.venus.reparentTo(render)
		self.world.venus.setScale(1.2)
		self.world.venus.setPos(random.randrange(-30, 30, 2),random.randrange(-30, 30, 2),3)

	'''def rotatePlanets(self, player, task):
		if (self.isRotating is False and (self.world.venus.getPos() - player.getPos()).length() < 5):
			print("start")
			self.start_rotating = task.time
			self.isRotating = True

		if (self.isRotating is True):
			do = task.time - self.start_rotating
			self.world.venus.setH(self.world.venus.getH() + 5)

		if (self.isRotating is True and (self.world.venus.getPos() - player.getPos()).length() > 5):
			self.isRotating = False
		return task.cont'''


class Earth(Environment):

	def __init__(self, world):
		self.isRotating= False
		# Create the spheres
		self.world = world

		#The earth
		self.world.earth = loader.loadModel("models/planet_sphere")
		self.world.earth_tex = loader.loadTexture("models/earth_1k_tex.jpg")
		self.world.earth.setTexture(self.world.earth_tex, 1)
		self.world.earth.reparentTo(render)
		self.world.earth.setScale(1.2)
		self.world.earth.setPos(random.randrange(-30, 30, 2),random.randrange(-30, 30, 2),3)

	'''def rotatePlanets(self, player, task):
		if (self.isRotating is False and (self.world.earth.getPos() - player.getPos()).length() < 5):
			print("start")
			self.start_rotating = task.time
			self.isRotating = True

		if (self.isRotating is True):
			do = task.time - self.start_rotating
			self.world.earth.setH(self.world.earth.getH() + 5)

		if (self.isRotating is True and (self.world.earth.getPos() - player.getPos()).length() > 5):
			self.isRotating = False
		return task.cont'''



