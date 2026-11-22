package com.example.quiz.servlet;

import com.example.quiz.dao.QuizDao;
import com.example.quiz.model.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/quiz/config")
public class ConfigServlet extends HttpServlet {
    private final QuizDao quizDao = new QuizDao();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setAttribute("availableQuestions", quizDao.countQuestions());
        request.getRequestDispatcher("/WEB-INF/views/config.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int availableQuestions = quizDao.countQuestions();
        int totalQuestions = parseInt(request.getParameter("totalQuestions"), -1);
        int questionsPerPage = parseInt(request.getParameter("questionsPerPage"), -1);

        if (totalQuestions < 1 || totalQuestions > availableQuestions || questionsPerPage < 1 || questionsPerPage > totalQuestions) {
            request.setAttribute("availableQuestions", availableQuestions);
            request.setAttribute("error", "Choose a test size between 1 and " + availableQuestions
                + ", and a page size between 1 and the test size.");
            request.setAttribute("totalQuestions", request.getParameter("totalQuestions"));
            request.setAttribute("questionsPerPage", request.getParameter("questionsPerPage"));
            request.getRequestDispatcher("/WEB-INF/views/config.jsp").forward(request, response);
            return;
        }

        User user = (User) request.getSession().getAttribute("user");
        long attemptId = quizDao.createAttempt(user.id(), totalQuestions, questionsPerPage);
        request.getSession().setAttribute("attemptId", attemptId);
        response.sendRedirect(request.getContextPath() + "/quiz?page=1");
    }

    private int parseInt(String value, int fallback) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            return fallback;
        }
    }
}
