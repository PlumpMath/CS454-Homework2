package networking.request;

// Java Imports
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

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
        private static final DbClient connect = new DbClient("cs454user", "cs454pwd", "hw2db", "localhost", "3306");

        System.out.println("before db");

        String sql = "UPDATE players SET pos=?, isMoving=? WHERE username=?";

        c = DriverManager.getConnection( url, username, password );
        PreparedStatement pstmt = c.prepareStatement( sql );
        pstmt.setString( 1, x + "," + y + "," + z + "," + h );
        if(isMoving == 1)
        {
          pstmt.setBoolean(2, true);
        }
        else
        {
          pstmt.setBoolean(2, false);
        }
        pstmt.setString( 3, "Vicken");
        pstmt.executeUpdate();
        } catch (SQLException ex) {
            Logger.getLogger(DbInteract.class.getName()).log(Level.SEVERE, null, ex);
        }

        responseMove.setX(x);
        responseMove.setY(y);
        responseMove.setZ(z);
        responseMove.setH(h);
        responseMove.setIsMoving(isMoving);
      }
}
