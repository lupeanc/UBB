<?php

namespace repo;
require_once "../model/Idea.php";
use Idea;
use PDO;
use PDOException;
class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "practic";
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

    public function getIdeasAndCommentCount(){
        $stmt = $this->pdo->prepare("SELECT * FROM idea");
        $stmt->execute();
        $ideas = $stmt->fetchAll();
        $stmt = $this->pdo->prepare("SELECT * FROM users");
        $stmt->execute();
        $users = $stmt->fetchAll();

        $finalIdeas = array();
        foreach ($ideas as $idea){
            foreach($users as $user){
                if($idea['userId'] == $user['id']) {
                    $stmt = $this->pdo->prepare("SELECT * FROM comment WHERE ideaId=:idea_id");
                    $stmt->bindParam(":idea_id", $idea["id"]);
                    $stmt->execute();
                    $comments = $stmt->fetchAll();
                    $commentCount = count($comments);
                    $finalIdea = new Idea($idea, $user, $commentCount);
                }
            }

            array_push($finalIdeas, $finalIdea);
        }

        return $finalIdeas;
    }

    public function addIdea($userId, $title, $body, $postedAt){
        $stmt = $this->pdo->prepare("INSERT INTO idea(userId, title, body, postedAt) VALUES(:userId, :title, :body, :postedAt)");
        $stmt->bindParam(":userId", $userId);
        $stmt->bindParam(":title", $title);
        $stmt->bindParam(":body", $body);
        $stmt->bindParam(":postedAt", $postedAt);
        $stmt->execute();

        return $stmt->rowCount();
    }

    public function addComment($userId, $ideaId, $body, $postedAt){
        $stmt = $this->pdo->prepare("INSERT INTO comment(ideaId, userId, body, postedAt) VALUES(:ideaId, :userId, :body, :postedAt)");
        $stmt->bindParam(":userId", $userId);
        $stmt->bindParam(":ideaId", $ideaId);
        $stmt->bindParam(":body", $body);
        $stmt->bindParam(":postedAt", $postedAt);
        $stmt->execute();

        return $stmt->rowCount();
    }

    public function addVote($username, $ideaId){
        $user = "%". $username ."%";
        $stmt = $this->pdo->prepare("SELECT votes FROM idea WHERE id=:idea_id AND votes NOT LIKE :user");
        $stmt->bindParam(":idea_id", $ideaId);
        $stmt->bindParam(":user", $user);
        $stmt->execute();
        $votes = $stmt->fetch();
//        echo $votes['votes'];
        if($votes['votes'] > 0){
//            echo "yes";
//            echo $votes['votes'];
            $newVote = $votes['votes'] . " " . $username;
            echo $newVote;
            $stmt = $this->pdo->prepare("UPDATE idea SET votes = :newVote WHERE id=:idea_id");
            $stmt->bindParam(":newVote", $newVote);
            $stmt->bindParam(":idea_id", $ideaId);
            $stmt->execute();

        } else {
//            echo "no";
            return 0;
        }

//        $stmt = $this->pdo->prepare("UPDATE idea SET votes =  WHERE id=:idea_id");
    }

    public function getCommentsForIdea($ideaId){
        $stmt = $this->pdo->prepare("SELECT * FROM comment WHERE ideaId=:idea_id");
        $stmt->bindParam(":idea_id", $ideaId);
        $stmt->execute();
        $comments = $stmt->fetchAll();
        foreach ($comments as &$comment){
            $stmt = $this->pdo->prepare("SELECT username FROM users WHERE id=:user_id");
            $stmt->bindParam(":user_id", $comment['userId']);
            $stmt->execute();
            $user = $stmt->fetch();
            $comment['userId'] = $user['username'];
        }
        return $comments;
    }

    public function getComments(){
        $stmt = $this->pdo->prepare("SELECT * FROM comment");
        $stmt->execute();
        $comments = $stmt->fetchAll();
        foreach ($comments as &$comment){
            $stmt = $this->pdo->prepare("SELECT username FROM users WHERE id=:user_id");
            $stmt->bindParam(":user_id", $comment['userId']);
            $stmt->execute();
            $user = $stmt->fetch();
            $comment['userId'] = $user['username'];
        }
        return $comments;
    }

}