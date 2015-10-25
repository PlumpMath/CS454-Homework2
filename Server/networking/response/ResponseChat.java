package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseChat extends GameResponse {

    private float number;

    public ResponseChat() {
        responseCode = Constants.SMSG_CHAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addChat(number+1);

        return packet.getBytes();
    }

	public float getNumber() {
		//return number;
	}

	public void setNumber(Chat number) {
		//this.number = number;
	}
}
