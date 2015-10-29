import __builtin__

""" Python Imports """
from hashlib import md5
from sys import exit
from time import strftime

""" Panda3D Imports """
from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import Texture
from panda3d.core import WindowProperties
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
import direct.directbase.DirectStart
import random, sys, os, math, time
import os.path
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Point3
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Sequence

sys.path.append(os.path.join(os.path.dirname(__file__), "assets"))
from controls import Control
from character import *
from chat import *
from environment import *
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager

SPEED = 0.5

class World(DirectObject):

    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True

    def __init__(self):
        base.win.setClearColor(Vec4(0,0,0,1))

        # Network Setup
        print "before"
        self.cManager = ConnectionManager(self)
        self.startConnection()
        print "after"

        # Set up the environment
        #

        self.environ = loader.loadModel("models/square")
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.environ.setScale(100,100,1)
        self.moon_tex = loader.loadTexture("models/moon_1k_tex.jpg")
    	self.environ.setTexture(self.moon_tex, 1)

        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

        # # add spheres
        earth = Earth(self)
        sun = Sun(self)
        venus = Venus(self)



        controls = Control()
        chat = Chat(self)
        player = Car(self)


        # player = Panda(self)
        # player = Car(self)



        taskMgr.add(player.move,"moveTask" )
        taskMgr.add(sun.rotatePlanets,"rotateSun", extraArgs = [self.player], appendTask = True)
        taskMgr.add(earth.rotatePlanets,"rotateEarth", extraArgs = [self.player], appendTask = True)
        taskMgr.add(venus.rotatePlanets,"rotateVenus", extraArgs = [self.player], appendTask = True)


        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))

w = World()
run()
