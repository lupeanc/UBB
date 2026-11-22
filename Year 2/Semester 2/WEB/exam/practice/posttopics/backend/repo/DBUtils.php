<?php

namespace repo;

use PDO;
use PDOException;
class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "posttopics";
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
    //--------------------------------

    public function getUser($username){
        $stmt = $this->pdo->prepare("SELECT p.user FROM posts p WHERE p.user = :username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        $result = $stmt->fetch();
        return $result;
    }

    public function getPosts(){
        $stmt = $this->pdo->prepare("SELECT * FROM posts");
        $stmt->execute();
        $result = $stmt->fetchAll();
        return $result;
    }

    public function updatePost($id, $user, $topicid, $text, $date){
        $stmt = $this->pdo->prepare("UPDATE posts SET user = :user, topicid = :topicid, text = :text, date = :date WHERE id = :id");
        $stmt->bindParam(":id", $id);
        $stmt->bindParam(":user", $user);
        $stmt->bindParam(":topicid", $topicid);
        $stmt->bindParam(":text", $text);
        $stmt->bindParam(":date", $date);
        $stmt->execute();
        return $stmt->rowCount();
    }

    public function addPost($user, $topicname, $text, $date){
        $stmt = $this->pdo->prepare("SELECT * FROM topics WHERE topicname = :topicname");
        $stmt->bindParam(":topicname", $topicname);
        $stmt->execute();
        $result = $stmt->rowCount();

        if($result == 0){
            $stmt = $this->pdo->prepare("INSERT INTO topics(topicname) VALUES (:topicname)");
            $stmt->bindParam(":topicname", $topicname);
            $stmt->execute();
        }

        $stmt = $this->pdo->prepare("SELECT * FROM topics WHERE topicname = :topicname");
        $stmt->bindParam(":topicname", $topicname);
        $stmt->execute();
        $row = $stmt->fetch();
        $topicid = $row['id'];

        $stmt = $this->pdo->prepare("INSERT INTO posts(user, topicid, text, date) VALUES (:user, :topicid, :text, :date)");
        $stmt->bindParam(":user", $user);
        $stmt->bindParam(":topicid", $topicid);
        $stmt->bindParam(":text", $text);
        $stmt->bindParam(":date", $date);
        $stmt->execute();
        return $stmt->rowCount();
    }
}