<?php

class MapScore
{
    public $user;
    public $muscleGroup;
    public $score;

    public function __construct($user, $muscleGroup, $score){
        $this->user = $user;
        $this->muscleGroup = $muscleGroup;
        $this->score = $score;
    }

}