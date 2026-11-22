<?php
namespace controller;

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

use Model;
use view\View;
//error_reporting(E_ALL);
//ini_set('display_errors', 1);
//header('Content-Type: application/json');

//if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
//    http_response_code(200);
//    exit();
//}
require_once '../model/model.php';
require_once '../model/Reservation.php';
require_once '../model/Room.php';
require_once '../view/View.php';
class Controller
{
    private $model;
    private $view;

    public function __construct(){
        $this->model = new Model();
        $this->view = new View();
    }

    public function service(){
        if(isset($_GET['action']) && !empty($_GET['action'])) {
            if ($_GET['action'] == 'getAllRooms') {
                $this->{$_GET['action']}();
            } else if ($_GET['action'] == 'getRoom') {
                $this->{$_GET['action']}($_GET['id']);
            } else if ($_GET['action'] == 'getAllReservations') {
                $this->{$_GET['action']}();
            } else if ($_GET['action'] == 'getReservation') {
                $this->{$_GET['action']}($_GET['id']);
            } else if ($_GET['action'] == 'getNbBeds') {
                $this->{$_GET['action']}();
            } else if ($_GET['action'] == 'getCategories') {
                $this->{$_GET['action']}();
            } else if ($_GET['action'] == 'getPrices') {
                $this->{$_GET['action']}();
            } else if ($_GET['action'] == 'addReservation') {
                $this->{$_GET['action']}($_GET['user_id'], $_GET['room_id'], $_GET['start'], $_GET['end']);
            } else if ($_GET['action'] == 'deleteReservation') {
                $this->{$_GET['action']}($_GET['id']);
            } else if ($_GET['action'] == 'updateReservation') {
                $this->{$_GET['action']}($_GET['id'], $_GET['user_id'], $_GET['room_id'], $_GET['start'], $_GET['end']);
            } else if ($_GET['action'] == 'getFilteredRoomsByNbBeds') {
                $this->{$_GET['action']}($_GET['nb_beds']);
            } else if ($_GET['action'] == 'getFilteredRoomsByCategory') {
                $this->{$_GET['action']}($_GET['category']);
            } else if ($_GET['action'] == 'getFilteredRoomsByPrice') {
                $this->{$_GET['action']}($_GET['price']);
            }
            else if($_GET['action'] == 'getUser') {
                $this->{$_GET['action']}($_GET['username'], $_GET['password']);
            }
        }
    }

    public function getAllRooms(){
        $rooms = $this->model->selectAllRooms();
        return $this->view->output($rooms);
    }

    public function getAllReservations(){
        $reservations = $this->model->selectAllReservations();
        return $this->view->output($reservations);
    }

    public function getReservation($id){
        $reservation = $this->model->selectReservation($id);
        return $this->view->output($reservation);
    }

    public function getNbBeds(){
        $nbBedsList = $this->model->getNbBeds();
        return $this->view->output($nbBedsList);
    }

    public function getCategories(){
        $categories = $this->model->getCategories();
        return $this->view->output($categories);
    }

    public function getPrices(){
        $prices = $this->model->getPrices();
        return $this->view->output($prices);
    }

    public function getFilteredRoomsByNbBeds($nbBeds){
        $rooms = $this->model->getFilteredRoomsByNbBeds($nbBeds);
        return $this->view->output($rooms);
    }

    public function getFilteredRoomsByPrice($price){
        $rooms = $this->model->getFilteredRoomsByPrice($price);
        return $this->view->output($rooms);
    }

    public function getFilteredRoomsByCategory($category){
        $rooms = $this->model->getFilteredRoomsByCategory($category);
        return $this->view->output($rooms);
    }

    public function addReservation($user_id, $room_id, $start, $end){
//        var_dump($start, $end);
//        exit;
        $result = $this->model->addReservation($user_id, $room_id, $start, $end);
        if($result > 0){
            $r = "Success";
        }
        else{
            $r = "Error";
        }
        $this->view->returnResult($r);
    }

    public function updateReservation($id, $user_id, $room_id, $start, $end){
        $result = $this->model->updateReservation($id, $user_id, $room_id, $start, $end);
        if($result > 0){
            $r = "Success";
        }
        else{
            $r = "Error";
        }
        $this->view->returnResult($r);
    }

    public function deleteReservation($id){
        $result = $this->model->deleteReservation($id);
        if($result > 0){
            $r = "Success";
        }
        else{
            $r = "Error";
        }
        $this->view->returnResult($r);
    }

    public function getUser($username, $password){
        $result = $this->model->getUser($username, $password);
        if($result > 0){
            $r = "Success";
        }
        else {
            $r = "Error";
        }
        $this->view->returnResult($r);
    }
}

$controller = new Controller();
$controller->service();