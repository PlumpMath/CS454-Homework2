from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCreateCharacter(ServerRequest):


    def send(self, character = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_CHARACTER)
            characterlist =character.split()
            # print "characterlist", characterlist
            # print "username ",characterlist[0]
            # print "charname ",characterlist[1]
            pkg.addString(characterlist[0])
            pkg.addString(characterlist[1])
            
            

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] Int Request')
            print_exc()
