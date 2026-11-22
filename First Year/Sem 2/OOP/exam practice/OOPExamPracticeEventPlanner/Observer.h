
#ifndef OBSERVER_H
#define OBSERVER_H
#include <vector>
using namespace std;

class Observer {
  public:
    virtual void update() = 0;
    ~Observer() = default;
};

class Subject {
  public:
    vector<Observer*> observers;

    void addObserver(Observer* obs){
      observers.push_back(obs);
    }

    void notify(){
      for(auto obs : observers){
        obs->update();
      }
    }

};

#endif //OBSERVER_H
