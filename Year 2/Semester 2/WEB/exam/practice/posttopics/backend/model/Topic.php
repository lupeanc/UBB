<?php

namespace model;

class Topic implements \JsonSerializable
{
    public $id;
    public $topicname;

    function __construct($id, $topicname){
        $this->id = $id;
        $this->topicname = $topicname;
    }
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }


}