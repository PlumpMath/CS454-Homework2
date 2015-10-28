package networking.response;

// Custom Imports
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

import database.DbClient;
import database.DbInteract;
import metadata.Constants;
import utility.GamePacket;

public class ResponseLogin extends GameResponse {

    private String username;
    private String password;

    public ResponseLogin() {
        responseCode = Constants.SMSG_AUTH;
    }

    @Override
    public byte[] constructResponseInBytes() {
      
      int number = 0;
      number = validateUser(username, password); 
   

      if(number==1) {
    	  System.out.println("valid");
    	  int count =0;
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(number);
        packet.addString("Welcome "+username);
        
        ResultSet resultcount = connect.Query("select count(*) from connectedPlayers;");

        try {
            while (resultcount.next()) {

                count = resultcount.getInt("COUNT(*)");
                System.out.println("hi count"+count);
                packet.addInt32(count);


            }
        } catch (SQLException ex) {
            Logger.getLogger(DbInteract.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        ResultSet resultlist = connect.Query("select * from connectedPlayers;");
        
        try {
            while (resultlist.next()) {
            	
                System.out.println("hi test"+resultlist.getString("username"));
                System.out.println("hi test"+resultlist.getString("model"));
                
                packet.addString(resultlist.getString("username")+","+resultlist.getString("model"));


            }
        } catch (SQLException ex) {
            Logger.getLogger(DbInteract.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
        
        return packet.getBytes();
      }
      else {
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


    private int validateUser(String user, String pwd) {
        System.out.println("before db");
        
        ResultSet result = connect.Query("select * from players where username='"+user+"';");
        System.out.println("after");
        try {
            while (result.next()) {
                System.out.println("hi test"+result.getString("password"));
                if (pwd.equals(result.getString("password")))
                {
                	System.out.println("matched");
                	return 1;
                }
                else
                {
                	System.out.println("unmatched");
                	return 0;
                }


            }
        } catch (SQLException ex) {
            Logger.getLogger(DbInteract.class.getName()).log(Level.SEVERE, null, ex);
        }

        return 0;
    }
}
