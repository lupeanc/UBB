<?php

namespace model;

use JsonSerializable;

class GymClass implements JsonSerializable
{
    public $id;
    public $className;

    public $instructorName;

    public $classDate;
    public $maxCapacity;

    function __construct($id, $className, $instructorName, $classDate, $maxCapacity){
        $this->id = $id;
        $this->className = $className;
        $this->instructorName = $instructorName;
        $this->classDate = $classDate;
        $this->maxCapacity = $maxCapacity;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }


}