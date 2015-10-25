package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseDisconnect extends GameResponse {

    private float number;

    public ResponseDisconnect() {
        responseCode = Constants.SMSG_DISCONNECT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addDisconnect(number+1);

        return packet.getBytes();
    }

	public float getNumber() {
		//return number;
	}

	public void setNumber(Disconnect number) {
		//this.number = number;
	}
}
