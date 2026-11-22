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

    public function getUserBookingClasses($username){
        $res = $this->db->getUserBookingClasses($username);
        $classes = array();
        foreach ($res as $key => $value) {
            $max = $value['maxCapacity'];
            $booked = $this->db->getActiveBookingsForClass($value['id']);
            $left = $max-$booked;
            $class = new GymClass($value['id'], $value['className'], $value['instructorName'], $value['classDate'], $left);
            array_push($classes, $class);
        }
        return $classes;
    }

    public function addBooking($userId, $classId, $bookedAt, $cancelled){
        $user = $this->db->getUserById($userId);
        $class = $this->db->getClassById($classId);
        $duplicate = $this->db->getUserBookingsClassCount($userId, $classId);

        if($duplicate > 0){
            return "duplicate";
        }

        if($user->membershipType == "Basic" && str_contains($class->className, "High")){
            return "membership";
        }

        $booked = $this->db->getActiveBookingsForClass($classId);
        if($class->maxCapacity-$booked==0){
            $this->db->addToWaitList($userId, $classId, $bookedAt);
            return "maxCapacity";
        }

        return $this->db->addBooking($userId, $classId, $bookedAt, $cancelled);
    }

    public function cancelBooking($userId, $classId){
        $res = $this->db->cancelBooking($userId, $classId);
        return $res;
    }

}