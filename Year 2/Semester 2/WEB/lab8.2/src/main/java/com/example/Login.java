package com.example;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet(name = "login", value = "/login")
public class Login extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        response.setContentType("text/html");

        String username = request.getParameter("username");
        String password = request.getParameter("password");

        DatabaseConnector db = new DatabaseConnector();
        int userId = db.getUserId(username, password);

        if (userId != 0) {
            HttpSession session = request.getSession();
            session.setAttribute("login", "true");
            session.setAttribute("userID", userId);
            session.setAttribute("username", username);
            response.sendRedirect("quizSetup.jsp");
        } else {
            response.sendRedirect("loginError.html");
        }
    }
}
