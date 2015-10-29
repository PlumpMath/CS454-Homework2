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
from game import *

# from modules.characterSelection import characterSelection

class Main(DirectObject):

    def __init__(self):
        base.win.setClearColor(Vec4(0,0,0,1))
 
        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.environ.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

	    # Network Setup
        self.cManager = ConnectionManager(self)
        self.cManager.startConnection()
        # self.login = login(self)



    
        
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
        self.StartGame = Game(self)
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
