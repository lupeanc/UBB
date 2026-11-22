window.addEventListener("DOMContentLoaded", function () {
    const logoutForms = document.querySelectorAll("form[action='logout']");

    logoutForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            if (!confirm("Are you sure you want to logout?")) {
                event.preventDefault();
            }
        });
    });
});
