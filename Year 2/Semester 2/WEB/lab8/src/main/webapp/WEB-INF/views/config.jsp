<%@ page import="com.example.quiz.model.User" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    User user = (User) session.getAttribute("user");
    int availableQuestions = (Integer) request.getAttribute("availableQuestions");
    Object totalQuestions = request.getAttribute("totalQuestions");
    Object questionsPerPage = request.getAttribute("questionsPerPage");
%>
<!doctype html>
<html>
<head>
    <title>Configure Quiz</title>
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
    <section class="panel">
        <h1>Configure your test</h1>
        <p class="muted">There are <%= availableQuestions %> questions available in the database.</p>

        <% if (request.getAttribute("error") != null) { %>
            <div class="alert"><%= request.getAttribute("error") %></div>
        <% } %>

        <form method="post" action="${pageContext.request.contextPath}/quiz/config" class="form-grid">
            <label>
                Number of questions in the test
                <input type="number" name="totalQuestions" min="1" max="<%= availableQuestions %>" required
                       value="<%= totalQuestions == null ? Math.min(5, availableQuestions) : totalQuestions %>">
            </label>
            <label>
                Questions per page
                <input type="number" name="questionsPerPage" min="1" max="<%= availableQuestions %>" required
                       value="<%= questionsPerPage == null ? 2 : questionsPerPage %>">
            </label>
            <button type="submit">Start quiz</button>
        </form>
    </section>
</main>
</body>
</html>
