from traceback import print_exc

from common.Constants import Constants
# from cs import main
from net.response.ServerResponse import ServerResponse


from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import Texture
from panda3d.core import WindowProperties
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Sequence

# from modules.characterSelection import characterSelection

class ResponseLogin(ServerResponse):

    def execute(self, conn, data):

        try:
            
            conn.main.login.processingLoginResponse(data)

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
