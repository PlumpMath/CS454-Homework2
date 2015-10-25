package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseCreateCharacter;
import utility.DataReader;

public class RequestCreateCharacter extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseCreateCharacter responseCreateCharacter;

    public RequestCreateCharacter() {
        responses.add(responseCreateCharacter = new ResponseCreateCharacter());
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
