<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!doctype html>
<html>
<head>
    <title>Login - Quiz App</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/style.css">
</head>
<body>
<main class="auth-shell">
    <section class="panel">
        <h1>Quiz App</h1>
        <p class="muted">Sign in to start a database-backed quiz test.</p>

        <% if (request.getAttribute("error") != null) { %>
            <div class="alert"><%= request.getAttribute("error") %></div>
        <% } %>

        <form method="post" action="${pageContext.request.contextPath}/login" class="form-grid">
            <label>
                Username
                <input type="text" name="username" minlength="3" required
                       value="<%= request.getAttribute("username") == null ? "" : request.getAttribute("username") %>">
            </label>
            <label>
                Password
                <input type="password" name="password" minlength="6" required>
            </label>
            <button type="submit">Log in</button>
        </form>

        <p class="hint">Demo users: <strong>student/student123</strong> or <strong>admin/admin123</strong></p>
    </section>
</main>
</body>
</html>
