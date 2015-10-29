package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseChat;
import utility.DataReader;

public class RequestChat extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseChat responseChat;

    public RequestChat() {
        responseChat = new ResponseChat();
    }

    @Override
    public void parse() throws IOException {
        message = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        if(message.substring(0, 3).toLowerCase().equals("/m "))
        {
          String[] messaging = message.split();
          message = message.replace(messaging[0] + messaging[1], "");
          responseChat.setMessage("Whisper from "this.client.getUsername() + " : " + message);

          this.client.getServer().addResponseForUser(messaging[1], responseMove);
        }
        else
        {
          responseChat.setMessage(this.client.getUsername() + " : " + message);
        }
    }
}
