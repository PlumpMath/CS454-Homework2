from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
# from modules.characterSelection import characterSelection

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            self.msg1 = data.getInt32()
            self.msg2 = data.getString()
            print "ResponseLogin - ", self.msg1
            print "ResponseLogin - ", self.msg2
            # self.characterSelection()
            # return task.done
            # taskMgr.add(self.characterSelection, "characterSelection")

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
