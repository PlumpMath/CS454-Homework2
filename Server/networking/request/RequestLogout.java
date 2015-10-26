package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseLogout;
import utility.DataReader;

public class RequestLogout extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseLogout responseLogout;

    public RequestLogout() {
        responses.add(responseLogout = new ResponseLogout());
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
