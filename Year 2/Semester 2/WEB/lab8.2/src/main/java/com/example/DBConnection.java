package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnection {
    protected static Connection initializeDB() throws ClassNotFoundException, SQLException {

        String dbDriver = "com.mysql.cj.jdbc.Driver";
        String dbURL = "jdbc:mysql://localhost:3306/lab8";

//        String dbName = "lab8";
        String dbUser = "root";
        String dbPassword = "";

        // loads the mysql jdb dirver into memory
        // + registers it with driverManager
        Class.forName(dbDriver);
        return DriverManager.getConnection(dbURL, dbUser, dbPassword);
    }
}
