package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseHeartbeat extends GameResponse {

    private float number;

    public ResponseHeartbeat() {
        responseCode = Constants.SMSG_HEARTBEAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addHeartbeat(number+1);

        return packet.getBytes();
    }

	public float getNumber() {
		//return number;
	}

	public void setNumber(Heartbeat number) {
		//this.number = number;
	}
}
