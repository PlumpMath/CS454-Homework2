package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseExitGame extends GameResponse {

    private float number;

    public ResponseExitGame() {
        responseCode = Constants.SMSG_SAVE_EXIT_GAME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(1);

        return packet.getBytes();
    }

/*	public float getNumber() {
		//return number;
	}

	public void setNumber(ExitGame number) {
		//this.number = number;
	}
	
	*/
}
