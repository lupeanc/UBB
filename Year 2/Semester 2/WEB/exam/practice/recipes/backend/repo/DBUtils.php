<?php

namespace repo;

use PDO;
use PDOException;
class DBUtils
{
    private $host = "localhost";
    private $user = "root";
    private $pass = "";
    private $db = "recipes";
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

    public function getIngredients(){
        $stmt = $this->pdo->prepare("SELECT * FROM ingredient");
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function addRecipe($user, $title, $totalCalories){
        $stmt = $this->pdo->prepare("SELECT id FROM users WHERE username = :username");
        $stmt->bindParam(":username", $user);
        $stmt->execute();
        $row = $stmt->fetch();
        $id = $row['id'];

        $stmt = $this->pdo->prepare("INSERT INTO recipe(userid, title, totalCalories) VALUES(:userid, :title, :totalcalories)");
        $stmt->bindParam(":userid", $id);
        $stmt->bindParam(":title", $title);
        $stmt->bindParam(":totalcalories", $totalCalories);
        $stmt->execute();

        return $stmt->rowCount();
    }
}