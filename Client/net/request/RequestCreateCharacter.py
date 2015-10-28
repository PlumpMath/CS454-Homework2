from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCreateCharacter(ServerRequest):


    def send(self, characterInfo = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_AUTH)
            characterList = characterInfo.split(",")
            pkg.addString(characterList[0])
            pkg.addUint16(int(characterList[1]))
            pkg.addUint16(int(characterList[2]))


            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] Int Request')
            print_exc()
