import direct.directbase.DirectStart
import random, sys, os, math, time
import os.path

from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Point3
from panda3d.core import Vec3,Vec4,BitMask32

from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Sequence
from direct.showbase.DirectObject import DirectObject

sys.path.append(os.path.join(os.path.dirname(__file__), "assets"))
from controls import Control
from character import *
from chat import *

SPEED = 0.5

class World(DirectObject):
    def __init__(self):
        base.win.setClearColor(Vec4(0,0,0,1))

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

        controls = Control()
        chat = Chat(self)
        player = Ralph(self)

        # player = Panda(self)
        # player = Car(self)

        taskMgr.add(player.move,"moveTask")


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
