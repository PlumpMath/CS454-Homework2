from common.Constants import Constants

from net.request.RequestRandomInt import RequestRandomInt
from net.request.RequestRandomString import RequestRandomString
from net.request.RequestRandomShort import RequestRandomShort
from net.request.RequestRandomFloat import RequestRandomFloat
from net.request.RequestLogin import RequestLogin
from net.request.RequestLogout import RequestLogout
from net.request.RequestRegistration import RequestRegistration
from net.request.RequestChat import RequestChat
from net.request.RequestMove import RequestMove
from net.request.RequestHeartbeat import RequestHeartbeat
from net.request.RequestExitGame import RequestExitGame
from net.request.RequestCreateCharacter import RequestCreateCharacter

class ServerRequestTable:
    """
    The ServerRequestTable contains a mapping of all requests for use
    with the networking component.
    """
    requestTable = {}

    def __init__(self):
        """Initialize the request table."""
        self.add(Constants.RAND_INT, 'RequestRandomInt')
        self.add(Constants.RAND_STRING, 'RequestRandomString')
        self.add(Constants.RAND_SHORT, 'RequestRandomShort')
        self.add(Constants.RAND_FLOAT, 'RequestRandomFloat')
        self.add(Constants.CMSG_AUTH, 'RequestLogin')
        self.add(Constants.CMSG_DISCONNECT, 'RequestLogout')
        self.add(Constants.CMSG_REGISTER, 'RequestRegistration')
        self.add(Constants.CMSG_CHAT, 'RequestChat')
        self.add(Constants.CMSG_MOVE, 'RequestMove')
        self.add(Constants.REQ_HEARTBEAT, 'RequestHeartbeat')
        self.add(Constants.CMSG_SAVE_EXIT_GAME, 'RequestExitGame')
        self.add(Constants.CMSG_CREATE_CHARACTER,'RequestCreateCharacter')


    def add(self, constant, name):
        """Map a numeric request code with the name of an existing request module."""
        # print self.requestTable
        if name in globals():
            self.requestTable[constant] = name
            # print name
        else:
            print 'Add Request Error: No module named ' + str(name)

    def get(self, requestCode):
        """Retrieve an instance of the corresponding request."""
        serverRequest = None

        if requestCode in self.requestTable:
            serverRequest = globals()[self.requestTable[requestCode]]()
        else:
            print 'Bad Request Code: ' + str(requestCode)

        return serverRequest
