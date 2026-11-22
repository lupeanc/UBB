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
    private $db = "personcourses";
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
        $stmt = $this->pdo->prepare("SELECT * FROM people WHERE name = :username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function getCourses(){
        $stmt = $this->pdo->prepare("SELECT * FROM courses");
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getStudentsToCourse($coursename){
        $stmt = $this->pdo->prepare("SELECT participants FROM courses WHERE coursename = :coursename");
        $stmt->bindParam(":coursename", $coursename);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getStudents(){
        $stmt = $this->pdo->prepare("SELECT * FROM people WHERE role='student'");
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getStudentCourses($name){
        $stmt = $this->pdo->prepare("SELECT * FROM courses WHERE participants LIKE :name");
        $stmt->bindValue(":name", "%" . $name . "%");
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function addStudentGrade($professorid, $studentname, $coursename, $grade){
        $stmt = $this->pdo->prepare("SELECT * FROM courses WHERE coursename = :coursename AND professorid = :professorid AND participants LIKE :studentname");
        $stmt->bindParam(":coursename", $coursename);
        $stmt->bindParam(":professorid", $professorid);
        $stmt->bindValue(":studentname", "%" . $studentname . "%");
        $stmt->execute();
        $result = $stmt->rowCount();
        if($result > 0){
            $stmt = $this->pdo->prepare("SELECT grades FROM courses WHERE coursename = :coursename");
            $stmt->bindParam(":coursename", $coursename);
            $stmt->execute();
            $result = $stmt->fetchAll();
//            $newgrades = $result[0]["grades"];
//            $stmt = $this->pdo->prepare("UPDATE courses SET grade = :grade WHERE grade LIKE CONCAT(' ', :studentname,'-')");
//            $gradeString = ' ' . $studentname . "-" . $grade;
//            $stmt->bindValue(":grade", $gradeString);
//            $stmt->bindParam(":studentname", $studentname);
        }
        $stmt = $this->pdo->prepare("");
    }

}