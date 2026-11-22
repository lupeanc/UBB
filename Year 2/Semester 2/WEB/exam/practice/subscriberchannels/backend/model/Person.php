<?php

namespace model;

use JsonSerializable;

class Person implements JsonSerializable
{
    public $id;
    public $name;
    public $age;
    public $gender;

    function __construct($id, $name, $age, $gender){
        $this->id = $id;
        $this->name = $name;
        $this->age = $age;
        $this->gender = $gender;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }

}