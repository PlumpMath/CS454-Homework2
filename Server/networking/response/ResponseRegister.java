package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseRegister extends GameResponse {

    private float number;

    public ResponseRegister() {
        responseCode = Constants.SMSG_REGISTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addRegister(number+1);

        return packet.getBytes();
    }

	public float getNumber() {
		//return number;
	}

	public void setNumber(Register number) {
		//this.number = number;
	}
}
