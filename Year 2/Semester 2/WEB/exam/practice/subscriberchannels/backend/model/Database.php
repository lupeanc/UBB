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

    public function getUserByUsername($username){
        $res = $this->db->getUserByUsername($username);
        return $res;
    }

    public function getUserOwnedChannels($username){
        $res = $this->db->getUserOwnedChannels($username);
        return $res;
    }

    public function getUserSubscribedChannels($username){
        $res = $this->db->getUserSubscribedChannels($username);
        return $res;
    }

    public function subscribeTo($username, $channel, $date){
        $res =  $this->db->subscribeTo($username, $channel, $date);
        return $res;
    }

}