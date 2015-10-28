from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseLogout(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()

            print "ResponseLogout - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_DISCONNECT) + '] String Response')
            print_exc()