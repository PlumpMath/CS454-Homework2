package networking.response;

// Custom Imports
import database.DbClient;
import metadata.Constants;
import utility.GamePacket;

public class ResponseLogout extends GameResponse {
	
	private String username;

    public ResponseLogout() {
        responseCode = Constants.SMSG_DISCONNECT;
    }

    @Override
    public byte[] constructResponseInBytes() {
    	
    	int number = 0;
    	boolean flag;
        flag = Userlogout(username); 
        
        if(flag) {
        	System.out.println("Logout");
        GamePacket packet = new GamePacket(responseCode);
        return packet.getBytes();
        }
        else {
        	      	 
             GamePacket packet = new GamePacket(responseCode);
             //packet.addInt32(number);
             return packet.getBytes();
        }
    }
    
    public String getUsername() {
  		return username;
  	}

  	public void setUsername(String username) {
  		this.username = username;
  	}
  	
  	private static final DbClient connect = new DbClient();


    private boolean Userlogout(String user) {
    	
        System.out.println("before db");
        
    	return connect.Update("delete from connectedPlayers where username='"+user+"';");
    }
}
