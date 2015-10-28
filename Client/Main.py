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
