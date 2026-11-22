<?php

namespace controller;

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

require_once "../model/Database.php";
require_once "../view/View.php";
use Database;
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
            if($_GET['action'] == 'getUser') {
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getUserClasses') {
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'addBooking') {
                $this->{$_GET['action']}($_GET['user'], $_GET['classId'], $_GET['bookedAt']);
            } else if($_GET['action'] == 'getClasses') {
                $this->{$_GET['action']}();
            } else if($_GET['action'] == 'cancelBooking') {
                $this->{$_GET['action']}($_GET['user'], $_GET['classId']);
            }
        }
    }

    public function getUser($username)
    {
        $res = $this->db->getUser($username);
        return $this->view->output($res);
    }

    public function getUserClasses($username){
        $res = $this->db->getUserClasses($username);
        return $this->view->output($res);
    }

    public function addBooking($userId, $classId, $bookedAt)
    {
        $res = $this->db->addBooking($userId, $classId, $bookedAt);
        if ($res == "duplicate" || $res == "maxCapacity" || $res == "basic") {
            $this->view->returnResult($res);
        } else {
            return $this->view->output($res);
        }
    }

    public function getClasses(){
        $res = $this->db->getClasses();
        return $this->view->output($res);
    }

    public function cancelBooking($userId, $classId){
        $res = $this->db->cancelBooking($userId, $classId);
        $this->view->returnResult($res);
    }
}

$controller = new Controller();
$controller->service();


// COMMAND: php -S localhost:8000