<?php

namespace repo;

use PDO;
use PDOException;
class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "gym2";
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

    //-----------------------------------
    public function getUser($username){
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username=:username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function getUserClasses($username){
        $stmt = $this->pdo->prepare(
            "SELECT c.id, c.className, c.instructorName, c.classDate, c.maxCapacity 
                    FROM users u INNER JOIN bookings b ON u.id=b.userId INNER JOIN classes c ON b.classId=c.id 
                    WHERE u.username=:username AND c.classDate > NOW() AND b.cancelled=0");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        $classes = $stmt->fetchAll();

        foreach($classes as &$class){
            $stmt = $this->pdo->prepare("SELECT * FROM classes c INNER JOIN bookings b ON b.classId=c.id WHERE b.cancelled=0 AND c.id=:classId");
            $stmt->bindParam(":classId", $class['id']);
            $stmt->execute();
            $spotsTaken = $stmt->fetchAll();
            $spots = count($spotsTaken);
            $class['maxCapacity'] -= $spots;
        }

        return $classes;
    }

    public function addBooking($userId, $classId, $bookedAt){
        //check duplicate
        $stmt = $this->pdo->prepare("SELECT * FROM bookings WHERE classId=:classId AND userId=:userId AND cancelled=0");
        $stmt->bindParam(":classId", $classId);
        $stmt->bindParam(":userId", $userId);
        $stmt->execute();
        $duplicate = $stmt->rowCount();

        if($duplicate > 0){
            return "duplicate";
        }

        // check intensity
        $stmt = $this->pdo->prepare("SELECT * FROM classes WHERE id=:classId");
        $stmt->bindParam(":classId", $classId);
        $stmt->execute();
        $class = $stmt->fetch();

        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE id=:userId");
        $stmt->bindParam(":userId", $userId);
        $stmt->execute();
        $user = $stmt->fetch();

        if($user['membershipType'] == "Basic" && str_contains($class['className'], "High")){
            return "basic";
        }

        // check Capacity
        $stmt = $this->pdo->prepare("SELECT * FROM classes c INNER JOIN bookings b ON b.classId=c.id WHERE b.cancelled=0 AND c.id=:classId");
        $stmt->bindParam(":classId", $classId);
        $stmt->execute();

        $spotsTaken = $stmt->fetchAll();
        $spots = count($spotsTaken);
        $class['maxCapacity'] -= $spots;

        if($class['maxCapacity'] == 0){
            $stmt = $this->pdo->prepare("SELECT * FROM waitlists WHERE userId=:userId AND classId=:classId");
            $stmt->bindParam(":userId", $userId);
            $stmt->bindParam(":classId", $classId);
            $stmt->execute();
            $alreadyOn = $stmt->rowCount();

            if($alreadyOn == 0) {
                $stmt = $this->pdo->prepare("INSERT INTO waitlists(userId, classId, addedAt) VALUES(:userId, :classId, :addedAt)");
                $stmt->bindParam(":userId", $userId);
                $stmt->bindParam(":classId", $classId);
                $stmt->bindParam(":addedAt", $bookedAt);
                $stmt->execute();
            }
            return "maxCapacity";
        }

        //all good
        $stmt = $this->pdo->prepare("INSERT INTO bookings(userId, classId, bookedAt, cancelled) VALUES(:userId, :classId, :bookedAt, 0)");
        $stmt->bindParam(":userId", $userId);
        $stmt->bindParam(":classId", $classId);
        $stmt->bindParam(":bookedAt", $bookedAt);
        $stmt->execute();

        return $stmt->rowCount();

    }

    public function getClasses(){
        $stmt = $this->pdo->prepare("SELECT * FROM classes");
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function cancelBooking($userId, $classId){
        $stmt = $this->pdo->prepare("UPDATE bookings SET cancelled=1 WHERE classId=:classId AND userId=:userId");
        $stmt->bindParam(":classId", $classId);
        $stmt->bindParam(":userId", $userId);
        $stmt->execute();

        $stmt = $this->pdo->prepare("SELECT * FROM waitlists WHERE classId=:classId ORDER BY addedAt ASC");
        $stmt->bindParam(":classId", $classId);
        $stmt->execute();
        $waiters = $stmt->fetchAll();
        if(count($waiters) > 0){
            $first = $waiters[0];
            // delete waitlist
            $stmt = $this->pdo->prepare("DELETE FROM waitlists WHERE classId=:classId AND userId=:userId");
            $stmt->bindParam(":classId", $classId);
            $stmt->bindParam(":userId", $first['userId']);
            $stmt->execute();

            // add booking
            $stmt = $this->pdo->prepare("INSERT INTO bookings(userId, classId, bookedAt) VALUES(:userId, :classId, NOW())");
            $stmt->bindParam(":userId", $first['userId']);
            $stmt->bindParam(":classId", $classId);
            $stmt->execute();

            //return username
            $stmt = $this->pdo->prepare("SELECT username FROM users WHERE id=:userId");
            $stmt->bindParam(":userId", $first['userId']);
            $stmt->execute();
            $user = $stmt->fetch();
            return $user['username'];
        }

        return "null";

    }

}