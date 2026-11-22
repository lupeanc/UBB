package com.example.lib.Model

class Character {
    private var firstName: String;
    private var nickname: String?;
    private var lastName: String?;

    constructor(firstName:String, nickname:String, lastName: String){
        this.firstName = firstName;
        this.nickname = nickname;
        this.lastName = lastName;
    }
}