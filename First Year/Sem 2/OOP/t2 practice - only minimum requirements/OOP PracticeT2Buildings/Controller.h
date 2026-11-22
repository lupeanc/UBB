
#ifndef CONTROLLER_H
#define CONTROLLER_H
#include "House.h"
#include "Block.h"
#include <vector>

class Controller {
  private:
    vector<Building*> buildings;

    public:
//      Controller();
      void addBuilding(Building* building);
      void initController();
      vector<Building*> getBuildings();
//      ~Controller();
};

#endif //CONTROLLER_H
