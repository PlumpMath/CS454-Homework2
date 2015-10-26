package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseCharacterCreation;
import utility.DataReader;

public class RequestCharacterCreation extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseCharacterCreation responseCharacterCreation;

    public RequestCharacterCreation() {
        responses.add(responseCharacterCreation = new ResponseCharacterCreation());
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
