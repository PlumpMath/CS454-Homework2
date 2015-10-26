package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseLogout extends GameResponse {

    public ResponseLogout() {
        responseCode = Constants.SMSG_DISCONNECT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        return packet.getBytes();
    }
}
