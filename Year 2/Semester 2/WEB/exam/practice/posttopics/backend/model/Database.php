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

    public function getPosts(){
        $res = $this->db->getPosts();
        return $res;
    }

    public function updatePost($id, $user, $topicid, $text, $date){
        $res = $this->db->updatePost($id, $user, $topicid, $text, $date);
        return $res;
    }

    public function addPost($user, $topicname, $text, $date){
        $res = $this->db->addPost($user, $topicname,$text, $date);
        return $res;
    }

}