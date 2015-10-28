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
from common.Constants import Constants
from m import ModelSelection

class login(DirectObject):
    TEXT_COLOR = (1,1,1,1)
    FONT_TYPE_01 = 0
    TEXT_SHADOW_COLOR = (0,0,0,0.5)
    usernameInput = ""
    passwordInput = ""
    frame = DirectFrame()
    window = OnscreenImage()
    username = OnscreenText()
    password = OnscreenText()
    cpassword = OnscreenText()
    failed = OnscreenText()
    userTextbox = DirectEntry()
    passTextbox = DirectEntry()
    submitBtn = DirectButton()
    registerBtn = DirectButton()
    cancelBtn = DirectButton()
    
    
    registerUsername = ""
    registerPassword = ""
    registerCPassword = ""
    
    regInputUser = DirectEntry()
    regInputPass = DirectEntry()
    regInputCPass = DirectEntry()
    
    regRegisterBtn = DirectButton()
    regCancelBtn = DirectButton()
    
    def __init__(self, world):
        self.world = world
        print 'Loading Login...'
        frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                            frameSize=(-1, 1, -1, 1),#(Left,Right,Bottom,Top)
                            pos=(-0.5, 0, 0.5))
        self.createLoginWindow()
    

    def clearPassText(self):
        self.passTextbox.enterText('')
    def clearUserText(self):
        self.userTextbox.enterText('')
    def clearRegUserText(self):
        self.regInputUser.enterText('')
    def clearRegPassText(self):
        self.regInputPass.enterText('')
    def clearRegCPassText(self):
        self.regInputCPass.enterText('')

    def getUserText(self):
        self.usernameInput = self.userTextbox.get()
    def getPassText(self):
        self.passwordInput = self.passTextbox.get()
    def setUserText(self, textEntered):
        print "username: ",textEntered
        self.usernameInput = textEntered
        print(usernameInput)
    def setPassText(self, textEntered):
        print "password: ",textEntered
        self.passwordInput = textEntered
    def clickedSubmit(self):
        self.usernameInput = self.userTextbox.get().strip()
        self.passwordInput = self.passTextbox.get().strip()
        if(self.usernameInput is not "" and self.passwordInput is not ""):
            print "You pressed Submit", self.usernameInput, " ; ",self.passwordInput
            self.world.cManager.sendRequest(Constants.CMSG_AUTH, self.usernameInput+" "+self.passwordInput);
        else:
            print "Please enter in a username and password"
    def clickedCancel(self):
        print "You pressed Cancel"
        exit()
    def clickedRegister(self):
        print "You pressed Register"
        self.createRegisterWindow()
    def clickedRegRegister(self):
        self.registerUsername = self.regInputUser.get()
        self.registerPassword = self.regInputPass.get()
        self.registerCPassword = self.regInputCPass.get()
        if self.registerPassword == self.registerCPassword:
            print "Success (",self.registerUsername, ", ",self.registerPassword,", ",self.registerCPassword,")"
            self.world.cManager.sendRequest(Constants.CMSG_REGISTER, self.registerUsername+" "+self.registerPassword)
            self.createLoginWindow()
        else:
            self.failed = OnscreenText(text="Your password does not match Confirm Password.", pos=(-0.5, 0.5), scale=0.06,fg=(1,0.1,0.1,1), align=TextNode.ALeft,mayChange=0)
            print "Failed (",self.registerUsername, ", ",self.registerPassword,", ",self.registerCPassword,")"
    def clickedRegCancel(self):
        self.destroyRegisterWindow()
        self.createLoginWindow()
    def destroyLoginWindow(self):
        self.frame.destroy()
        self.username.destroy()
        self.password.destroy()
        self.userTextbox.destroy()
        self.passTextbox.destroy()
        self.submitBtn.destroy()
        self.registerBtn.destroy()
        self.cancelBtn.destroy()
    def destroyRegisterWindow(self):
        self.frame.destroy()
        self.username.destroy()
        self.password.destroy()
        self.cpassword.destroy()
        self.regInputUser.destroy()
        self.regInputPass.destroy()
        self.regInputCPass.destroy()
        self.cancelBtn.destroy()
        self.registerBtn.destroy()
        self.failed.destroy();
    def createLoginWindow(self):
        

        self.window = OnscreenImage(image = "Interface/login_window.png", pos = (0,0,0), scale = (2, 1, 2) )
        self.window.setTransparency(TransparencyAttrib.MAlpha)

        self.userTextbox = DirectEntry(text = "" ,scale=.05, pos = (-0.3, 0, 0.3),command=self.setUserText,initialText="Username",  numLines = 2,focus=0,focusInCommand=self.clearUserText, focusOutCommand=self.getUserText)
        self.passTextbox = DirectEntry(text = "" ,scale=.05, pos = (-0.3, 0, 0.1),command=self.setPassText,initialText="password", numLines = 2,focus=0,focusInCommand=self.clearPassText, focusOutCommand=self.getPassText)
        
        self.username = OnscreenText(text = "Username:", pos = (-0.6, 0.3), scale = 0.05,fg=(0,0,0.2,1),align=TextNode.ALeft,mayChange=0)
        self.password = OnscreenText(text="Password: ", pos = (-0.6, 0.1), scale=0.05, fg=(0, 0,0.2,1), align=TextNode.ALeft, mayChange=0)

        self.submitBtn = DirectButton(image = "Interface/submitBtn.png", command=self.clickedSubmit, pos = (0.35, 0, -0.2),scale = (0.1, 1, 0.07))
        self.submitBtn.setTransparency(TransparencyAttrib.MAlpha)
        self.registerBtn = DirectButton(image = "Interface/registerBtn.png", command=self.clickedRegister, pos = (0.1, 0, -0.2),scale = (0.1, 1, 0.07))
        self.registerBtn.setTransparency(TransparencyAttrib.MAlpha)
        self.cancelBtn = DirectButton(image = "Interface/cancelBtn.png", command=self.clickedCancel, pos = (-0.35, 0, -0.2),scale = (0.1, 1, 0.07))
        self.cancelBtn.setTransparency(TransparencyAttrib.MAlpha)

    def createRegisterWindow(self):
        


        self.window = OnscreenImage(image = "Interface/login_window.png", pos = (0,0,0), scale = (2, 1, 2) )
        self.window.setTransparency(TransparencyAttrib.MAlpha)


        self.username = OnscreenText(text = "Username:", pos = (-0.9, 0.3), scale = 0.05,fg=(0,0,0.2,1),align=TextNode.ALeft,mayChange=0)
        self.password = OnscreenText(text="Password: ", pos = (-0.9, 0.1), scale=0.05, fg=(0, 0,0.2,1), align=TextNode.ALeft, mayChange=0)
        self.cpassword = OnscreenText(text="Confirm Password: ", pos = (-0.9, -0.1), scale=0.05, fg=(0, 0,0.2,1), align=TextNode.ALeft, mayChange=0)
        

        self.regInputUser = DirectEntry(text = "" ,scale=.05, pos = (-0.3, 0, 0.3), command=self.setUserText,initialText="username", numLines = 1,focus=0,focusInCommand=self.clearRegUserText, focusOutCommand=self.getUserText)
        self.regInputPass = DirectEntry(text = "" ,scale=.05, pos = (-0.3, 0, 0.1),command=self.setPassText,initialText="password", numLines = 1,focus=0,focusInCommand=self.clearRegPassText, focusOutCommand=self.getPassText)
        self.regInputCPass = DirectEntry(text = "" ,scale=.05, pos = (-0.3, 0, -0.1),command=self.setPassText,initialText="confirm password", numLines = 1,focus=0,focusInCommand=self.clearRegCPassText, focusOutCommand=self.getPassText)
       

        self.registerBtn = DirectButton(image = "Interface/registerBtn.png", command=self.clickedRegRegister, pos = (0.1, 0, -0.4),scale = (0.1, 1, 0.07))
        self.registerBtn.setTransparency(TransparencyAttrib.MAlpha)
        self.cancelBtn = DirectButton(image = "Interface/cancelBtn.png", command=self.clickedRegCancel, pos = (-0.35, 0, -0.4),scale = (0.1, 1, 0.07))
        self.cancelBtn.setTransparency(TransparencyAttrib.MAlpha)

    def processingLoginResponse(self, data):

        self.msg1 = data.getInt32()
        if self.msg1:
            self.pl_list = []
            self.welcome = data.getString()
            self.pl_count = data.getInt32()
            print "ResponseLogin - ", self.msg1
            print "ResponseLogin msg- ", self.pl_count
            for num in range (0,self.pl_count):
                self.pl_list.append([num+1,data.getString()])
                print self.pl_list
            #h(self,self.welcome,self.pl_list)
            self.world.CharSelect(self.welcome,self.pl_list)

        else :
            print "login error"


