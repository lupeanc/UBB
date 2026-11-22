
#ifndef SERVICE_H
#define SERVICE_H
#pragma once
#include "Repo.h"

class Service {
  private:
    Repo repo;

  public:
    Service(Repo repo);
    vector<Appliance*> getAllRepo();
    void addAppliance(Appliance* appliance);
};

#endif //SERVICE_H
