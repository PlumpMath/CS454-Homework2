package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseLogout extends GameResponse {

    private float number;

    public ResponseLogout() {
        responseCode = Constants.SMSG_Logout;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addLogout(number+1);

        return packet.getBytes();
    }

	public float getNumber() {
		//return number;
	}

	public void setNumber(Logout number) {
		//this.number = number;
	}
}
