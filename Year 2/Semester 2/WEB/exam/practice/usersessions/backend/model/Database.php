<?php

use Couchbase\User;
use repo\DBUtils;

require_once '../repo/DBUtils.php';
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

    public function getUserSessionHistory($username){
        $res = $this->db->getUserSessionHistory($username);
        return $res;
    }

    public function getUserAndScore($username){
        $res = $this->db->getUserAndScore($username);
        return $res;
    }

    public function getMoves(){
        $res = $this->db->getMoves();
        return $res;
    }
}