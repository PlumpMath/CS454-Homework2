package networking.request;

// Java Imports
import java.io.IOException;



// Custom Imports
//import core.GameServer;
import networking.response.ResponseLogin;
import utility.DataReader;

public class RequestLogin extends GameRequest {

    // Data
    private String username;
    private String password;
    // Responses
    private ResponseLogin responseLogin;

    public RequestLogin() {
        responses.add(responseLogin = new ResponseLogin());
    }

    @Override
    public void parse() throws IOException {
        username = DataReader.readString(dataInput);
        password = DataReader.readString(dataInput);
       // System.out.println("RequestLogin : code " +username);
      //  System.out.println("RequestLogin : code " +password);
    }

    @Override
    public void doBusiness() throws Exception {
        responseLogin.setUsername(username);
        responseLogin.setPassword(password);
    }
}
