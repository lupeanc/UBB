
#include "Block.h"
Block::Block(){}
Block::Block(string address, int constrYear, int nbAp, int occupied) {
  this->address = address;
  this->constrYear = constrYear;
  this->nbAp = nbAp;
  this->occupied = occupied;
}

string Block::toString() {
  string str;
  str = "Address: " + address + " Constr Year: " + to_string(constrYear) + "Nb Ap: " + to_string(nbAp) + "Occupied: " + to_string(occupied);
  return str;
}


Block::~Block(){}