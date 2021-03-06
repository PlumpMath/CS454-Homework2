from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseHeartbeat(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseHeartbeat - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.REQ_HEARTBEAT) + '] String Response')
            print_exc()