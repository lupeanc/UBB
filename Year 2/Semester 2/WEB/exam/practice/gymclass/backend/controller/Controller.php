<?php

namespace controller;

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

require_once "../model/Database.php";
require_once "../model/Booking.php";
require_once "../model/GymClass.php";
require_once "../model/User.php";
require_once "../model/Waitlist.php";
require_once "../view/View.php";

use model\Database;
use view\View;

error_reporting(E_ALL);
ini_set('display_errors', 1);
if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

class Controller
{
    private $db;
    private $view;
    public function __construct(){
        $this->db = new Database();
        $this->view = new View();
    }

    public function service(){
        if(isset($_GET['action']) && !empty($_GET['action'])){
            if($_GET['action'] == 'getUser'){
//                echo "GOT IN IF";
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getUserBookingClasses'){
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'addBooking'){
                $this->{$_GET['action']}($_GET['userId'], $_GET['classId'], $_GET['bookedAt'], $_GET['cancelled']);
            } else if($_GET['action'] == 'cancelBooking'){
                $this->{$_GET['action']}($_GET['userId'], $_GET['classId']);
            }
        }
    }

    public function getUser($username)
    {
        $res = $this->db->getUser($username);
        return $this->view->output($res);
    }

    public function getUserBookingClasses($username){
        $classes = $this->db->getUserBookingClasses($username);
        return $this->view->output($classes);
    }

    public function addBooking($username, $classId, $bookedAt, $cancelled){
        $res = $this->db->addBooking($username, $classId, $bookedAt, $cancelled);
        if($res == "duplicate" || $res == "maxCapacity" || $res == "membership"){
            $this->view->returnResult($res);
        }
        else $this->view->output($res);
    }

    public function cancelBooking($username, $classId){
        $res = $this->db->cancelBooking($username, $classId);
        return $this->view->output($res);
    }
}
$controller = new Controller();
$controller->service();