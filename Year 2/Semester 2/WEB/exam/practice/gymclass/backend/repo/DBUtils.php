<?php

namespace repo;

use model\GymClass;
use model\User;
use model\Waitlist;
use PDO;
use PDOException;
class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "gymClass";
    private $charset = "utf8";

//    database access layer
    private $pdo;
    private $error;

    public function __construct(){
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
    }

    //---------------------------------------

    public function getUser($username){
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function getUserBookingClasses($username){
        $stmt = $this->pdo->prepare(
            "SELECT c.id, c.className, c.instructorName, c.classDate, c.maxCapacity
                    FROM users u INNER JOIN bookings b ON u.id = b.userId INNER JOIN classes c ON b.classId = c.id
                    WHERE u.username = :username AND c.classDate >= NOW() AND b.cancelled = 0");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
//        echo $stmt->rowCount();
        return $stmt->fetchAll();
    }

    public function getActiveBookingsForClass($classId){
        $stmt = $this->pdo->prepare("SELECT * FROM bookings WHERE classId = :classId AND cancelled = 0");
        $stmt->bindParam(":classId", $classId);
        $stmt->execute();
        $rows = $stmt->rowCount();
        return $rows;
    }

    public function addBooking($userId, $classId, $bookedAt, $cancelled){
        $stmt = $this->pdo->prepare("INSERT INTO bookings(userId, classId, bookedAt, cancelled) VALUES (:userId, :classId, :bookedAt, :cancelled)");
        $stmt->bindParam(":userId", $userId);
        $stmt->bindParam(":classId", $classId);
        $stmt->bindParam(":bookedAt", $bookedAt);
        $stmt->bindParam(":cancelled", $cancelled);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getUserBookingsClassCount($userId, $classId){
        $stmt = $this->pdo->prepare(
            "SELECT c.id, c.className, c.instructorName, c.classDate, c.maxCapacity
                    FROM users u INNER JOIN bookings b ON u.id = b.userId INNER JOIN classes c ON b.classId = c.id
                    WHERE u.id = :id AND c.classDate >= NOW() AND b.classId = :classId AND cancelled = 0");
        $stmt->bindParam(":id", $userId);
        $stmt->bindParam(":classId", $classId);
        $stmt->execute();
//        echo $stmt->rowCount();
        return $stmt->rowCount();
    }

    public function getUserById($userId){
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE id = :id");
        $stmt->bindParam(":id", $userId);
        $stmt->execute();

        $row = $stmt->fetch();
//        echo $row;
        $user = new User($row["id"], $row["username"], $row["membershipType"]);
        return $user;
    }

    public function getClassById($classId){
        $stmt = $this->pdo->prepare("SELECT * FROM classes WHERE id = :id");
        $stmt->bindParam(":id", $classId);
        $stmt->execute();

        $row = $stmt->fetch();
        $class = new GymClass($row["id"], $row["className"], $row["instructorName"], $row["classDate"], $row["maxCapacity"]);
        return $class;
    }

    public function addToWaitList($userId, $classId, $bookedAt){
        $duplicate = $this->getUserWaitlist($userId, $classId);

        if($duplicate>0){
            return "duplicate";
        }

        $stmt = $this->pdo->prepare("INSERT INTO waitlists(userId, classId, addedAt) VALUES (:userId, :classId, :bookedAt)");
        $stmt->bindParam(":userId", $userId);
        $stmt->bindParam(":classId", $classId);
        $stmt->bindParam(":bookedAt", $bookedAt);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function getUserWaitlist($userId, $classId){
        $stmt = $this->pdo->prepare("SELECT * FROM waitlists WHERE classId = :classId AND userId = :userId");
        $stmt->bindParam(":classId", $classId);
        $stmt->bindParam(":userId", $userId);
        $stmt->execute();
        $row = $stmt->rowCount();
        return $row;
    }

    public function getClassWaitlist($classId){
        $stmt = $this->pdo->prepare("SELECT * FROM waitlists WHERE classId = :classId ORDER BY addedAt ASC");
        $stmt->bindParam(":classId", $classId);
        $stmt->execute();
        $res = $stmt->fetchAll();
        $waitlist = array();

        foreach($res as $key => $value){
            $wait = new Waitlist($value['id'], $value["userId"], $classId, $value["addedAt"]);
            array_push($waitlist, $wait);
        }
        return $waitlist;
    }

    public function cancelBooking($userId, $classId){
        $stmt = $this->pdo->prepare("UPDATE bookings SET cancelled = 1 WHERE classId = :classId AND userId = :userId");
        $stmt->bindParam(":classId", $classId);
        $stmt->bindParam(":userId", $userId);
        $stmt->execute();

        $waitlist = $this->getClassWaitlist($classId);
        if(count($waitlist)>0){
            $wait=$waitlist[0];
//        echo $wait->id;
            $this->addBooking($wait->userId, $wait->classId, $wait->addedAt, 0);
            $stmt=$this->pdo->prepare("DELETE FROM waitlists WHERE id = :id");
            $stmt->bindParam(":id", $wait->id);
            $stmt->execute();
        }

        return true;

    }

}