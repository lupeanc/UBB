
#include "Service.h"

void Service::addCar(Car* car){
  cars.push_back(car);
}
vector<Car*> Service::getCars(){
  return cars;
}

void Service::init(){
  Engine* engine = new Turbo(2.4);
  Car* car = new Car("A1", engine);
  addCar(car);
  Engine* engine2 = new Electric(10, 100);
  Car* car2 =  new Car("A2", engine2);
  addCar(car2);
}