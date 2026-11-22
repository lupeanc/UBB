package com.example.quiz.model;

import java.util.List;

public record Question(long id, String text, List<Answer> answers, Long selectedAnswerId) {
}
