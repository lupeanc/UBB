<%@ page import="com.example.DatabaseConnector" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    String isLoggedIn = (String) session.getAttribute("login");
    if (isLoggedIn == null || !isLoggedIn.equals("true")) {
        response.sendRedirect("loginError.html");
        return;
    }

    Integer attemptId = (Integer) session.getAttribute("attemptID");
    Integer userId = (Integer) session.getAttribute("userID");
    if (attemptId == null || userId == null) {
        response.sendRedirect("quizSetup.jsp");
        return;
    }

    DatabaseConnector db = new DatabaseConnector();
%>
<html>
<head>
    <title>Quiz result</title>
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
    <h1>Result</h1>
    <%= db.getResultHtml(attemptId, userId) %>

    <form action="quizSetup.jsp" method="get" class="inline-form">
        <input type="submit" value="Start another test">
    </form>
</main>
</body>
</html>
