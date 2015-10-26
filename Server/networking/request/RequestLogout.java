package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseLogout;
import utility.DataReader;

public class RequestLogout extends GameRequest {
  
    // Responses
    private ResponseLogout responseLogout;

    public RequestLogout() {
        responses.add(responseLogout = new ResponseLogout());
    }

    @Override
    public void parse() throws IOException {
    }

    @Override
    public void doBusiness() throws Exception {

    }
}
