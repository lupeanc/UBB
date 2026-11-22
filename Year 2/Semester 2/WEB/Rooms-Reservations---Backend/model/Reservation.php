<?php

class Reservation implements JsonSerializable
{
    private $id;

    private $user_id;

    private $room_id;

    private $start;

    private $end;

    function __construct($id, $user_id, $room_id, $start, $end){
        $this->id = $id;
        $this->user_id = $user_id;
        $this->room_id = $room_id;
        $this->start = $start;
        $this->end = $end;
    }

    public function getId(){
        return $this->id;
    }

    public function getUserId(){
        return $this->user_id;
    }

    public function getRoomId(){
        return $this->room_id;
    }

    public function getStart(){
        return $this->start;
    }

    public function getEnd(){
        return $this->end;
    }

    public function setId($id){
        $this->id = $id;
    }

    public function setUserId($id){
        $this->user_id = $id;
    }

    public function setRoomId($room_id){
        $this->room_id = $room_id;
    }

    public function setStart($start){
        $this->start = $start;
    }

    public function setEnd($end){
        $this->end = $end;
    }
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }
}