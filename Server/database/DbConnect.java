package database;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;

public class DbConnect {

    private Connection  connection  = null;
    private Statement   statement   = null;
    private ResultSet   set         = null;

    String host;
    String port;
    String login;
    String password;
    String url;

    public DbConnect (String login, String password, String db, String host, String port) {
        this.login = login;
        this.password = password;
        this.host = host;
        this.port = port;
        url = "jdbc:mysql://"+host+":"+port+"/"+db;
        Connect ();
    }

    public void Disconnect () {
        connection = null;
    }

    private void Connect() {
        try {
            DriverManager.registerDriver(new com.mysql.jdbc.Driver ());
        } catch (SQLException ex) {
            Logger.getLogger(DbConnect.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            connection = DriverManager.getConnection(url, login, password);
            statement = connection.createStatement();
        }

        catch (SQLException e) {
            Logger logger = Logger.getLogger(DbConnect.class.getName());
            logger.log(Level.SEVERE, e.getSQLState(), e);
        }
    }

    public ResultSet Query(String query){

        try {
            statement = connection.createStatement();
            set = statement.executeQuery(query);
        }
        catch (Exception e) {
            System.out.println("Exception in query method:\n" + e.getMessage());
        }
        return set;
    }

    public boolean Update (String update) {

        try {
            statement = connection.createStatement();
            statement.executeUpdate(update);

        }
        catch (SQLException e) {
            System.out.println("Exception in update method:\n" + e.getMessage());
            return false;
        }

        return true;
    }

    public void closeConnection(){

        try {
            connection.close();
            connection = null;
        }
        catch(Exception e)         {
            System.out.println("Problem in closing connection ");
        }
    }

}