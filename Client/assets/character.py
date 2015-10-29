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

from common.Constants import Constants

class Character:
    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.world.keyMap[key] = value

    def loadControls(self):
        # Accept the control keys for movement and rotation
        self.world.accept("escape", sys.exit)

        # Movement
        self.world.accept("w", self.setKey, ["forward",1])
        self.world.accept("a", self.setKey, ["left",1])
        self.world.accept("s", self.setKey, ["backward",1])
        self.world.accept("d", self.setKey, ["right",1])
        self.world.accept("w-up", self.setKey, ["forward",0])
        self.world.accept("a-up", self.setKey, ["left",0])
        self.world.accept("s-up", self.setKey, ["backward",0])
        self.world.accept("d-up", self.setKey, ["right",0])

        self.world.accept("arrow_left", self.setKey, ["left",1])
        self.world.accept("arrow_right", self.setKey, ["right",1])
        self.world.accept("arrow_up", self.setKey, ["forward",1])
        self.world.accept("arrow_down", self.setKey, ["backward", 1])
        self.world.accept("arrow_left-up", self.setKey, ["left",0])
        self.world.accept("arrow_right-up", self.setKey, ["right",0])
        self.world.accept("arrow_up-up", self.setKey, ["forward",0])
        self.world.accept("arrow_down-up", self.setKey, ["backward", 0])

        # Camera
        self.world.accept("q", self.setKey, ["cam-right",1])
        self.world.accept("e", self.setKey, ["cam-left",1])
        self.world.accept("q-up", self.setKey, ["cam-right",0])
        self.world.accept("e-up", self.setKey, ["cam-left",0])

    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):
        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.
        base.camera.lookAt(self.world.player)
        if (self.world.keyMap["cam-left"]!=0):
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if (self.world.keyMap["cam-right"]!=0):
            base.camera.setX(base.camera, +20 * globalClock.getDt())

        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.

        startpos = self.world.player.getPos()

        # If a move-key is pressed, move ralph in the specified direction.

        if (self.world.keyMap["left"]!=0):
            self.world.player.setH(self.world.player.getH() + 300 * globalClock.getDt())
        if (self.world.keyMap["right"]!=0):
            self.world.player.setH(self.world.player.getH() - 300 * globalClock.getDt())
        if (self.world.keyMap["forward"]!=0):
            self.world.player.setY(self.world.player, -25 * globalClock.getDt())
        if (self.world.keyMap["backward"]!=0):
            self.world.player.setY(self.world.player, 25 * globalClock.getDt())

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.

        if (self.world.keyMap["forward"]!=0) or (self.world.keyMap["backward"]!=0) or (self.world.keyMap["left"]!=0) or (self.world.keyMap["right"]!=0):
            if self.world.isMoving is False:
                self.world.player.loop("run")
                self.world.isMoving = True
                self.world.cManager.sendRequest(Constants.CMSG_MOVE, str(self.world.player.getX()) + "," +
                                                                     str(self.world.player.getY()) + "," +
                                                                     str(self.world.player.getZ()) + "," +
                                                                     str(self.world.player.getH()) + ",1")
        else:
            if self.world.isMoving:
                self.world.player.stop()
                self.world.player.pose("walk",5)
                self.world.isMoving = False
                self.world.cManager.sendRequest(Constants.CMSG_MOVE, str(self.world.player.getX()) + "," +
                                                                     str(self.world.player.getY()) + "," +
                                                                     str(self.world.player.getZ()) + "," +
                                                                     str(self.world.player.getH()) + ",0")

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.

        camvec = self.world.player.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0


        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.

        self.world.floater.setPos(self.world.player.getPos())
        self.world.floater.setZ(self.world.player.getZ() + 2.0)
        base.camera.lookAt(self.world.floater)

        return task.cont



    def isMovePossible(self,newPosition):
        possibleMove = True
        # for : # every characters on the map
        #     possibleMove = self.detectCollision(newPosition, character)
        #     if possibleMove is False :
        #         return possibleMove
        # return possibleMove

    def detectCollision(self, newPosition, character) :
        d = (newPosition - character.getPos()).length
        if( d < self.radius + character.radius ):
            return False
        else:
            return True

class Ralph(Character):
    def __init__(self, world):
        self.world = world
        self.world.keyMap = {"left":0, "right":0, "forward":0, "backward":0, "cam-left":0, "cam-right":0}

        # Create the main character, Ralph
        self.world.player = Actor("models/ralph",
                                 {"run":"models/ralph-run",
                                  "walk":"models/ralph-walk"})
        self.world.player.reparentTo(render)
        self.world.player.setScale(.2)
        self.world.player.setPos(10,10,0)
        base.camera.setPos(self.world.player.getX(),self.world.player.getY()+10,2)
        base.disableMouse()

        self.loadControls()
        self.world.isMoving = False

        self.radius = 10

class Panda(Character):
    def __init__(self, world):
        self.world = world
        self.world.keyMap = {"left":0, "right":0, "forward":0, "backward":0, "cam-left":0, "cam-right":0}

        # Create the main character, Ralph
        self.world.player = Actor("models/panda-model")
        self.world.player.reparentTo(render)
        self.world.player.setScale(0.004)
        self.world.player.setPos(10,10,0)
        base.camera.setPos(self.world.player.getX(),self.world.player.getY()+10,2)
        base.disableMouse()

        self.loadControls()
        self.world.isMoving = False

        self.radius = 20
class Car(Character):
    def __init__(self, world):
        self.world = world
        self.world.keyMap = {"left":0, "right":0, "forward":0, "backward":0, "cam-left":0, "cam-right":0}

        # Create the main character, Ralph
        self.world.player = Actor("models/T-SM3")
        self.world.player.reparentTo(render)
        self.world.player.setScale(0.3)
        self.world.player.setPos(10,10,0)
        self.world.player.setHpr(0, 0, 0)
        base.camera.setPos(self.world.player.getX(),self.world.player.getY()+10,2)
        base.disableMouse()

        self.loadControls()
        self.world.isMoving = False

        self.radius = 30
