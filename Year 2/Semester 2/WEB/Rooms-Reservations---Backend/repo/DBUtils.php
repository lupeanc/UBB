<?php

namespace repo;

use PDO;
use PDOException;

class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";

    private $db = "web_lab5";

    private $charset = "utf8";

//    database access layer
    private $pdo;

    private $error;

//    private $conn;

    public function __construct () {
        $dsn = "mysql:host=$this->host;dbname=$this->db;charset=$this->charset";
        $opt = array(PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false);
        try {
            $this->pdo = new PDO($dsn, $this->user, $this->pass, $opt);
        } // Catch any errors
        catch(PDOException $e){
            $this->error = $e->getMessage();
            echo "Error connecting to DB: " . $this->error;
        }
//        $this->conn = mysqli_connect($this->host, $this->user, $this->pass, $this->db);
    }

    public function selectReservation($id){
        $stmt = $this->pdo->query("SELECT * FROM reservations where id='$id'");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function selectAllReservations(){
        $stmt = $this->pdo->query("SELECT * FROM reservations");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function selectRoom($id){
        $stmt = $this->pdo->query("SELECT * FROM rooms where id='$id'");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function selectAllRooms(){
        $stmt = $this->pdo->query("SELECT * FROM rooms");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    //nb_beds, categ, price
    public function getFilteredRoomsByNbBeds($nbBeds){
        $stmt = $this->pdo->query("SELECT * FROM rooms where nb_beds=$nbBeds");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getFilteredRoomsByCetegory($category){
        $stmt = $this->pdo->query("SELECT * FROM rooms where category='$category'");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getFilteredRoomsByPrice($price){
        $stmt = $this->pdo->query("SELECT * FROM rooms where price<=$price");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getNbBeds()
    {
        $stmt = $this->pdo->query("SELECT DISTINCT nb_beds FROM rooms");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getCategories(){
        $stmt = $this->pdo->query("SELECT DISTINCT category FROM rooms");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getPrices(){
        $stmt = $this->pdo->query("SELECT DISTINCT price FROM rooms");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

//    public function addReservation($user_id, $room_id, $start, $end)
//    {
//        $is_already_occupied = $this->pdo->query("SELECT COUNT(*) as cnt FROM reservations WHERE room_id='$room_id' AND ('$start' BETWEEN start AND end OR '$end' BETWEEN start AND end OR ('$start' < start AND '$end' > end))");
//        $row = $is_already_occupied->fetch(PDO::FETCH_ASSOC);
//        if($row['cnt']>0){
//            return 0;
//        }
//        $affected_rows = $this->pdo->exec("INSERT INTO Reservations (user_id, room_id, start, end) values ($user_id, $room_id, '$start', '$end')");
//        return $affected_rows;
//    }

    public function addReservation($user_id, $room_id, $start, $end)
    {
        $stmt = $this->pdo->prepare("
        SELECT COUNT(*) as cnt
        FROM Reservations
        WHERE room_id = ?
        AND (
            ? BETWEEN `start` AND `end`
            OR
            ? BETWEEN `start` AND `end`
            OR
            (? < `start` AND ? > `end`)
        )
    ");

        $stmt->execute([$room_id, $start, $end, $start, $end]);
        $row = $stmt->fetch(PDO::FETCH_ASSOC);

        if($row['cnt'] > 0){
            return 0;
        }

        $stmt = $this->pdo->prepare("
        INSERT INTO Reservations (user_id, room_id, `start`, `end`)
        VALUES (?, ?, ?, ?)
    ");

        $stmt->execute([$user_id, $room_id, $start, $end]);

        return $stmt->rowCount();
    }

    public function deleteReservation($id){
        $affected_rows = $this->pdo->query("DELETE FROM Reservations where id='$id'");
        return $affected_rows;
    }

//    public function updateReservation($id, $user_id, $room_id, $start, $end){
//        $is_already_occupied = $this->pdo->query("SELECT COUNT(*) as cnt FROM reservations WHERE room_id='$room_id' AND ('$start' BETWEEN start AND end OR '$end' BETWEEN start AND end OR ('$start' < start AND '$end' > end))");
//        $row = $is_already_occupied->fetch(PDO::FETCH_ASSOC);
//        if($row['cnt']>0){
//            return 0;
//        }
//
//        $affected_rows = $this->pdo->exec("UPDATE reservations SET user_id = $user_id, room_id = $room_id, start = '$start', end = '$end' WHERE id = '$id'");
//        return $affected_rows;
//    }

    public function updateReservation($id, $user_id, $room_id, $start, $end)
    {
        // this is sent first
        $stmt = $this->pdo->prepare("
        SELECT COUNT(*) as cnt
        FROM Reservations
        WHERE room_id = ?
        AND id != ?
        AND (
            ? BETWEEN `start` AND `end`
            OR
            ? BETWEEN `start` AND `end`
            OR
            (? < `start` AND ? > `end`)
        )
    ");

        // values are sent separately => they are sent as plain text
        // if i were to simply execute the query as i wrote it, the whole thing would
        // be considered code => someone could write "drop table ___" and t would be executed
        // now it is merely a string :)
        $stmt->execute([$room_id, $id, $start, $end, $start, $end]);
        $row = $stmt->fetch(PDO::FETCH_ASSOC);

        if($row['cnt'] > 0){
            return 0;
        }

        $stmt = $this->pdo->prepare("
        UPDATE Reservations
        SET user_id = ?, room_id = ?, `start` = ?, `end` = ?
        WHERE id = ?
    ");

        $stmt->execute([$user_id, $room_id, $start, $end, $id]);

        return $stmt->rowCount();
    }

    public function getUser($username, $password)
    {
        $stmt = $this->pdo->prepare("SELECT * FROM users where username=? and password=?");
        $stmt->execute([$username, $password]);

        return $stmt->rowCount();

    }

}