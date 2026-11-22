<?php

class Idea implements JsonSerializable
{
    public $idea;
    public $user;
    public $commentCount;

    function __construct($idea, $user, $commentCount){
        $this->idea = $idea;
        $this->user = $user;
        $this->commentCount = $commentCount;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }
}