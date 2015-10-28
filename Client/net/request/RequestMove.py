from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestMove(ServerRequest):


    def send(self, pos):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_MOVE)
            posNew = pos.split(",")
            pkg.addFloat32(float(posNew[0]))
            pkg.addFloat32(float(posNew[1]))
            pkg.addFloat32(float(posNew[2]))
            pkg.addFloat32(float(posNew[3]))
            pkg.addInt32(int(posNew[4]))

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_MOVE) + '] Int Request')
            print_exc()
