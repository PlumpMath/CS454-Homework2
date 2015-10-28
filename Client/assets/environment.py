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
	def __init__(self, world):
		# Create the spheres
    	self.world.sun = loader.loadModel("models/planet_sphere")
	    self.world.sun_tex = loader.loadTexture("models/world.sun_1k_tex.jpg")
	    self.world.sun.setTexture(self.world.sun_tex, 1)
	    self.world.sun.reparentTo(render)
	    self.world.sun.setScale(2 * self.sizescale)

        self.world.sun.setPos(random.randrange(0, 40, 2),random.randrange(0, 40, 2),3)



