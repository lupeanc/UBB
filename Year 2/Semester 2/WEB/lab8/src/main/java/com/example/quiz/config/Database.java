package com.example.quiz.config;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public final class Database {
    private static final String JDBC_URL = "jdbc:h2:~/quizapp-db";
    private static final String USER = "sa";
    private static final String PASSWORD = "";

    private Database() {
    }

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(JDBC_URL, USER, PASSWORD);
    }

    public static void init() {
        try {
            Class.forName("org.h2.Driver");
            try (Connection connection = getConnection(); Statement statement = connection.createStatement()) {
                statement.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id IDENTITY PRIMARY KEY,
                        username VARCHAR(80) NOT NULL UNIQUE,
                        password VARCHAR(120) NOT NULL
                    )
                    """);
                statement.execute("""
                    CREATE TABLE IF NOT EXISTS questions (
                        id IDENTITY PRIMARY KEY,
                        text VARCHAR(500) NOT NULL
                    )
                    """);
                statement.execute("""
                    CREATE TABLE IF NOT EXISTS answers (
                        id IDENTITY PRIMARY KEY,
                        question_id BIGINT NOT NULL,
                        text VARCHAR(300) NOT NULL,
                        correct BOOLEAN NOT NULL,
                        CONSTRAINT fk_answers_questions FOREIGN KEY (question_id) REFERENCES questions(id)
                    )
                    """);
                statement.execute("""
                    CREATE TABLE IF NOT EXISTS quiz_attempts (
                        id IDENTITY PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        total_questions INT NOT NULL,
                        questions_per_page INT NOT NULL,
                        correct_count INT DEFAULT 0 NOT NULL,
                        wrong_count INT DEFAULT 0 NOT NULL,
                        status VARCHAR(20) DEFAULT 'IN_PROGRESS' NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        completed_at TIMESTAMP,
                        CONSTRAINT fk_attempts_users FOREIGN KEY (user_id) REFERENCES users(id)
                    )
                    """);
                statement.execute("""
                    CREATE TABLE IF NOT EXISTS attempt_questions (
                        attempt_id BIGINT NOT NULL,
                        question_id BIGINT NOT NULL,
                        position INT NOT NULL,
                        PRIMARY KEY (attempt_id, question_id),
                        CONSTRAINT fk_attempt_questions_attempt FOREIGN KEY (attempt_id) REFERENCES quiz_attempts(id),
                        CONSTRAINT fk_attempt_questions_question FOREIGN KEY (question_id) REFERENCES questions(id)
                    )
                    """);
                statement.execute("""
                    CREATE TABLE IF NOT EXISTS attempt_answers (
                        attempt_id BIGINT NOT NULL,
                        question_id BIGINT NOT NULL,
                        answer_id BIGINT NOT NULL,
                        PRIMARY KEY (attempt_id, question_id),
                        CONSTRAINT fk_attempt_answers_attempt FOREIGN KEY (attempt_id) REFERENCES quiz_attempts(id),
                        CONSTRAINT fk_attempt_answers_question FOREIGN KEY (question_id) REFERENCES questions(id),
                        CONSTRAINT fk_attempt_answers_answer FOREIGN KEY (answer_id) REFERENCES answers(id)
                    )
                    """);
                seed(statement);
            }
        } catch (ClassNotFoundException | SQLException e) {
            throw new IllegalStateException("Could not initialize quiz database", e);
        }
    }

    private static void seed(Statement statement) throws SQLException {
        statement.executeUpdate("""
            MERGE INTO users (username, password) KEY(username)
            VALUES ('student', 'student123'), ('admin', 'admin123')
            """);

        statement.executeUpdate("""
            MERGE INTO questions (id, text) KEY(id) VALUES
            (1, 'Which HTTP method is usually used to submit a form that changes server state?'),
            (2, 'What object is commonly used in servlets to store per-user login data?'),
            (3, 'Which SQL clause filters rows before grouping?'),
            (4, 'What does AJAX allow a web page to do?'),
            (5, 'Which JSP directive sets the page content type?'),
            (6, 'What status code means the request was successful?'),
            (7, 'Which Java interface can protect pages before a servlet is reached?'),
            (8, 'What is the main role of a DAO class?'),
            (9, 'Which database key uniquely identifies each row?'),
            (10, 'What should happen when a user logs out?'),
            (11, 'Which HTML control is best for one answer from many options?'),
            (12, 'Where should persistent quiz answers be saved between requests?')
            """);

        statement.executeUpdate("""
            MERGE INTO answers (id, question_id, text, correct) KEY(id) VALUES
            (1, 1, 'GET', FALSE), (2, 1, 'POST', TRUE), (3, 1, 'TRACE', FALSE), (4, 1, 'HEAD', FALSE),
            (5, 2, 'ServletContext', FALSE), (6, 2, 'HttpSession', TRUE), (7, 2, 'PrintWriter', FALSE), (8, 2, 'Cookie only', FALSE),
            (9, 3, 'ORDER BY', FALSE), (10, 3, 'WHERE', TRUE), (11, 3, 'HAVING', FALSE), (12, 3, 'LIMIT', FALSE),
            (13, 4, 'Reload the entire browser window every second', FALSE), (14, 4, 'Exchange data with the server without a full page reload', TRUE), (15, 4, 'Compile Java into SQL', FALSE), (16, 4, 'Replace sessions', FALSE),
            (17, 5, 'include', FALSE), (18, 5, 'taglib', FALSE), (19, 5, 'page', TRUE), (20, 5, 'forward', FALSE),
            (21, 6, '200 OK', TRUE), (22, 6, '404 Not Found', FALSE), (23, 6, '500 Internal Server Error', FALSE), (24, 6, '302 Found', FALSE),
            (25, 7, 'Filter', TRUE), (26, 7, 'ResultSet', FALSE), (27, 7, 'DriverManager', FALSE), (28, 7, 'JspWriter', FALSE),
            (29, 8, 'Render CSS animations', FALSE), (30, 8, 'Centralize database access logic', TRUE), (31, 8, 'Replace the web container', FALSE), (32, 8, 'Store passwords in HTML', FALSE),
            (33, 9, 'Foreign key', FALSE), (34, 9, 'Primary key', TRUE), (35, 9, 'Check constraint', FALSE), (36, 9, 'Index hint', FALSE),
            (37, 10, 'Keep the session active forever', FALSE), (38, 10, 'Invalidate the current session', TRUE), (39, 10, 'Delete all questions', FALSE), (40, 10, 'Disable CSS', FALSE),
            (41, 11, 'Radio buttons', TRUE), (42, 11, 'Text area', FALSE), (43, 11, 'Password input', FALSE), (44, 11, 'File upload', FALSE),
            (45, 12, 'Only in hidden HTML inputs', FALSE), (46, 12, 'In the database', TRUE), (47, 12, 'Only in JavaScript variables', FALSE), (48, 12, 'In CSS classes', FALSE)
            """);
    }
}
