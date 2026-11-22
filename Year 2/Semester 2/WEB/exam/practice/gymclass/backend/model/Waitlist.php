<?php

namespace model;

use JsonSerializable;

class Waitlist implements JsonSerializable
{
    public $id;
    public $userId;
    public $classId;
    public $addedAt;

    function __construct($id, $userId, $classId, $addedAt){
        $this->id = $id;
        $this->userId = $userId;
        $this->classId = $classId;
        $this->addedAt = $addedAt;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }

}