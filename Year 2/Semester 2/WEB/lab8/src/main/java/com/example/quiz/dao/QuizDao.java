package com.example.quiz.dao;

import com.example.quiz.config.Database;
import com.example.quiz.model.Answer;
import com.example.quiz.model.Attempt;
import com.example.quiz.model.BestResult;
import com.example.quiz.model.Question;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class QuizDao {
    public int countQuestions() {
        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement("SELECT COUNT(*) FROM questions");
             ResultSet resultSet = statement.executeQuery()) {
            resultSet.next();
            return resultSet.getInt(1);
        } catch (SQLException e) {
            throw new IllegalStateException("Could not count questions", e);
        }
    }

    public long createAttempt(long userId, int totalQuestions, int questionsPerPage) {
        String attemptSql = """
            INSERT INTO quiz_attempts (user_id, total_questions, questions_per_page)
            VALUES (?, ?, ?)
            """;
        String questionSql = "SELECT id FROM questions ORDER BY RAND() LIMIT ?";
        String attemptQuestionSql = """
            INSERT INTO attempt_questions (attempt_id, question_id, position)
            VALUES (?, ?, ?)
            """;

        try (Connection connection = Database.getConnection()) {
            connection.setAutoCommit(false);
            try (PreparedStatement attemptStatement = connection.prepareStatement(attemptSql, Statement.RETURN_GENERATED_KEYS)) {
                attemptStatement.setLong(1, userId);
                attemptStatement.setInt(2, totalQuestions);
                attemptStatement.setInt(3, questionsPerPage);
                attemptStatement.executeUpdate();

                long attemptId;
                try (ResultSet generatedKeys = attemptStatement.getGeneratedKeys()) {
                    generatedKeys.next();
                    attemptId = generatedKeys.getLong(1);
                }

                try (PreparedStatement questionStatement = connection.prepareStatement(questionSql);
                     PreparedStatement attemptQuestionStatement = connection.prepareStatement(attemptQuestionSql)) {
                    questionStatement.setInt(1, totalQuestions);
                    try (ResultSet resultSet = questionStatement.executeQuery()) {
                        int position = 1;
                        while (resultSet.next()) {
                            attemptQuestionStatement.setLong(1, attemptId);
                            attemptQuestionStatement.setLong(2, resultSet.getLong("id"));
                            attemptQuestionStatement.setInt(3, position++);
                            attemptQuestionStatement.addBatch();
                        }
                    }
                    attemptQuestionStatement.executeBatch();
                }

                connection.commit();
                return attemptId;
            } catch (SQLException e) {
                connection.rollback();
                throw e;
            } finally {
                connection.setAutoCommit(true);
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Could not create quiz attempt", e);
        }
    }

    public Optional<Attempt> findAttempt(long attemptId, long userId) {
        String sql = """
            SELECT id, total_questions, questions_per_page, correct_count, wrong_count, status
            FROM quiz_attempts
            WHERE id = ? AND user_id = ?
            """;
        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setLong(1, attemptId);
            statement.setLong(2, userId);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return Optional.of(new Attempt(
                        resultSet.getLong("id"),
                        resultSet.getInt("total_questions"),
                        resultSet.getInt("questions_per_page"),
                        resultSet.getInt("correct_count"),
                        resultSet.getInt("wrong_count"),
                        resultSet.getString("status")
                    ));
                }
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Could not load quiz attempt", e);
        }
        return Optional.empty();
    }

    public List<Question> findQuestionsForPage(long attemptId, int page, int pageSize) {
        int offset = (page - 1) * pageSize;
        String questionSql = """
            SELECT q.id, q.text, aa.answer_id AS selected_answer_id
            FROM attempt_questions aq
            JOIN questions q ON q.id = aq.question_id
            LEFT JOIN attempt_answers aa ON aa.attempt_id = aq.attempt_id AND aa.question_id = q.id
            WHERE aq.attempt_id = ?
            ORDER BY aq.position
            LIMIT ? OFFSET ?
            """;
        String answerSql = """
            SELECT id, question_id, text
            FROM answers
            WHERE question_id IN (%s)
            ORDER BY id
            """;

        try (Connection connection = Database.getConnection();
             PreparedStatement questionStatement = connection.prepareStatement(questionSql)) {
            questionStatement.setLong(1, attemptId);
            questionStatement.setInt(2, pageSize);
            questionStatement.setInt(3, offset);

            List<QuestionRow> rows = new ArrayList<>();
            try (ResultSet resultSet = questionStatement.executeQuery()) {
                while (resultSet.next()) {
                    Long selectedAnswerId = resultSet.getObject("selected_answer_id") == null
                        ? null
                        : resultSet.getLong("selected_answer_id");
                    rows.add(new QuestionRow(resultSet.getLong("id"), resultSet.getString("text"), selectedAnswerId));
                }
            }
            if (rows.isEmpty()) {
                return List.of();
            }

            String placeholders = String.join(",", rows.stream().map(row -> "?").toList());
            Map<Long, List<Answer>> answersByQuestion = new HashMap<>();
            try (PreparedStatement answerStatement = connection.prepareStatement(answerSql.formatted(placeholders))) {
                for (int i = 0; i < rows.size(); i++) {
                    answerStatement.setLong(i + 1, rows.get(i).id());
                }
                try (ResultSet resultSet = answerStatement.executeQuery()) {
                    while (resultSet.next()) {
                        long questionId = resultSet.getLong("question_id");
                        answersByQuestion
                            .computeIfAbsent(questionId, ignored -> new ArrayList<>())
                            .add(new Answer(resultSet.getLong("id"), questionId, resultSet.getString("text")));
                    }
                }
            }

            return rows.stream()
                .map(row -> new Question(
                    row.id(),
                    row.text(),
                    answersByQuestion.getOrDefault(row.id(), List.of()),
                    row.selectedAnswerId()
                ))
                .toList();
        } catch (SQLException e) {
            throw new IllegalStateException("Could not load quiz questions", e);
        }
    }

    public void saveAnswer(long attemptId, long questionId, long answerId) {
        String ownershipSql = """
            SELECT COUNT(*)
            FROM attempt_questions aq
            JOIN answers a ON a.question_id = aq.question_id
            WHERE aq.attempt_id = ? AND aq.question_id = ? AND a.id = ?
            """;
        String saveSql = """
            MERGE INTO attempt_answers (attempt_id, question_id, answer_id) KEY(attempt_id, question_id)
            VALUES (?, ?, ?)
            """;

        try (Connection connection = Database.getConnection();
             PreparedStatement ownershipStatement = connection.prepareStatement(ownershipSql)) {
            ownershipStatement.setLong(1, attemptId);
            ownershipStatement.setLong(2, questionId);
            ownershipStatement.setLong(3, answerId);
            try (ResultSet resultSet = ownershipStatement.executeQuery()) {
                resultSet.next();
                if (resultSet.getInt(1) == 0) {
                    throw new IllegalArgumentException("Selected answer does not belong to this question.");
                }
            }

            try (PreparedStatement saveStatement = connection.prepareStatement(saveSql)) {
                saveStatement.setLong(1, attemptId);
                saveStatement.setLong(2, questionId);
                saveStatement.setLong(3, answerId);
                saveStatement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Could not save answer", e);
        }
    }

    public int countAnsweredQuestions(long attemptId) {
        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement("SELECT COUNT(*) FROM attempt_answers WHERE attempt_id = ?")) {
            statement.setLong(1, attemptId);
            try (ResultSet resultSet = statement.executeQuery()) {
                resultSet.next();
                return resultSet.getInt(1);
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Could not count saved answers", e);
        }
    }

    public void finishAttempt(long attemptId) {
        String scoreSql = """
            SELECT
                SUM(CASE WHEN a.correct THEN 1 ELSE 0 END) AS correct_count,
                SUM(CASE WHEN a.correct THEN 0 ELSE 1 END) AS wrong_count
            FROM attempt_answers aa
            JOIN answers a ON a.id = aa.answer_id
            WHERE aa.attempt_id = ?
            """;
        String updateSql = """
            UPDATE quiz_attempts
            SET correct_count = ?, wrong_count = ?, status = 'COMPLETED', completed_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """;

        try (Connection connection = Database.getConnection();
             PreparedStatement scoreStatement = connection.prepareStatement(scoreSql);
             PreparedStatement updateStatement = connection.prepareStatement(updateSql)) {
            scoreStatement.setLong(1, attemptId);
            int correct;
            int wrong;
            try (ResultSet resultSet = scoreStatement.executeQuery()) {
                resultSet.next();
                correct = resultSet.getInt("correct_count");
                wrong = resultSet.getInt("wrong_count");
            }
            updateStatement.setInt(1, correct);
            updateStatement.setInt(2, wrong);
            updateStatement.setLong(3, attemptId);
            updateStatement.executeUpdate();
        } catch (SQLException e) {
            throw new IllegalStateException("Could not finish quiz attempt", e);
        }
    }

    public Optional<BestResult> findBestResult(long userId) {
        String sql = """
            SELECT correct_count, wrong_count, total_questions
            FROM quiz_attempts
            WHERE user_id = ? AND status = 'COMPLETED'
            ORDER BY (correct_count * 1.0 / total_questions) DESC, correct_count DESC, completed_at ASC
            LIMIT 1
            """;
        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setLong(1, userId);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return Optional.of(new BestResult(
                        resultSet.getInt("correct_count"),
                        resultSet.getInt("wrong_count"),
                        resultSet.getInt("total_questions")
                    ));
                }
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Could not load best result", e);
        }
        return Optional.empty();
    }

    private record QuestionRow(long id, String text, Long selectedAnswerId) {
    }
}
