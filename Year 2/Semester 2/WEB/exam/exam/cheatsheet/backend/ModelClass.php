<?php

//MIGHT NEED TO IMPORT JSON CLASS!!!!
class ModelClass implements JsonSerializable
{
    public $id;
    public $field;

    function __construct($id, $field){
        $this->id = $id;
        $this->field = $field;
    }

    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }

}