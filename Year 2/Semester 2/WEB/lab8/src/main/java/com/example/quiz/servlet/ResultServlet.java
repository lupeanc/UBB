package com.example.quiz.servlet;

import com.example.quiz.dao.QuizDao;
import com.example.quiz.model.Attempt;
import com.example.quiz.model.BestResult;
import com.example.quiz.model.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.Optional;

@WebServlet("/quiz/result")
public class ResultServlet extends HttpServlet {
    private final QuizDao quizDao = new QuizDao();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        User user = (User) request.getSession().getAttribute("user");
        Long attemptId = (Long) request.getSession().getAttribute("attemptId");
        if (attemptId == null) {
            response.sendRedirect(request.getContextPath() + "/quiz/config");
            return;
        }

        Optional<Attempt> attempt = quizDao.findAttempt(attemptId, user.id());
        if (attempt.isEmpty()) {
            response.sendRedirect(request.getContextPath() + "/quiz/config");
            return;
        }
        if ("IN_PROGRESS".equals(attempt.get().status())) {
            quizDao.finishAttempt(attemptId);
            attempt = quizDao.findAttempt(attemptId, user.id());
        }

        Optional<BestResult> bestResult = quizDao.findBestResult(user.id());
        request.setAttribute("attempt", attempt.get());
        request.setAttribute("bestResult", bestResult.orElse(null));
        request.getRequestDispatcher("/WEB-INF/views/result.jsp").forward(request, response);
    }
}
