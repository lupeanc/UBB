
#ifndef SERVICE_H
#define SERVICE_H
#include "Car.h"
#include "Engine.h"
#include "Turbo.h"
#include "Electric.h"
#include <vector>

class Service{
  private:
    vector<Car*> cars;

    public:
      void addCar(Car* car);
      void init();
      vector<Car*> getCars();
};

#endif //SERVICE_H
