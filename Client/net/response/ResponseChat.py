from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChat(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseChat - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] String Response')
            print_exc()