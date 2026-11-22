package com.example;

import java.sql.Connection;

public class Main {

    public static void main(String[] args) {

        try {

            Connection con = DBConnection.initializeDB();

            if (con != null) {
                System.out.println("Connected!");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}