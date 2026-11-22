<%@ page import="com.example.quiz.model.Answer" %>
<%@ page import="com.example.quiz.model.Attempt" %>
<%@ page import="com.example.quiz.model.Question" %>
<%@ page import="com.example.quiz.model.User" %>
<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    User user = (User) session.getAttribute("user");
    Attempt attempt = (Attempt) request.getAttribute("attempt");
    List<Question> questions = (List<Question>) request.getAttribute("questions");
    int currentPage = (Integer) request.getAttribute("page");
    int pageCount = (Integer) request.getAttribute("pageCount");
%>
<!doctype html>
<html>
<head>
    <title>Quiz</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/style.css">
</head>
<body>
<header class="topbar">
    <div>
        <strong>Quiz App</strong>
        <span class="muted">Signed in as <%= user.username() %></span>
    </div>
    <form method="post" action="${pageContext.request.contextPath}/logout"
          onsubmit="return confirm('Log out and discard this session?');">
        <button class="secondary" type="submit">Log out</button>
    </form>
</header>

<main class="page">
    <form method="post" action="${pageContext.request.contextPath}/quiz" class="quiz-form">
        <input type="hidden" name="page" value="<%= currentPage %>">
        <div class="quiz-head">
            <div>
                <h1>Page <%= currentPage %> of <%= pageCount %></h1>
                <p class="muted"><%= attempt.totalQuestions() %> questions total, <%= attempt.questionsPerPage() %> per page.</p>
            </div>
            <a class="link-button" href="${pageContext.request.contextPath}/quiz/config"
               onclick="return confirm('Cancel this quiz and configure a new one?');">Cancel</a>
        </div>

        <% if (request.getAttribute("error") != null) { %>
            <div class="alert"><%= request.getAttribute("error") %></div>
        <% } %>

        <% for (Question question : questions) { %>
            <section class="question-block">
                <h2><%= question.text() %></h2>
                <div class="answers">
                    <% for (Answer answer : question.answers()) { %>
                        <label class="answer-option">
                            <input type="radio"
                                   name="answer_<%= question.id() %>"
                                   value="<%= answer.id() %>"
                                   <%= question.selectedAnswerId() != null && question.selectedAnswerId() == answer.id() ? "checked" : "" %>
                                   required>
                            <span><%= answer.text() %></span>
                        </label>
                    <% } %>
                </div>
            </section>
        <% } %>

        <div class="actions">
            <% if (currentPage > 1) { %>
                <a class="link-button" href="${pageContext.request.contextPath}/quiz?page=<%= currentPage - 1 %>">Previous</a>
            <% } %>
            <% if (currentPage < pageCount) { %>
                <button type="submit" name="action" value="next">Save and continue</button>
            <% } else { %>
                <button type="submit" name="action" value="finish"
                        onclick="return confirm('Submit this quiz and view your result?');">Finish quiz</button>
            <% } %>
        </div>
    </form>
</main>
</body>
</html>
