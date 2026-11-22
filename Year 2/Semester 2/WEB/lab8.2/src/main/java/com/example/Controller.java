package com.example;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Map;

@WebServlet(name = "controller", value = "/controller")
public class Controller extends HttpServlet {
    private boolean isLoggedIn(HttpServletRequest request, HttpServletResponse response) throws IOException {
        HttpSession session = request.getSession(false);
        if (session == null || !"true".equals(session.getAttribute("login"))) {
            response.sendRedirect("loginError.html");
            return false;
        }
        return true;
    }

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        if (!isLoggedIn(request, response)) {
            return;
        }

        String action = request.getParameter("action");
        if ("start".equals(action)) {
            startQuiz(request, response);
        } else if ("answer".equals(action)) {
            saveAnswers(request, response);
        } else if ("finish".equals(action)) {
            finishQuiz(request, response);
        } else {
            response.sendRedirect("quizSetup.jsp");
        }
    }

    private void startQuiz(HttpServletRequest request, HttpServletResponse response) throws IOException {
        HttpSession session = request.getSession();
        int userId = (Integer) session.getAttribute("userID");

        int quizId = parseInt(request.getParameter("quiz_id"), 0);
        int totalQuestions = parseInt(request.getParameter("total_questions"), 0);
        int questionsPerPage = parseInt(request.getParameter("questions_per_page"), 0);

        if (quizId <= 0 || totalQuestions <= 0 || questionsPerPage <= 0 || questionsPerPage > totalQuestions) {
            session.setAttribute("error", "Choose a quiz and use valid positive numbers. Questions per page cannot be bigger than total questions.");
            response.sendRedirect("quizSetup.jsp");
            return;
        }

        DatabaseConnector db = new DatabaseConnector();
        int availableQuestions = db.getQuestionCount(quizId);
        if (availableQuestions < totalQuestions) {
            session.setAttribute("error", "This quiz only has " + availableQuestions + " questions.");
            response.sendRedirect("quizSetup.jsp");
            return;
        }

        int attemptId = db.createAttempt(userId, quizId, totalQuestions, questionsPerPage);
        session.setAttribute("attemptID", attemptId);
        writeQuizPage(response.getWriter(), session, db, attemptId, 1);
    }

    private void saveAnswers(HttpServletRequest request, HttpServletResponse response) throws IOException {
        HttpSession session = request.getSession();
        Integer attemptId = (Integer) session.getAttribute("attemptID");
        if (attemptId == null) {
            response.sendRedirect("quizSetup.jsp");
            return;
        }

        DatabaseConnector db = new DatabaseConnector();
        Map<Integer, Integer> answers = db.readSubmittedAnswers(request.getParameterMap());
        db.saveAnswers(attemptId, answers);

        int nextPage = parseInt(request.getParameter("next_page"), 1);
        if (nextPage > db.getPageCount(attemptId)) {
            response.sendRedirect("result.jsp");
            return;
        }

        writeQuizPage(response.getWriter(), session, db, attemptId, nextPage);
    }

    private void finishQuiz(HttpServletRequest request, HttpServletResponse response) throws IOException {
        HttpSession session = request.getSession();
        Integer attemptId = (Integer) session.getAttribute("attemptID");
        if (attemptId == null) {
            response.sendRedirect("quizSetup.jsp");
            return;
        }

        DatabaseConnector db = new DatabaseConnector();
        db.saveAnswers(attemptId, db.readSubmittedAnswers(request.getParameterMap()));
        db.finishAttempt(attemptId);
        response.sendRedirect("result.jsp");
    }

    private void writeQuizPage(PrintWriter out, HttpSession session, DatabaseConnector db, int attemptId, int page) {
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Quiz</title>");
        out.println("<script src='quiz.js' defer></script>");
        out.println("</head>");
        out.println("<body>");
        out.println("<div class='top-bar'><p>Hello " + session.getAttribute("username") + "!</p><form action='logout' method='post'><input type='submit' value='Logout'></form></div>");
        out.println("<main>");
        out.println("<h1>Quiz test</h1>");
        out.println(db.getQuizPageHtml(attemptId, page));
        out.println("</main>");
        out.println("</body>");
        out.println("</html>");
    }

    private int parseInt(String value, int defaultValue) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException ex) {
            return defaultValue;
        }
    }
}
