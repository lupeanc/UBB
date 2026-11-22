<%@ page import="com.example.DatabaseConnector" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    String isLoggedIn = (String) session.getAttribute("login");
    if (isLoggedIn == null || !isLoggedIn.equals("true")) {
        response.sendRedirect("loginError.html");
        return;
    }

    DatabaseConnector db = new DatabaseConnector();
    String error = (String) session.getAttribute("error");
    session.removeAttribute("error");
%>
<html>
<head>
    <title>Quiz setup</title>
    <script src="quiz.js" defer></script>
</head>
<body>
<div class="top-bar">
    <p>Hello <%= session.getAttribute("username") %>!</p>
    <form action="logout" method="post">
        <input type="submit" value="Logout">
    </form>
</div>

<main>
    <h1>Quiz setup</h1>

    <% if (error != null) { %>
        <p class="error"><%= error %></p>
    <% } %>

    <form action="controller" method="post" class="setup-form">
        <input type="hidden" name="action" value="start">

        <label>Quiz</label>
        <select name="quiz_id" required>
            <option value="">Choose quiz</option>
            <%= db.getQuizOptionsHtml() %>
        </select>

        <label>Number of questions in test</label>
        <input type="number" name="total_questions" min="1" required>

        <label>Questions per page</label>
        <input type="number" name="questions_per_page" min="1" required>

        <input type="submit" value="Start test">
    </form>
</main>
</body>
</html>
