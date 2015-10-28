package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseCharacterCreation;
import utility.DataReader;

public class RequestCharacterCreation extends GameRequest {

    // Data
	private String username;
    private String characterName;
    //private int factionId;
    //private int classType;
    // Responses
    private ResponseCharacterCreation responseCharacterCreation;

    public RequestCharacterCreation() {
        responses.add(responseCharacterCreation = new ResponseCharacterCreation());
    }

    @Override
    public void parse() throws IOException {
    	username = DataReader.readString(dataInput);
        characterName = DataReader.readString(dataInput);
        //factionId = DataReader.readInt(dataInput);
        //classType = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
    	responseCharacterCreation.setUsername(username);
        responseCharacterCreation.setCharacterName(characterName);
        //responseCharacterCreation.setFactionId(factionId);
        //responseCharacterCreation.setClassType(classType);
    }
}
