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
        
	    # Network Setup
        self.cManager = ConnectionManager(self)
        self.cManager.startConnection()
        # self.login = login(self)
        taskMgr.add(self.menu, "Menu")



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
            self.user = data.getString().split(" ")
            self.pl_count = data.getInt32()

            print "welcome ",self.user[1]
            print "No of players logged in- ", self.pl_count
            for num in range (0,self.pl_count):
                self.pl_list.append([num+1,data.getString()])
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

        self.StartGame = self.Start(self)



    
        
    # def CharSelect(self, welcome, userList):
    #     self.welcome = welcome
    #     self.userList = userList
    #     self.charSelect = characterSelection(self)

    # def Logout(self):
    #     print "Logout"

    # def Game(self,user,char,count,playerlist):
    #     self.user = user
    #     self.char = char
    #     self.count = count
    #     self.playerlist = playerlist
    #     print self.user
    #     print self.char
    #     print self.count
    #     print self.playerlist
    #     self.StartGame = Game(self)
    #     print "game started"

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
