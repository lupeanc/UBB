<?php

class Article implements JsonSerializable
{
    private $id;
    private $user;

    private $journalID;
    private $summary;
    private $date;

    function __construct($id, $user, $journalID, $summary, $date){
        $this->id = $id;
        $this->user = $user;
        $this->journalID = $journalID;
        $this->summary = $summary;
        $this->date = $date;
    }
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }
}