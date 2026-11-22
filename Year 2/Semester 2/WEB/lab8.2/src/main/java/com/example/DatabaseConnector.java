package com.example;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.LinkedHashMap;
import java.util.Map;

public class DatabaseConnector {
    private Connection connection;

    public DatabaseConnector() {
        try {
            this.connection = DBConnection.initializeDB();
        } catch (SQLException | ClassNotFoundException ex) {
            ex.printStackTrace();
        }
    }

    public int getUserId(String username, String password) {
        int userId = 0;
        String hashedPassword = sha256(password);

        try {
            PreparedStatement statement = connection.prepareStatement(
                    "SELECT id FROM users WHERE username = ? AND (password_hash = ? OR password_hash = ?)"
            );
            statement.setString(1, username);
            statement.setString(2, hashedPassword);
            statement.setString(3, password);

            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                userId = resultSet.getInt("id");
            }
            resultSet.close();
            statement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return userId;
    }

    public String getQuizOptionsHtml() {
        StringBuilder result = new StringBuilder();

        try {
            PreparedStatement statement = connection.prepareStatement("SELECT id, title FROM quizzes ORDER BY title");
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                result.append("<option value='")
                        .append(resultSet.getInt("id"))
                        .append("'>")
                        .append(escape(resultSet.getString("title")))
                        .append("</option>");
            }

            resultSet.close();
            statement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return result.toString();
    }

    public int getQuestionCount(int quizId) {
        int count = 0;

        try {
            PreparedStatement statement = connection.prepareStatement("SELECT COUNT(*) FROM questions WHERE quiz_id = ?");
            statement.setInt(1, quizId);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                count = resultSet.getInt(1);
            }
            resultSet.close();
            statement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return count;
    }

    public int createAttempt(int userId, int quizId, int totalQuestions, int questionsPerPage) {
        int attemptId = 0;

        try {
            PreparedStatement statement = connection.prepareStatement(
                    "INSERT INTO attempts(user_id, quiz_id, total_questions, questions_per_page) VALUES (?, ?, ?, ?)",
                    Statement.RETURN_GENERATED_KEYS
            );
            statement.setInt(1, userId);
            statement.setInt(2, quizId);
            statement.setInt(3, totalQuestions);
            statement.setInt(4, questionsPerPage);
            statement.executeUpdate();

            ResultSet keys = statement.getGeneratedKeys();
            if (keys.next()) {
                attemptId = keys.getInt(1);
            }
            keys.close();
            statement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return attemptId;
    }

    public Map<Integer, Integer> readSubmittedAnswers(Map<String, String[]> parameters) {
        Map<Integer, Integer> answers = new LinkedHashMap<>();

        for (String key : parameters.keySet()) {
            if (key.startsWith("question_")) {
                int questionId = Integer.parseInt(key.substring("question_".length()));
                int answerId = Integer.parseInt(parameters.get(key)[0]);
                answers.put(questionId, answerId);
            }
        }

        return answers;
    }

    public void saveAnswers(int attemptId, Map<Integer, Integer> answers) {
        try {
            for (Integer questionId : answers.keySet()) {
                PreparedStatement statement = connection.prepareStatement(
                        "INSERT INTO attempt_answers(attempt_id, question_id, answer_id) VALUES (?, ?, ?) " +
                                "ON DUPLICATE KEY UPDATE answer_id = VALUES(answer_id), answered_at = CURRENT_TIMESTAMP"
                );
                statement.setInt(1, attemptId);
                statement.setInt(2, questionId);
                statement.setInt(3, answers.get(questionId));
                statement.executeUpdate();
                statement.close();
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    public void finishAttempt(int attemptId) {
        try {
            PreparedStatement statement = connection.prepareStatement(
                    "UPDATE attempts SET status = 'FINISHED', finished_at = CURRENT_TIMESTAMP WHERE id = ?"
            );
            statement.setInt(1, attemptId);
            statement.executeUpdate();
            statement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    public int getPageCount(int attemptId) {
        int pageCount = 1;

        try {
            PreparedStatement statement = connection.prepareStatement(
                    "SELECT CEIL(total_questions / questions_per_page) FROM attempts WHERE id = ?"
            );
            statement.setInt(1, attemptId);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                pageCount = resultSet.getInt(1);
            }
            resultSet.close();
            statement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return pageCount;
    }

    public String getQuizPageHtml(int attemptId, int page) {
        StringBuilder result = new StringBuilder();
        int quizId = 0;
        int totalQuestions = 0;
        int questionsPerPage = 0;

        try {
            PreparedStatement attemptStatement = connection.prepareStatement(
                    "SELECT quiz_id, total_questions, questions_per_page FROM attempts WHERE id = ?"
            );
            attemptStatement.setInt(1, attemptId);
            ResultSet attemptSet = attemptStatement.executeQuery();
            if (attemptSet.next()) {
                quizId = attemptSet.getInt("quiz_id");
                totalQuestions = attemptSet.getInt("total_questions");
                questionsPerPage = attemptSet.getInt("questions_per_page");
            }
            attemptSet.close();
            attemptStatement.close();

            int pageCount = (int) Math.ceil((double) totalQuestions / questionsPerPage);
            int offset = (page - 1) * questionsPerPage;
            int limit = Math.min(questionsPerPage, totalQuestions - offset);

            result.append("<form action='controller' method='post' class='quiz-form'>");
            result.append("<input type='hidden' name='action' value='").append(page == pageCount ? "finish" : "answer").append("'>");
            result.append("<input type='hidden' name='next_page' value='").append(page + 1).append("'>");
            result.append("<p class='muted'>Page ").append(page).append(" of ").append(pageCount).append("</p>");

            PreparedStatement questionStatement = connection.prepareStatement(
                    "SELECT id, text FROM questions WHERE quiz_id = ? ORDER BY position LIMIT ? OFFSET ?"
            );
            questionStatement.setInt(1, quizId);
            questionStatement.setInt(2, limit);
            questionStatement.setInt(3, offset);
            ResultSet questionSet = questionStatement.executeQuery();

            while (questionSet.next()) {
                int questionId = questionSet.getInt("id");
                result.append("<section class='question'>");
                result.append("<h2>").append(escape(questionSet.getString("text"))).append("</h2>");
                result.append(getAnswersHtml(attemptId, questionId));
                result.append("</section>");
            }

            questionSet.close();
            questionStatement.close();
            result.append("<input type='submit' value='").append(page == pageCount ? "Finish test" : "Next page").append("'>");
            result.append("</form>");
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return result.toString();
    }

    private String getAnswersHtml(int attemptId, int questionId) throws SQLException {
        StringBuilder result = new StringBuilder();
        int selectedAnswerId = getSelectedAnswerId(attemptId, questionId);

        PreparedStatement answerStatement = connection.prepareStatement(
                "SELECT id, text FROM answers WHERE question_id = ? ORDER BY position"
        );
        answerStatement.setInt(1, questionId);
        ResultSet answerSet = answerStatement.executeQuery();

        while (answerSet.next()) {
            int answerId = answerSet.getInt("id");
            result.append("<label class='answer'>");
            result.append("<input type='radio' required name='question_").append(questionId).append("' value='").append(answerId).append("'");
            if (answerId == selectedAnswerId) {
                result.append(" checked");
            }
            result.append(">");
            result.append(escape(answerSet.getString("text")));
            result.append("</label>");
        }

        answerSet.close();
        answerStatement.close();
        return result.toString();
    }

    private int getSelectedAnswerId(int attemptId, int questionId) throws SQLException {
        int answerId = 0;
        PreparedStatement statement = connection.prepareStatement(
                "SELECT answer_id FROM attempt_answers WHERE attempt_id = ? AND question_id = ?"
        );
        statement.setInt(1, attemptId);
        statement.setInt(2, questionId);
        ResultSet resultSet = statement.executeQuery();
        if (resultSet.next()) {
            answerId = resultSet.getInt("answer_id");
        }
        resultSet.close();
        statement.close();
        return answerId;
    }

    public String getResultHtml(int attemptId, int userId) {
        int correct = 0;
        int wrong = 0;
        int best = 0;

        try {
            PreparedStatement resultStatement = connection.prepareStatement(
                    "SELECT SUM(a.is_correct = TRUE) AS correct_answers, SUM(a.is_correct = FALSE) AS wrong_answers " +
                            "FROM attempt_answers aa INNER JOIN answers a ON aa.answer_id = a.id WHERE aa.attempt_id = ?"
            );
            resultStatement.setInt(1, attemptId);
            ResultSet resultSet = resultStatement.executeQuery();
            if (resultSet.next()) {
                correct = resultSet.getInt("correct_answers");
                wrong = resultSet.getInt("wrong_answers");
            }
            resultSet.close();
            resultStatement.close();

            PreparedStatement bestStatement = connection.prepareStatement(
                    "SELECT MAX(score) FROM (" +
                            "SELECT attempts.id, SUM(answers.is_correct = TRUE) AS score " +
                            "FROM attempts " +
                            "INNER JOIN attempt_answers ON attempts.id = attempt_answers.attempt_id " +
                            "INNER JOIN answers ON attempt_answers.answer_id = answers.id " +
                            "WHERE attempts.user_id = ? AND attempts.status = 'FINISHED' " +
                            "GROUP BY attempts.id" +
                            ") scores"
            );
            bestStatement.setInt(1, userId);
            ResultSet bestSet = bestStatement.executeQuery();
            if (bestSet.next()) {
                best = bestSet.getInt(1);
            }
            bestSet.close();
            bestStatement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return "<div class='result'>" +
                "<p>Correct answers: <strong>" + correct + "</strong></p>" +
                "<p>Wrong answers: <strong>" + wrong + "</strong></p>" +
                "<p>Your all time best result: <strong>" + best + "</strong></p>" +
                "</div>";
    }

    private String sha256(String value) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(value.getBytes(StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder();
            for (byte b : hash) {
                hex.append(String.format("%02x", b));
            }
            return hex.toString();
        } catch (NoSuchAlgorithmException ex) {
            throw new RuntimeException(ex);
        }
    }

    private String escape(String value) {
        if (value == null) {
            return "";
        }
        return value.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\"", "&quot;")
                .replace("'", "&#39;");
    }
}
