<?php

namespace model;

class Channel
{
    public $id;
    public $ownerid;
    public $name;
    public $description;
    public $subscribers;

    function __construct($id, $ownerid, $name, $description, $subscribers){
        $this->id = $id;
        $this->ownerid = $ownerid;
        $this->name = $name;
        $this->description = $description;
        $this->subscribers = $subscribers;
    }

}