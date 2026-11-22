
#ifndef OBSERVER_H
#define OBSERVER_H
#include <vector>
using namespace std;

class Observer{
  public:
  virtual void update() = 0;
  virtual ~Observer() = default;
};

class Subject{
  private:
    vector<Observer*> observers;

    public:
      void addObserver(Observer* obs){
        observers.push_back(obs);
      }

      void notify(){
        for(auto obs : observers) {
          obs->update();
        }

      }
};

#endif //OBSERVER_H
