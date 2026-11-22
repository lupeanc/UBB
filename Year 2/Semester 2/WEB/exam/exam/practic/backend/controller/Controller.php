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
            } else if($_GET['action'] == 'getIdeasAndCommentCount') {
                $this->{$_GET['action']}();
            } else if($_GET['action'] == 'addIdea') {
                $this->{$_GET['action']}($_GET['user'], $_GET['title'], $_GET['body'], $_GET['postedAt']);
            } else if($_GET['action'] == 'addComment') {
                $this->{$_GET['action']}($_GET['user'], $_GET['idea'], $_GET['body'], $_GET['postedAt']);
            } else if($_GET['action'] == 'addVote') {
                $this->{$_GET['action']}($_GET['user'], $_GET['idea']);
            } else if($_GET['action'] == 'getCommentsForIdea') {
                $this->{$_GET['action']}($_GET['idea']);
            } else if($_GET['action'] == 'getComments') {
                $this->{$_GET['action']}();
            }
        }
    }

    public function getUser($username)
    {
        $res = $this->db->getUser($username);
        return $this->view->output($res);
    }

    public function getIdeasAndCommentCount(){
        $res = $this->db->getIdeasAndCommentCount();
        return $this->view->output($res);
    }

    public function addIdea($userId, $title, $body, $postedAt){
        $res = $this->db->addIdea($userId, $title, $body, $postedAt);
        return $this->view->output($res);
    }

    public function addComment($userId, $ideaId, $body, $postedAt){
        $res = $this->db->addComment($userId, $ideaId, $body, $postedAt);
        return $this->view->output($res);
    }
    public function addVote($userId, $ideaId){
        $res = $this->db->addVote($userId, $ideaId);
        return $this->view->output($res);
    }

    public function getCommentsForIdea($ideaId){
        $res = $this->db->getCommentsForIdea($ideaId);
        return $this->view->output($res);
    }

    public function getComments(){
        $res = $this->db->getComments();
        return $this->view->output($res);
    }

}

$controller = new Controller();
$controller->service();


// COMMAND: php -S localhost:8000