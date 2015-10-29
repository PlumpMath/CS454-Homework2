package networking.request;

// Java Imports
import java.io.IOException;

import database.DbClient;
// Custom Imports
//import core.GameServer;
import networking.response.ResponseExitGame;
import utility.DataReader;

public class RequestExitGame extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseExitGame responseExitGame;

    public RequestExitGame() {
        responses.add(responseExitGame = new ResponseExitGame());
    }

    @Override
    public void parse() throws IOException {
        //message = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
    	final DbClient connect = new DbClient();
        connect.Update("delete from connectedPlayers where username = " + this.client.getUsername() + ";");
        
        //responseExitGame.setNumber(number);
    }
}
