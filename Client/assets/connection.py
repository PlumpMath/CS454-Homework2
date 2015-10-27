from direct.showbase.ShowBase import ShowBase
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode,NodePath,Camera,TextNode

from panda3d.core import ConnectionWriter
from panda3d.core import NetDatagram
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader

import random, sys, os, math

class Connection(ShowBase):
	def __init__(self):

		self.cManager = QueuedConnectionManager()
		self.cListener = QueuedConnectionListener(self.cManager, 0)
		self.cReader = QueuedConnectionReader(self.cManager, 0)
		self.cWriter = ConnectionWriter(self.cManager, 0)

		try:
			host = "localhost"
			port = 9252
			self.connection = self.cManager.openTCPClientConnection(host, port, 10000)

			self.received = 1

			if self.connection:
				self.cReader.addConnection(self.connection)
				taskMgr.add(self.updateRoutine, 'updateRoutine')
				# taskMgr.add(self.message, 'message')
		except:
			pass

	# def message(self, task):
	# 	self.option = 0
	# 	self.option = str(raw_input("1-Send integer\n2-Send string\n3-Send short\n4-Send float\n"))
	# 	if self.option == "1":
	# 		msg = int(100 * random.random()) - 50
	# 		request = self.intRequest(msg)
	# 		self.cWriter.send(request,self.connection)
	# 		print "sent ", msg
	# 		taskMgr.remove('message')
	# 	elif self.option == "2":
	# 		msg = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(7))
	# 		request = self.stringRequest(msg)
	# 		self.cWriter.send(request,self.connection)
	# 		print "sent ", msg
	# 		taskMgr.remove('message')
	# 	elif self.option == "3":
	# 		msg = int(100 * random.random())
	# 		request = self.shortRequest(msg)
	# 		self.cWriter.send(request,self.connection)
	# 		print "sent ", msg
	# 		taskMgr.remove('message')
	# 	elif self.option == "4":
	# 		msg = 100 * random.random()
	# 		request = self.floatRequest(msg)
	# 		self.cWriter.send(request,self.connection)
	# 		print "sent ", msg
	# 		taskMgr.remove('message')

	def intRequest(self, msg):
		pkg = PyDatagram()
		pkg.addUint16(1)
		pkg.addInt32(msg)
		return pkg

	def stringRequest(self, msg):
		pkg = PyDatagram()
		pkg.addUint16(2)
		pkg.addString(msg)
		return pkg

	def shortRequest(self, msg):
		pkg = PyDatagram()
		pkg.addUint16(3)
		pkg.addUint16(msg)
		return pkg

	def floatRequest(self, msg):
		pkg = PyDatagram()
		pkg.addUint16(4)
		pkg.addFloat32(msg)
		return pkg

	def loginRequest(self, username, password):
		pkg = PyDatagram()
		pkg.addUint16(101)
		pkg.addString(username)
		pkg.addString(password)
		return pkg

	def registerRequest(self, username, password):
		pkg = PyDatagram()
		pkg.addUint16(103)
		pkg.addString(username)
		pkg.addString(password)
		return pkg

	def characterCreationRequest(self, username, classType):
		pkg = PyDatagram()
		pkg.addUint16(104)
		pkg.addString(username)
		pkg.addUint16(0)
		pkg.addUint16(classType)
		return pkg

	def chatRequest(self, message):
		pkg = PyDatagram()
		pkg.addUint16(105)
		pkg.addString(message)
		return pkg

	def moveRequest(self, x, y, z, h, isMoving):
		pkg = PyDatagram()
		pkg.addUint16(106)
		pkg.addFloat32(x)
		pkg.addFloat32(y)
		pkg.addFloat32(z)
		pkg.addFloat32(h)
		pkg.addUint16(isMoving)
		return pkg

	def check(self):
		while self.cReader.dataAvailable():
			print "data here"
			datagram = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram):
				data = PyDatagramIterator(datagram)
				responseCode = data.getUint16()
				print responseCode
				if responseCode == 1:
					self.getInt(data)
				elif responseCode == 2:
					self.getString(data)
				elif responseCode == 3:
					self.getShort(data)
				elif responseCode == 4:
					self.getFloat(data)
				elif responseCode == 201:
					self.getLogin(data)
				elif responseCode == 203:
					self.getRegistion(data)
				elif responseCode == 204:
					self.getCharacterCreation(data)
				elif responseCode == 205:
					self.getChat(data)
				elif responseCode == 206:
					self.getMove(data)
				else:
					print "nothing found"

	def getInt(self, data):
		msg = data.getInt32()
		print "recieved ", msg
		taskMgr.add(self.message, 'message')

	def getString(self, data):
		msg = data.getString()
		print "recieved ", msg
		taskMgr.add(self.message, 'message')

	def getShort(self, data):
		msg = data.getUint16()
		print "recieved ", msg
		taskMgr.add(self.message, 'message')

	def getFloat(self, data):
		msg = data.getFloat32()
		print "recieved ", msg
		taskMgr.add(self.message, 'message')

	def getLogin(self, data):
		flag = data.getUint16()

		if(flag == 0):
			print "Invalid Login"
		else:
			listSize = data.getUint16()

			for i in xrange(listSize):
				characterName = data.getString()
				characterId = data.getUint16()
				characterType = data.getUint16()
				characterFaction = data.getUint16()

				# Need to add these to an active characters class


	def getRegistion(self, data):
		flag = data.getUint16()

		if(flag == 0):
			print "Invalid Login"
		else:
			print "Account Created"

	def getCharacterCreation(self, data):
		flag = data.getUint16()

		if(flag == 0):
			print "Invalid Character"
		else:
			listSize = data.getUint16()

			for i in xrange(listSize):
				characterName = data.getString()
				characterId = data.getUint16()
				characterType = data.getUint16()
				characterFaction = data.getUint16()

				# Need to add these to an active characters class

	def getChat(self, data):
		username = data.getString()
		factionId = data.getUint16()
		message = data.getString()

	def getMove(self, data):
		username = data.getString()
		x = data.getFloat32()
		y = data.getFloat32()
		z = data.getFloat32()
		h = data.getFloat32()
		isMoving = data.getUint16()

	def updateRoutine(self,task):
		self.check()
		return task.again;
