<?php
require_once 'functions.php';

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Reservation</title>
    <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <link rel="stylesheet" type="text/css" href="./style.css">
    <script type="text/javascript" src="./script.js"></script>
</head>

<body>
<button class="home" type="button" onclick="location.href='index.html'">HOME </button>
<br>

<section>
    <br>
    <table id="delete_table">
        <thead>
        <th>ID</th>
        <th>User ID</th>
        <th>Room ID</th>
        <th>Start</th>
        <th>End</th>
        </thead>
        <tbody>

        <?php getAllReservationsDelete(); ?>

        </tbody>
    </table>
</section>


<!-- <button class='btnUpdate' id='edit' name='edit' type='button' value= ". $row['id'] . " onclick=\"location.href='./update.php'\">Update</button> -->
</body>

</html>
