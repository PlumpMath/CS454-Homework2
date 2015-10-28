package networking.response;

// Custom Imports
import database.DbClient;
import metadata.Constants;
import utility.GamePacket;

public class ResponseCharacterCreation extends GameResponse {
	
	private String username;
    private String characterName;
    //private int factionId;
    //private int classType;

    public ResponseCharacterCreation() {
        responseCode = Constants.SMSG_CREATE_CHARACTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
    	int number=0;
    	boolean flag =true;
        flag = addPlayer(username, characterName); 
        
        if(flag) {
        	number=1;
      	  	System.out.println("valid");
      	  	GamePacket packet = new GamePacket(responseCode);
      	  	packet.addInt32(number);
      	  packet.addString(username);
      	  packet.addString(characterName);
      	  	return packet.getBytes();
        }
        else {
        	number=0;
        	System.out.println("invalid");
            GamePacket packet = new GamePacket(responseCode);
            packet.addInt32(number);
            return packet.getBytes();
        }
    	
    	
//        GamePacket packet = new GamePacket(responseCode);
//        packet.addString(characterName);
//        //packet.addInt32(factionId);
//        //packet.addInt32(classType);
//        return packet.getBytes();
    }

    public String getCharacterName() {
  		return characterName;
  	}

  	public void setCharacterName(String characterName) {
  		this.characterName = characterName;
  	}
  	
  	public String getUsername() {
  		return username;
  	}

  	public void setUsername(String username) {
  		this.username = username;
  	}


  /*  public int getFactionId() {
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
  	*/
  	
  	private static final DbClient connect = new DbClient("cs454user", "cs454pwd","hw2db", "localhost", "3306");


    private boolean addPlayer(String user, String charactor) {
    	
        System.out.println("before db");
        System.out.println(charactor);
        
    	return connect.Update("insert into connectedPlayers (username,model) VALUES ('"+user+"','"+charactor+"');");
    }
}
