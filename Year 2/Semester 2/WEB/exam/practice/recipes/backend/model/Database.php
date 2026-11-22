<?php

namespace model;
require_once "../repo/DBUtils.php";
use repo\DBUtils;
class Database
{
    private $db;

    public function __construct(){
        $this->db = new DBUtils();
    }
    public function getUser($username){
        $res = $this->db->getUser($username);
        return $res;
    }

    public function getIngredients(){
        $res = $this->db->getIngredients();
        return $res;
    }

    public function addRecipe($user, $title, $totalCalories){
        $res =  $this->db->addRecipe($user, $title, $totalCalories);
        return $res;
    }

}