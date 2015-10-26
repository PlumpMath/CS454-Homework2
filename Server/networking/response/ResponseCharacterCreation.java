package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseCharacterCreation extends GameResponse {

    private String characterName;
    private int factionId;
    private int classType;

    public ResponseCharacterCreation() {
        responseCode = Constants.SMSG_CREATE_CHARACTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(characterName);
        packet.addInt32(factionId);
        packet.addInt32(classType);
        return packet.getBytes();
    }

    public String getCharacterName() {
  		return characterName;
  	}

  	public void setCharacterName(String characterName) {
  		this.characterName = characterName;
  	}

    public int getFactionId() {
  		return factionId;
  	}

  	public void setFactionId(int factionId) {
  		this.factionId = factionId;
  	}

    public int getClassType() {
  		return classType;
  	}

  	public void setClassType(int classType) {
  		this.classType = classType;
  	}
}
