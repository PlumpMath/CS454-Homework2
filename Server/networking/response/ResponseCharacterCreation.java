package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseCharacterCreation extends GameResponse {

    private float number;

    public ResponseCharacterCreation() {
        responseCode = Constants.SMSG_CREATE_CHARACTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addCharacterCreation(number+1);

        return packet.getBytes();
    }

	public float getNumber() {
		//return number;
	}

	public void setNumber(CharacterCreation number) {
		//this.number = number;
	}
}
