<?php

use repo\DBUtils;

require_once '../repo/DBUtils.php';
class Model
{
    private $db;

    public function __construct(){
        $this->db = new DBUtils();
    }

    public function selectReservation($id){
        $resultset = $this->db->selectReservation($id);
        $reservation = new Reservation($resultset[0]['id'], $resultset[0]['user_id'], $resultset[0]['room_id'], $resultset[0]['start'], $resultset[0]['end']);
        return $reservation;
    }

    public function selectAllReservations(){
        $resultset = $this->db->selectAllReservations();
        $reservations = array();
        foreach($resultset as $key => $value){
            $reservation = new Reservation($value['id'], $value['user_id'], $value['room_id'], $value['start'], $value['end']);
            array_push($reservations, $reservation);
        }
        return $reservations;
    }

    public function selectRoom($id){
        $resultset = $this->db->selectRoom($id);
        $room = new Room($resultset[0]['id'], $resultset[0]['nb_beds'], $resultset[0]['category'], $resultset[0]['price']);
        return $room;
    }

    public function selectAllRooms(){
        $resultset = $this->db->selectAllRooms();
        $rooms = array();
        foreach($resultset as $key => $value){
            $room = new Room($value['id'], $value['nb_beds'], $value['category'], $value['price']);
            array_push($rooms, $room);
        }
        return $rooms;
    }

    //nb_beds, categ, price
    public function getFilteredRoomsByNbBeds($nbBeds){
        $resultset = $this->db->getFilteredRoomsByNbBeds($nbBeds);
        $rooms = array();
        foreach($resultset as $key => $value){
            $room = new Room($value['id'], $value['nb_beds'], $value['category'], $value['price']);
            array_push($rooms, $room);
        }
        return $rooms;
    }

    public function getFilteredRoomsByCategory($category){
        $resultset = $this->db->getFilteredRoomsByCetegory($category);
        $rooms = array();
        foreach($resultset as $key => $value){
            $room = new Room($value['id'], $value['nb_beds'], $value['category'], $value['price']);
            array_push($rooms, $room);
        }
        return $rooms;
    }

    public function getFilteredRoomsByPrice($price){
        $resultset = $this->db->getFilteredRoomsByPrice($price);
        $rooms = array();
        foreach($resultset as $key => $value){
            $room = new Room($value['id'], $value['nb_beds'], $value['category'], $value['price']);
            array_push($rooms, $room);
        }
        return $rooms;
    }

    public function getNbBeds()
    {
        $resultset = $this->db->getNbBeds();
        $nbBedsList = array();
        foreach($resultset as $value){
            array_push($nbBedsList, $value['nb_beds']);
        }
        return $nbBedsList;
    }

    public function getCategories(){
        $resultset = $this->db->getCategories();
        $categories = array();
        foreach($resultset as $value){
            array_push($categories, $value['category']);
        }
        return $categories;
    }

    public function getPrices(){
        $resultset = $this->db->getPrices();
        $prices = array();
        foreach($resultset as $value){
            array_push($prices, $value['price']);
        }
        return $prices;
    }

    public function addReservation($user_id, $room_id, $start, $end)
    {
        return $this->db->addReservation($user_id, $room_id, $start, $end);
    }

    public function deleteReservation($id){
        return $this->db->deleteReservation($id);
    }

    public function updateReservation($id, $user_id, $room_id, $start, $end){
        return $this->db->updateReservation($id, $user_id, $room_id, $start, $end);
    }

    public function getUser($username, $password){
        return $this->db->getUser($username, $password);
    }

}