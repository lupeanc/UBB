package com.example.lib.Model

interface CharacterDAO {
    fun insertCharacter(character: Character)
    fun deleteCharacter(character: Character)
    fun getCharcters(): List<Character>

}