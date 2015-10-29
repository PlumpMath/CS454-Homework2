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
from characterSelection import characterSelection

""" Custom Imports """
# import your modules
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager
from login import login
from old.game import *

# from modules.characterSelection import characterSelection

class Main(DirectObject):

    def __init__(self):

	    # Network Setup
        self.cManager = ConnectionManager(self)
        self.cManager.startConnection()
        self.login = login(self)



    def getUserName(self):
        print "Vatsal Sevak in Login Page"

    # def CharSelect(self,msg,
        
    def CharSelect(self, welcome, userList):
        self.welcome = welcome
        self.userList = userList
        self.charSelect = characterSelection(self)

    def Logout(self):
        print "Logout"

    def Game(self,user,char,count,playerlist):
        self.user = user
        self.char = char
        self.count = count
        self.playerlist = playerlist
        print self.user
        print self.char
        print self.count
        print self.playerlist

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

            print "game started"

    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True


m = Main()
run()
