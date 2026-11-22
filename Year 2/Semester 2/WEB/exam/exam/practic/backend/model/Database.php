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

    public function getIdeasAndCommentCount(){
        $res = $this->db->getIdeasAndCommentCount();
        return $res;
    }

    public function addIdea($userId, $title, $body, $postedAt){
        $res = $this->db->addIdea($userId, $title, $body, $postedAt);
        return $res;
    }

    public function addComment($userId, $ideaId, $body, $postedAt){
        $res = $this->db->addComment($userId, $ideaId, $body, $postedAt);
        return $res;
    }

    public function addVote($userId, $ideaId){
        $res = $this->db->addVote($userId, $ideaId);
        return $res;
    }

    public function getCommentsForIdea($ideaId){
        $res = $this->db->getCommentsForIdea($ideaId);
        return $res;
    }

    public function getComments(){
        $res = $this->db->getComments();
        return $res;
    }
}