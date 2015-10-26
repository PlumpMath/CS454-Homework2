package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseMove extends GameResponse {

    private float x;
    private float y;
    private float z;
    private float h;
    private int isMoving;

    public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addFloat(x);
        packet.addFloat(y);
        packet.addFloat(z);
        packet.addFloat(h);
        packet.addInt32(isMoving);

        return packet.getBytes();
    }

    public float getX() {
  		return x;
  	}

  	public void setNumber(float x) {
  		this.x = x;
  	}

    public float getY() {
  		return y;
  	}

  	public void setNumber(float y) {
  		this.y = y;
  	}

    public float getZ() {
  		return z;
  	}

  	public void setNumber(float z) {
  		this.z = z;
  	}

    public float getH() {
  		return h;
  	}

  	public void setNumber(float h) {
  		this.h = h;
  	}

    public int getIsMoving() {
  		return isMoving;
  	}

  	public void setNumber(int isMoving) {
  		this.isMoving = isMoving;
  	}
}
