<?php

namespace repo;

use PDO;
use PDOException;
class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "practice";
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

    public function getUserArticles($username){
        $stmt = $this->pdo->prepare("SELECT * FROM article WHERE user=:username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getUserArticlesByJournals($username, $name){
        $stmt = $this->pdo->prepare("SELECT a.id, a.user, a.journalid, a.summary, a.date FROM article a INNER JOIN journals j ON a.journalid=j.id WHERE j.name=:name AND user=:username");
        $stmt->bindParam(":name", $name);
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetchAll();
    }

//    public function getJournals(){
//        $stmt = $this->pdo->prepare("SELECT * FROM journal");
//        $stmt->execute();
//        return $stmt->fetchAll();
//    }

    public function getJournalNamesForUser($username){
        $stmt = $this->pdo->prepare("SELECT DISTINCT journals.name FROM article INNER JOIN journals ON article.journalid=journals.id WHERE article.user=:username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getUser($username){
        $stmt = $this->pdo->prepare("SELECT user FROM article WHERE user=:username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function addArticle($username, $journalid, $summary, $date, $journalname)
    {
        $stmt = $this->pdo->prepare("SELECT * FROM journals WHERE id=:journalid");
        $stmt->bindParam(":journalid", $journalid);
        $stmt->execute();
        $exists = $stmt->fetchAll();

        if(count($exists)<1){
            $stmt = $this->pdo->prepare("INSERT INTO journals(id, name) VALUES (:id, :name)");
            $stmt->bindParam(":id", $journalid);
            $stmt->bindParam(":name", $journalname);
            $stmt->execute();
        }

        $stmt = $this->pdo->prepare("INSERT INTO article(user, journalid, summary, date) VALUES(:username, :journalid, :summary, :date)");
        $stmt->bindParam(":username", $username);
        $stmt->bindParam(":journalid", $journalid);
        $stmt->bindParam(":summary", $summary);
        $stmt->bindParam(":date", $date);
        $stmt->execute();

//        $new = $this->pdo->prepare("SELECT * FROM article WHERE journalid=:journalid AND user=:username AND date=:date AND summary=:summary");
//        $new->bindParam(":journalid", $journalid);
//        $new->bindParam(":username", $username);
//        $new->bindParam(":date", $date);
//        $new->bindParam(":summary", $summary);
//        $new->execute();
        $rowCount = $stmt->rowCount();
        return $rowCount>0;

    }

    public function deleteArticle($id){
        $stmt = $this->pdo->prepare("DELETE FROM article WHERE id=:id");
        $stmt->bindParam(":id", $id);
        $stmt->execute();
        $rowCount = $stmt->rowCount();
        return $rowCount>0;
    }

    public function updateArticle($id, $user, $journalid, $summary, $date, $journalname){
        $stmt = $this->pdo->prepare("SELECT * FROM journals WHERE id=:journalid");
        $stmt->bindParam(":journalid", $journalid);
        $stmt->execute();
        $exists = $stmt->fetchAll();

        if(count($exists)<1){
            $stmt = $this->pdo->prepare("INSERT INTO journals(id, name) VALUES (:id, :name)");
            $stmt->bindParam(":id", $journalid);
            $stmt->bindParam(":name", $journalname);
            $stmt->execute();
        }

        $stmt = $this->pdo->prepare("UPDATE article SET summary=:summary, date=:date, journalid=:journalid, user=:user WHERE id=:id");
        $stmt->bindParam(":id", $id);
        $stmt->bindParam(":summary", $summary);
        $stmt->bindParam(":date", $date);
        $stmt->bindParam(":journalid", $journalid);
        $stmt->bindParam(":user", $user);
        $stmt->execute();
        $rowCount = $stmt->rowCount();
        return $rowCount>0;
    }
}