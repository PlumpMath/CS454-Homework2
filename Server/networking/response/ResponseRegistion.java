package networking.response;

// Custom Imports
import database.DbClient;
import metadata.Constants;
import utility.GamePacket;

public class ResponseRegistion extends GameResponse {

    private String username;
    private String password;

    public ResponseRegistion() {
        responseCode = Constants.SMSG_REGISTER;
    }

    @Override
    public byte[] constructResponseInBytes() {

    	int number = 0;
    	boolean flag;
        flag = addUser(username, password); 
    	
        if(flag) {
        	
        	number=1;
      	  System.out.println("valid");
      GamePacket packet = new GamePacket(responseCode);
      packet.addInt32(number);
      return packet.getBytes();
        }
        else {
        	number=0;
        	 System.out.println("invalid");
             GamePacket packet = new GamePacket(responseCode);
             packet.addInt32(number);
             return packet.getBytes();
        }
    }

    public String getUsername() {
      return username;
    }

    public void setUsername(String username) {
      this.username = username;
    }

    public String getPassword() {
      return password;
    }

    public void setPassword(String password) {
      this.password = password;
    }
    
    private static final DbClient connect = new DbClient("cs454user", "cs454pwd","hw2db", "localhost", "3306");


    private boolean addUser(String user, String pwd) {
    	
        System.out.println("before db");
        
    	return connect.Update("insert into players VALUES ('"+user+"','"+pwd+"','0,0,0,0',False);");
    }
}
