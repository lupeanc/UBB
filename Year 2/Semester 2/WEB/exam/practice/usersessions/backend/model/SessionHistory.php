<?php

class SessionHistory
{
    public $id;
    public $userid;
    public $moveid;
    public $movename;
    public $completed;

    function __construct($id, $userid, $moveid, $movename, $completed){
        $this->id = $id;
        $this->userid = $userid;
        $this->moveid = $moveid;
        $this->movename = $movename;
        $this->completed = $completed;
    }

}