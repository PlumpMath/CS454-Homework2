package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseDisconnect;
import utility.DataReader;

public class RequestDisconnect extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseDisconnect responseDisconnect;

    public RequestDisconnect() {
        responses.add(responseDisconnect = new ResponseDisconnect());
    }

    @Override
    public void parse() throws IOException {
        //message = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        //responseCreateCharacter.setNumber(number);
    }
}
