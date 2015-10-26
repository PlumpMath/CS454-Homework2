package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseRegistion;
import utility.DataReader;

public class RequestRegistion extends GameRequest {

  // Data
  private String username;
  private String password;
  // Responses
  private ResponseRegistion responseRegistion;

  public RequestRegistion() {
      responses.add(responseRegistion = new ResponseRegistion());
  }

  @Override
  public void parse() throws IOException {
      username = DataReader.readString(dataInput);
      password = DataReader.readString(dataInput);
  }

  @Override
  public void doBusiness() throws Exception {
      responseRegistion.setUsername(username);
      responseRegistion.setPassword(password);
  }
}
