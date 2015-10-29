from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRegistration(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getInt32()

            if self.msg:
            	print "User Added Successful"
            	print " "
            	conn.main.menu(self)
            	# taskMgr.add(conn.main.menu, "Menu")

            else:
            	print "Registration Error"

            # print "ResponseRegistration - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_REGISTER) + '] String Response')
            print_exc()