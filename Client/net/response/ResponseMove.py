from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseMove(ServerResponse):

    def execute(self, conn, data):

        try:
            self.username = data.getString()
            self.x = data.getFloat()
            self.y = data.getFloat()
            self.z = data.getFloat()
            self.h = data.getFloat()
            self.isMoving = data.getInt32()

            print "ResponseMove - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] String Response')
            print_exc()
