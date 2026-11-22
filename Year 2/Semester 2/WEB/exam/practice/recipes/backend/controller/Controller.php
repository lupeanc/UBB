<?php

namespace controller;

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

require_once "../model/Database.php";
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
                $this->{$_GET['action']}($_GET['user']);
            } else if($_GET['action'] == 'getIngredients'){
                $this->{$_GET['action']}();
            } else if($_GET['action'] == 'addRecipe'){
                $this->{$_GET['action']}($_GET['user'], $_GET['title'], $_GET['totalcalories']);
            }
        }
    }

    public function getUser($username)
    {
        $res = $this->db->getUser($username);
        return $this->view->output($res);
    }

    public function getIngredients(){
        $res = $this->db->getIngredients();
        return $this->view->output($res);
    }

    public function addRecipe($user, $title, $totalCalories){
        $res = $this->db->addRecipe($user, $title, $totalCalories);
        return $this->view->output($res);
    }

}
$controller = new Controller();
$controller->service();