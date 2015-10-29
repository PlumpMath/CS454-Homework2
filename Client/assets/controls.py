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

class Control:
    def __init__(self):
        self.text()

    # Function to put instructions on the screen.
    def addInstructions(self, pos, msg):
        return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                            pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

    # Function to put title on the screen.
    def addTitle(self, text):
        return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                            pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)

    def text(self):
        # Post the instructions
        self.title = self.addTitle("Homework 2")
        self.inst1 = self.addInstructions(0.95, "[ESC]: Quit")
        self.inst2 = self.addInstructions(0.90, "[A]: Move Left")
        self.inst3 = self.addInstructions(0.85, "[D]: Move Right")
        self.inst4 = self.addInstructions(0.80, "[W]: Move Forward")
        self.inst5 = self.addInstructions(0.75, "[S]: Moonwalk")
        self.inst6 = self.addInstructions(0.70, "[Q]: Rotate Camera Left")
        self.inst7 = self.addInstructions(0.65, "[E]: Rotate Camera Right")
        self.inst7 = self.addInstructions(0.60, "*Arrow Keys also work.")
        self.inst8 = self.addInstructions(0.55, "[M] : Open Chat Box")
        self.inst9 = self.addInstructions(0.50, "[Shift + W] : Run")
