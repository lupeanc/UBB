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
            if($_GET['action'] == 'getUser'){
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getUserSessionHistory'){
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getUserAndScore'){
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getMoves'){
                $this->{$_GET['action']}();
            }
        }
    }
    public function getUser($username)
    {
        $res = $this->db->getUser($username);
        return $this->view->output($res);
    }

    public function getUserSessionHistory($username){
        $res = $this->db->getUserSessionHistory($username);
        return $this->view->output($res);
    }

    public function getUserAndScore($username){
        $res = $this->db->getUserAndScore($username);
        return $this->view->output($res);
    }

    public function getMoves(){
        $res = $this->db->getMoves();
        return $this->view->output($res);
}
}

$controller = new Controller();
$controller->service();


// COMMAND: php -S localhost:8000