package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseCreateCharacter extends GameResponse {

    private float number;

    public ResponseCreateCharacter() {
        responseCode = Constants.SMSG_CREATE_CHARACTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addCreateCharacter(number+1);

        return packet.getBytes();
    }

	public float getNumber() {
		//return number;
	}

	public void setNumber(CreateCharacter number) {
		//this.number = number;
	}
}
