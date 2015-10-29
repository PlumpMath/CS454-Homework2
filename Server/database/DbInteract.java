package database;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;


// sample class to use db

public class DbInteract {


	    private static final DbClient connect = new DbClient();


	    public static int obtenerNumRegistros() {

	        ResultSet resultado = connect.Query("SELECT COUNT(*) FROM tweets;");

	        try {
	            while (resultado.next()) {

	                return resultado.getInt("COUNT(*)");


	            }
	        } catch (SQLException ex) {
	            Logger.getLogger(DbInteract.class.getName()).log(Level.SEVERE, null, ex);
	        }

	        return -1;
	    }

	    public static void insertarTweet(String id) {


	    	connect.Update("INSERT INTO tweets (id) VALUES ('"+id+"')");
	    }


	    public static void eliminarTweet(String id) {

	    	connect.Update("DELETE FROM tweets WHERE id = '"+id+"'");        
	    }

	    public static HashMap<String, Integer> obtenerHoraTweet(String id) {

	        HashMap<String, Integer> resultados = new HashMap<>();

	        ResultSet resultado = connect.Query("SELECT hora, min FROM tweets WHERE id = '"+id+"'");

	        try {
	            while (resultado.next()) {

	                resultados.put("Hora", resultado.getInt(1));
	                resultados.put("Minuto", resultado.getInt("min"));

	            }
	        } catch (SQLException ex) {
	            Logger.getLogger(DbInteract.class.getName()).log(Level.SEVERE, null, ex);
	        }

	        return resultados;

	    }

	    public static ArrayList<String> obtenerIdsRetweets(int retweets) {


	        ArrayList<String> resultados = new ArrayList<>();

	        ResultSet resultado = connect.Query("SELECT id FROM tweets WHERE retweets > "+retweets);

	        try {
	            while (resultado.next()) {
	                resultados.add(resultado.getString("id"));
	            }
	        } catch (SQLException ex) {
	            Logger.getLogger(DbInteract.class.getName()).log(Level.SEVERE, null, ex);
	        }

	        return resultados;
	    }


}
