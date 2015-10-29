package networking.response;

// Custom Imports
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

import database.DbClient;
import database.DbConnect;
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
            Logger.getLogger(DbConnect.class.getName()).log(Level.SEVERE, null, ex);
        }

        ResultSet resultlist = connect.Query("select * from connectedPlayers;");

        try {
            while (resultlist.next()) {

                System.out.println("hi test"+resultlist.getString("username"));
                System.out.println("hi test"+resultlist.getString("model"));

                  this.client.setUsername(resultlist.getString("username"));

                packet.addString(resultlist.getString("username")+","+resultlist.getString("model"));


            }
        } catch (SQLException ex) {
            Logger.getLogger(DbConnect.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        ResultSet result2 = connect.Query("Select p.username, c.model, p.pos, p.isMoving from connectedPlayers c, players p where p.username = c.username;");

        try {
            while (result2.next()) {
                packet.addString(result2.getString("p.username")+","+result2.getString("c.model")
                					+","+result2.getString("p.pos")+","+result2.getBoolean("p.isMoving"));
            }
        } catch (SQLException ex) {
            Logger.getLogger(DbConnect.class.getName()).log(Level.SEVERE, null, ex);
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

  	private static final DbClient connect = new DbClient();

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
            Logger.getLogger(DbConnect.class.getName()).log(Level.SEVERE, null, ex);
        }

        return 0;
    }
}
