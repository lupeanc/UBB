<?php

namespace repo;
use model\Channel;
use PDO;
use PDOException;
class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "subscriberchannels";
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
    public function getUserByUsername($username){
        $stmt = $this->pdo->prepare("SELECT * FROM people WHERE name = :username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function getUserOwnedChannels($username){
        $stmt = $this->pdo->prepare("SELECT c.id, c.ownerid, c.name, c.description, c.subscribers FROM people p INNER JOIN channels c ON p.id=c.ownerid WHERE p.name = :username");
        $stmt->bindParam(":username", $username);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getUserSubscribedChannels($username){
        $stmt = $this->pdo->prepare("SELECT c.id, c.ownerid, c.name, c.description, c.subscribers FROM channels c WHERE c.subscribers LIKE :username");
        $stmt->bindValue(":username", "%" . $username . "%");
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function subscribeTo($username, $channel, $date){
        $stmt = $this->pdo->prepare("SELECT * FROM channels WHERE name = :channel");
        $stmt->bindParam(":channel", $channel);
        $stmt->execute();
        $row = $stmt->fetch();

        $channel= new Channel($row['id'], $row['ownerid'], $row['name'], $row['description'], $row['subscribers']);
        $channel->subscribers = $channel->subscribers . " $username $date";
//        echo $channel->subscribers;

        $stmt = $this->pdo->prepare("INSERT INTO channels(ownerid, name, description, subscribers) VALUES('$channel->ownerid', '$channel->name', '$channel->description', '$channel->subscribers')");
        $stmt->execute();
        return $stmt->rowCount();
    }
}