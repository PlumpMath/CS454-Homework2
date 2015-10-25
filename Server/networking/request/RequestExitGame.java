package networking.request;

// Java Imports
import java.io.IOException;

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
        //responseExitGame.setNumber(number);
    }
}
