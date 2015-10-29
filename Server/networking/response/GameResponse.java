package networking.response;

// Java Imports
import java.lang.reflect.Field;

import core.GameClient;

/**
 * The GameResponse class is an abstract class used as a basis for storing
 * response information.
 */
public abstract class GameResponse {

    protected byte[] responseInBytes; // Response information stored as bytes
    protected short responseCode;
	protected GameClient client;

    /**
     * Convert the response into bytes format.
     * 
     * @return the response as bytes
     */
    public abstract byte[] constructResponseInBytes();
    
    public void setGameClient(GameClient client) {
        this.client = client;
    }


    @Override
    public String toString() {
        String str = "";

        str += "-----" + "\n";
        str += getClass().getName() + "\n";
        str += "\n";

        for (Field field : getClass().getDeclaredFields()) {
            try {
                str += field.getName() + " - " + field.get(this) + "\n";
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        }

        str += "-----";

        return str;
    }
}