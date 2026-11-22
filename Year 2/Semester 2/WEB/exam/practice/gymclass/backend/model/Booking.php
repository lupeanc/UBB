<?php

namespace model;

use JsonSerializable;

class Booking implements JsonSerializable
{
    private $id;
    private $userId;
    private $classId;
    private $bookedAt;
    private $cancelled;

    function __construct($id, $userId, $classId, $bookedAt, $cancelled){
        $this->id = $id;
        $this->userId = $userId;
        $this->classId = $classId;
        $this->bookedAt = $bookedAt;
        $this->cancelled = $cancelled;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }

}