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
    <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post" class="update_form">
        <input readonly id="id" type="text" name="update_id" placeholder="id" >
        <input id="user_id" type="text" name="update_user_id" placeholder="user_id">
        <input id="room_id" type="text" name="update_room_id" placeholder="room_id">
        <input id="start" type="text" name="update_start" placeholder="start">
        <input id="end" type="text" name="update_end" placeholder="end">

        <input id="update" type="submit" name="update" value="Update reservation">
    </form>
</section>

<section>
    <br>
    <table id="update_table">
        <thead>
        <th>ID</th>
        <th>User ID</th>
        <th>Room ID</th>
        <th>Start</th>
        <th>End</th>
        </thead>
        <tbody>

        <?php getAllReservationsUpdate(); ?>

        </tbody>
    </table>
</section>


<!-- <button class='btnUpdate' id='edit' name='edit' type='button' value= ". $row['id'] . " onclick=\"location.href='./update.php'\">Update</button> -->
</body>

</html>
