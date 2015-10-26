from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseExitGame(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()

            print "ResponseExitGame - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_SAVE_EXIT_GAME) + '] String Response')
            print_exc()