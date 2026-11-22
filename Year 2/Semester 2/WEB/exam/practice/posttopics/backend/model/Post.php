<?php

namespace model;

class Post implements \JsonSerializable
{
    public $id;
    public $user;
    public $topicid;
    public $text;
    public $date;

    function __construct($id, $user, $topicid, $text, $date){
        $this->id = $id;
        $this->user = $user;
        $this->topicid = $topicid;
        $this->text = $text;
        $this->date = $date;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }

}