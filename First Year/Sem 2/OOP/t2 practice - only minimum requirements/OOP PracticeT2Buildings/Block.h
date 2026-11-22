
#ifndef BLOCK_H
#define BLOCK_H
#include "Building.h"

class Block: public Building{
  private:
    int nbAp;
    int occupied;

    public:
      Block();
      Block(string address, int constrYear, int nbAp, int occupied);
      string toString() override;
      ~Block();
};

#endif //BLOCK_H
