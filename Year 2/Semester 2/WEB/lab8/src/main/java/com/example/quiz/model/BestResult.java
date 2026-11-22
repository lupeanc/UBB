package com.example.quiz.model;

public record BestResult(int correctCount, int wrongCount, int totalQuestions) {
    public double percentage() {
        return totalQuestions == 0 ? 0 : (correctCount * 100.0) / totalQuestions;
    }
}
