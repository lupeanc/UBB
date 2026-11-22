<?php

namespace controller;

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

require_once "../model/Database.php";
require_once "../view/View.php";
require_once "../model/Journal.php";
require_once "../model/Article.php";

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
            if($_GET['action'] == 'getUserArticles'){
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getUserArticlesByJournals'){
                $this->{$_GET['action']}($_GET['user'], $_GET['journal']);
            } else if($_GET['action'] == 'getJournalNamesForUser'){
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getUser'){
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'addArticle'){
                $this->{$_GET['action']}($_GET['user'], $_GET['journal'], $_GET['summary'], $_GET['date'], $_GET['journalname']);
            } else if($_GET['action'] == 'deleteArticle'){
                $this->{$_GET['action']}($_GET['id']);
            } else if ($_GET['action'] == 'updateArticle'){
                $this->{$_GET['action']}($_GET['id'], $_GET['user'], $_GET['journal'], $_GET['summary'], $_GET['date'], $_GET['journalname']);
            }
        }
    }

    public function getJournalNamesForUser($username){
        $articles = $this->db->getJournalNamesForUser($username);
        return $this->view->output($articles);
    }

    public function getUserArticles($user){
        $articles = $this->db->getUserArticles($user);
        return $this->view->output($articles);
    }

    public function getUserArticlesByJournals($user, $journal){
        $articles = $this->db->getUserArticlesByJournals($user, $journal);
        return $this->view->output($articles);
    }

    public function getUser($username)
    {
        $res = $this->db->getUser($username);
        return $this->view->output($res);
    }

    public function addArticle($username, $journal, $summary, $date, $journalname){
        $res = $this->db->addArticle($username, $journal, $summary, $date, $journalname);
        return $this->view->output($res);
    }

    public function deleteArticle($id)
    {
        $res = $this->db->deleteArticle($id);
        return $this->view->output($res);
    }

    public function updateArticle($id, $user, $journalid, $summary, $date, $journalname){
        $res = $this->db->updateArticle($id, $user, $journalid, $summary, $date, $journalname);
        return $this->view->output($res);
    }
}

$controller = new Controller();
$controller->service();


// COMMAND: php -S localhost:8000