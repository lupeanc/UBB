<?php

namespace controller;

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

require_once "../view/View.php";
require_once "../model/Database.php";
require_once "../model/Topic.php";
require_once "../model/Post.php";

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
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getPosts'){
                $this->{$_GET['action']}();
            } else if($_GET['action'] == 'updatePost'){
                $this->{$_GET['action']}($_GET['id'], $_GET['user'], $_GET['topicid'], $_GET['text'], $_GET['date']);
            } else if($_GET['action'] == 'addPost'){
                $this->{$_GET['action']}($_GET['user'], $_GET['topicname'], $_GET['text'], $_GET['date']);
            }
        }
    }

    public function getUser($username){
        $res = $this->db->getUser($username);
        return $this->view->output($res);
    }

    public function getPosts(){
        $res = $this->db->getPosts();
        return $this->view->output($res);
    }

    public function updatePost($id, $user, $topicid, $text, $date){
        $res = $this->db->updatePost($id, $user, $topicid, $text, $date);
        return $this->view->output($res);
    }

    public function addPost($user,  $topicname, $text, $date){
        $res = $this->db->addPost($user, $topicname, $text, $date);
        return $this->view->output($res);
    }

}

$controller = new Controller();
$controller->service();