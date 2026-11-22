<?php

namespace model;

use JsonSerializable;

class User implements JsonSerializable
{
    public $id;
    public $username;
    public $membershipType;

    function __construct($id, $username, $membershipType){
        $this->id = $id;
        $this->username = $username;
        $this->membershipType = $membershipType;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }

}