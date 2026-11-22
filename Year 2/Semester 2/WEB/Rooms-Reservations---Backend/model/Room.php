<?php

class Room implements JsonSerializable
{
    private $id;
    private $nb_beds;
    private $category;
    private $price;

    function __construct($id, $nb_beds, $category, $price){
        $this->id = $id;
        $this->nb_beds = $nb_beds;
        $this->category = $category;
        $this->price = $price;
    }

    public function getId(){
        return $this->id;
    }

    public function getNbBeds(){
        return $this->nb_beds;
    }

    public function getCategory(){
        return $this->category;
    }

    public function getPrice(){
        return $this->price;
    }

    public function setId($id){
        $this->id = $id;
    }

    public function setNbBeds($nb_beds){
        $this->nb_beds = $nb_beds;
    }

    public function setCategory($category){
        $this->category = $category;
    }

    public function setPrice($price){
        $this->price = $price;
    }
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        $vars = get_object_vars($this);
        return $vars;
    }
}