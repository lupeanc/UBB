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

    public function getUserClasses($username){
        $res = $this->db->getUserClasses($username);
        return $res;
    }

    public function addBooking($userId, $classId, $bookedAt){
        $res = $this->db->addBooking($userId, $classId, $bookedAt);
        return $res;
    }

    public function getClasses(){
        $res = $this->db->getClasses();
        return $res;
    }

    public function cancelBooking($userId, $classId){
        $res = $this->db->cancelBooking($userId, $classId);
        return $res;
    }
}