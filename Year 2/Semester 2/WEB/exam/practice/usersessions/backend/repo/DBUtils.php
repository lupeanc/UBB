<?php

namespace repo;
require_once "../model/SessionHistory.php";
require_once "../model/MapScore.php";

use MapScore;
use PDO;
use PDOException;
use SessionHistory;

class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "usersessions";
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

    public function getUserAndScore($username){
        $user = $this->getUser($username);
        $userId = $user['id'];

        $stmt = $this->pdo->prepare("SELECT * FROM move");
        $stmt->execute();
        $moves = $stmt->fetchAll();

        $stmt = $this->pdo->prepare("SELECT * FROM session WHERE userid=:userid");
        $stmt->bindParam(":userid", $userId);
        $stmt->execute();
        $sessions = $stmt->fetchAll();

        $stmt = $this->pdo->prepare("SELECT DISTINCT muscleGroup FROM move");
        $stmt->execute();
        $muscleGroups = $stmt->fetchAll();

        $map = array();

        foreach($muscleGroups as $muscleGroup){
            foreach($sessions as $session){
                foreach($moves as $move){
                    if($muscleGroup['muscleGroup'] == $move['muscleGroup'] && $session['moveid'] == $move['id']){
                        $score = new MapScore($user, $move['muscleGroup'], 0);
                        if($session['completed'] == 1 && $score->score < 100){
                            $score->score = $score->score + 10;
                        } else {
                            $score->score = $score->score * 0.8;
                        }
                    }
                }
            }
            array_push($map, $score);
        }

        return $map;

    }

    public function getUserSessionHistory($username){
        $stmt = $this->pdo->prepare("SELECT id FROM users WHERE username=:username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        $res = $stmt->fetch();
        $id = $res['id'];

        $stmt = $this->pdo->prepare("SELECT * FROM session WHERE userid=:id");
        $stmt->bindParam(":id", $id);
        $stmt->execute();
        $sess = $stmt->fetchAll();

        $stmt = $this->pdo->prepare("SELECT * FROM move");
        $stmt->execute();
        $moves = $stmt->fetchAll();

        $history = array();

        foreach($moves as $value){
            foreach($sess as $value2){
                if($value['id'] == $value2['moveid']){
                    $s = new SessionHistory($value2['id'], $value2['userid'], $value2['moveid'], $value['name'], $value2['completed']);
                    array_push($history, $s);
                }
            }
        }

        return $history;
    }

    public function getMoves(){
        $stmt = $this->pdo->prepare("SELECT * FROM move");
        $stmt->execute();
        return $stmt->fetchAll();
    }
}