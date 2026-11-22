package com.example.quiz.dao;

import com.example.quiz.config.Database;
import com.example.quiz.model.User;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Optional;

public class UserDao {
    public Optional<User> findByCredentials(String username, String password) {
        String sql = "SELECT id, username FROM users WHERE username = ? AND password = ?";
        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, username);
            statement.setString(2, password);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return Optional.of(new User(resultSet.getLong("id"), resultSet.getString("username")));
                }
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Could not check user credentials", e);
        }
        return Optional.empty();
    }
}
