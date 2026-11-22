<%@ page import="com.example.quiz.model.Attempt" %>
<%@ page import="com.example.quiz.model.BestResult" %>
<%@ page import="com.example.quiz.model.User" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    User user = (User) session.getAttribute("user");
    Attempt attempt = (Attempt) request.getAttribute("attempt");
    BestResult bestResult = (BestResult) request.getAttribute("bestResult");
%>
<!doctype html>
<html>
<head>
    <title>Quiz Result</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/style.css">
</head>
<body>
<header class="topbar">
    <div>
        <strong>Quiz App</strong>
        <span class="muted">Signed in as <%= user.username() %></span>
    </div>
    <form method="post" action="${pageContext.request.contextPath}/logout"
          onsubmit="return confirm('Log out and end this session?');">
        <button class="secondary" type="submit">Log out</button>
    </form>
</header>

<main class="page">
    <section class="panel result-panel">
        <h1>Your result</h1>
        <div class="score-grid">
            <div>
                <span class="score-number"><%= attempt.correctCount() %></span>
                <span class="score-label">Correct</span>
            </div>
            <div>
                <span class="score-number wrong"><%= attempt.wrongCount() %></span>
                <span class="score-label">Wrong</span>
            </div>
        </div>

        <% if (bestResult != null) { %>
            <p class="best">
                All-time best:
                <strong><%= bestResult.correctCount() %>/<%= bestResult.totalQuestions() %></strong>
                (<%= String.format("%.1f", bestResult.percentage()) %>%)
            </p>
        <% } %>

        <div class="actions">
            <a class="link-button" href="${pageContext.request.contextPath}/quiz/config">Take another quiz</a>
        </div>
    </section>
</main>
</body>
</html>
