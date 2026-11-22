package com.example.quiz.model;

public record Attempt(long id, int totalQuestions, int questionsPerPage, int correctCount, int wrongCount, String status) {
}
