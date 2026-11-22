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

    public function getCourses(){
        $res = $this->db->getCourses();
        return $res;
    }

    public function getStudentsToCourse($coursename){
        $res = $this->db->getStudentsToCourse($coursename);
        return $res;
    }

    public function getStudents(){
        $res = $this->db->getStudents();
        return $res;
    }

    public function getStudentCourses($name){
        $res = $this->db->getStudentCourses($name);
        return $res;
    }

}