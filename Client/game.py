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
from users import *

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

        taskMgr.add(self.menu, "Menu")


    def Start(self,pl_name,pl_char,pl_count,pl_list):



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


        if pl_char == "Panda1"  or pl_char == "Panda2":
            print "hi"
            player = Panda(self)
        elif pl_char == "Car":
            player = Car(self)
        else :
            player = Ralph(self)

        #player = Car(self)


        # player = Panda(self)
        # player = Car(self)



        taskMgr.add(player.move,"moveTask" )
        taskMgr.add(sun.rotatePlanets,"rotateSun", extraArgs = [self.sun,self.player], appendTask = True)
        taskMgr.add(earth.rotatePlanets,"rotateEarth", extraArgs = [self.earth, self.player], appendTask = True)
        taskMgr.add(venus.rotatePlanets,"rotateVenus", extraArgs = [self.venus, self.player], appendTask = True)


        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))

    def menu(self, task):
        self.option = 0
        choice = input("1-Register\n2-Login\n3-Exit\n")

        msg = 0
        self.username = ""
        self.password = ""
        self.cpassword = ""

        if choice is 1:
            self.username = str(raw_input("Enter the username\n"))
            self.password = str(raw_input("Enter the password\n"))
            self.cpassword = str(raw_input("Confirm password\n"))
            if self.password == self.cpassword:
                self.cManager.sendRequest(Constants.CMSG_REGISTER, self.username+" "+self.password)

        elif choice is 2:
            self.username = str(raw_input("Enter the username\n"))
            self.password = str(raw_input("Enter the password\n"))
            self.cManager.sendRequest(Constants.CMSG_AUTH, self.username+" "+self.password);
        elif choice is 3:
            sys.exit()
        else: print "Invalid input"

    def processingLoginResponse(self, data):

        self.msg1 = data.getInt32()
        if self.msg1:
            self.pl_list = []
            self.playersList = []
            self.user = data.getString().split(" ")
            self.pl_count = data.getInt32()

            print "welcome ",self.user[1]
            print "No of players logged in- ", self.pl_count
            for num in range (0,self.pl_count):
                self.pl_list.append([num+1,data.getString()])

            for num in range (0,self.pl_count):
                playerTemp = data.getString().split(",")
                self.playersList.append([User(playerTemp[0], float(playerTemp[2]), float(playerTemp[3])
                                            float(playerTemp[4]), float(playerTemp[5]),
                                            int(playerTemp[6]), playerTemp[1])])
                # print self.pl_list
            #h(self,self.welcome,self.pl_list)

            charlist =["Car","Ralph","Panda1","Panda2"]
            usedlist =[]
            for l in self.pl_list :
                pl = l[1].split(",")
                usedlist.append(pl[1])
                charlist.remove(pl[1])

            print "Pick a Available Charactor", charlist
            role = raw_input("")
            print self.user[1]
            print role
            self.cManager.sendRequest(Constants.CMSG_CREATE_CHARACTER, self.user[1]+" "+role)
            # self.world.CharSelect(self.welcome,self.pl_list)

        else :
            print "Username Or Password invalid"

    def processingCreateResponse(self, data):
        self.msg1 = data.getInt32()
        if self.msg1:
            self.pl_list = []
            self.name = data.getString()
            self.char = data.getString()
            self.pl_count = data.getInt32()
            for num in range (0,self.pl_count):
                self.pl_list.append([num+1,data.getString()])
                # print self.pl_list

        self.Start(self.name,self.char,self.pl_count,self.pl_list)

w = World()
run()
