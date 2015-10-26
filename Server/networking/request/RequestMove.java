package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseMove;
import utility.DataReader;

public class RequestMove extends GameRequest {

    // Data
    private float x;
    private float y;
    private float z;
    private float h;
    private int isMoving;
    // Responses
    private ResponseMove responseMove;

    public RequestMove() {
        responses.add(responseMove = new ResponseMove());
    }

    @Override
    public void parse() throws IOException {
        x = DataReader.readFloat(dataInput);
        y = DataReader.readFloat(dataInput);
        z = DataReader.readFloat(dataInput);
        h = DataReader.readFloat(dataInput);
        isMoving = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseMove.setX(x);
        responseMove.setY(y);
        responseMove.setZ(z);
        responseMove.setH(h);
        responseMove.setIsMoving(isMoving);
    }
}
