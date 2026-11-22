<?php
require_once 'functions.php';
// gets the link set by the loadRooms() function
if (isset($_GET['ajax'])) {
    getAllReservationsFiltered();
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rooms Browser</title>
    <script type="text/javascript" src="browse.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

<button class="home" type="button" onclick="location.href='./index.html'">HOME </button>

</div>

<div id="main">
    <h1> Rooms </h1>

    <select id="category">
        <option value="">All Categories</option>
        <option value="luxury">Luxury</option>
        <option value="standard">Standard</option>
    </select>

    <input type="number" id="beds" placeholder="Min beds">
    <input type="number" id="price" placeholder="Max price">

    <button onclick="loadRooms()">Filter</button>

    <div id="rooms"></div>

    <button id="prev" onclick="prevPage()">Previous</button>
    <button id="next" onclick="nextPage()">Next</button>

</div>
</body>
</html>
