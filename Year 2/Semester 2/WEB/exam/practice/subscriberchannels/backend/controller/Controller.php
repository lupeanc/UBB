<?php

namespace controller;
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

use model\Database;
use view\View;

error_reporting(E_ALL);
ini_set('display_errors', 1);
if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

require_once "../model/Database.php";
require_once "../model/Channel.php";
require_once "../model/Person.php";
require_once "../view/View.php";
class Controller
{
    private $db;
    private $view;
    public function __construct(){
        $this->db = new Database();
        $this->view = new View();
    }
    public function service(){
//        echo "service";
        if(isset($_GET['action']) && !empty($_GET['action'])){
            if($_GET['action'] == 'getUserByUsername'){
//                echo "here";
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getUserOwnedChannels'){
                $this->{$_GET['action']}($_GET['user']);
            } else if ($_GET['action'] == 'getUserSubscribedChannels') {
                $this->{$_GET['action']}($_GET['user']);
            } else if ($_GET['action'] == 'subscribeTo') {
                $this->{$_GET['action']}($_GET['user'], $_GET['channel'], $_GET['date']);
            }
        }
    }

    public function getUserByUsername($username){
        $res = $this->db->getUserByUsername($username);
        return $this->view->output($res);
    }

    public function getUserOwnedChannels($username){
        $res = $this->db->getUserOwnedChannels($username);
        return $this->view->output($res);
    }

    public function getUserSubscribedChannels($username){
        $res = $this->db->getUserSubscribedChannels($username);
        return $this->view->output($res);
    }

    public function subscribeTo($username, $channel, $date){
        $res =  $this->db->subscribeTo($username, $channel, $date);
        return $this->view->output($res);
    }

}

$controller = new Controller();
$controller->service();