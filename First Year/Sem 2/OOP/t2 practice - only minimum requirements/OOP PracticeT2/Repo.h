
#ifndef REPO_H
#define REPO_H
#pragma once
#include "Appliance.h"
#include "Refrigerator.h"
#include "Dishwasher.h"
#include <vector>
class Repo {
private:
    vector<Appliance*> appliances;
  public:
      void addRepo(Appliance* appliance);
      void init();
//      void removeRepo();
      vector<Appliance*> getAllRepo();
};

#endif //REPO_H
