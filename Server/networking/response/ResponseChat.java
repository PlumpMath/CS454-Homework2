package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseChat extends GameResponse {

    private String message;

    public ResponseChat() {
        responseCode = Constants.SMSG_CHAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(1);

        return packet.getBytes();
    }

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
}
