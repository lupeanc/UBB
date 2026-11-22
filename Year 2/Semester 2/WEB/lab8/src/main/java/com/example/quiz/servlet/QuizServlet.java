package com.example.quiz.servlet;

import com.example.quiz.dao.QuizDao;
import com.example.quiz.model.Attempt;
import com.example.quiz.model.Question;
import com.example.quiz.model.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.List;
import java.util.Optional;

@WebServlet("/quiz")
public class QuizServlet extends HttpServlet {
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
        if (attempt.isEmpty() || !"IN_PROGRESS".equals(attempt.get().status())) {
            response.sendRedirect(request.getContextPath() + "/quiz/config");
            return;
        }

        int pageCount = (int) Math.ceil(attempt.get().totalQuestions() / (double) attempt.get().questionsPerPage());
        int page = clamp(parseInt(request.getParameter("page"), 1), 1, pageCount);
        List<Question> questions = quizDao.findQuestionsForPage(attemptId, page, attempt.get().questionsPerPage());

        request.setAttribute("attempt", attempt.get());
        request.setAttribute("questions", questions);
        request.setAttribute("page", page);
        request.setAttribute("pageCount", pageCount);
        request.getRequestDispatcher("/WEB-INF/views/quiz.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        User user = (User) request.getSession().getAttribute("user");
        Long attemptId = (Long) request.getSession().getAttribute("attemptId");
        if (attemptId == null) {
            response.sendRedirect(request.getContextPath() + "/quiz/config");
            return;
        }

        Optional<Attempt> attempt = quizDao.findAttempt(attemptId, user.id());
        if (attempt.isEmpty() || !"IN_PROGRESS".equals(attempt.get().status())) {
            response.sendRedirect(request.getContextPath() + "/quiz/config");
            return;
        }

        int pageCount = (int) Math.ceil(attempt.get().totalQuestions() / (double) attempt.get().questionsPerPage());
        int page = clamp(parseInt(request.getParameter("page"), 1), 1, pageCount);
        List<Question> questions = quizDao.findQuestionsForPage(attemptId, page, attempt.get().questionsPerPage());

        for (Question question : questions) {
            String answerValue = request.getParameter("answer_" + question.id());
            if (answerValue == null || answerValue.isBlank()) {
                showPageWithError(request, response, attempt.get(), questions, page, pageCount, "Please answer every question on this page.");
                return;
            }
            try {
                quizDao.saveAnswer(attemptId, question.id(), Long.parseLong(answerValue));
            } catch (IllegalArgumentException e) {
                showPageWithError(request, response, attempt.get(), questions, page, pageCount, "One selected answer is not valid.");
                return;
            }
        }

        String action = request.getParameter("action");
        if ("finish".equals(action)) {
            int answered = quizDao.countAnsweredQuestions(attemptId);
            if (answered < attempt.get().totalQuestions()) {
                showPageWithError(request, response, attempt.get(), questions, page, pageCount,
                    "You must answer all questions before finishing the test.");
                return;
            }
            quizDao.finishAttempt(attemptId);
            response.sendRedirect(request.getContextPath() + "/quiz/result");
            return;
        }

        response.sendRedirect(request.getContextPath() + "/quiz?page=" + Math.min(page + 1, pageCount));
    }

    private void showPageWithError(HttpServletRequest request, HttpServletResponse response, Attempt attempt,
                                   List<Question> questions, int page, int pageCount, String error)
        throws ServletException, IOException {
        request.setAttribute("attempt", attempt);
        request.setAttribute("questions", questions);
        request.setAttribute("page", page);
        request.setAttribute("pageCount", pageCount);
        request.setAttribute("error", error);
        request.getRequestDispatcher("/WEB-INF/views/quiz.jsp").forward(request, response);
    }

    private int parseInt(String value, int fallback) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            return fallback;
        }
    }

    private int clamp(int value, int min, int max) {
        return Math.max(min, Math.min(value, max));
    }
}
