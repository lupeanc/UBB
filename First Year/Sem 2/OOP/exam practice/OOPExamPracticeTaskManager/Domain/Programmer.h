
#ifndef PROGRAMMER_H
#define PROGRAMMER_H
#include <iostream>
using namespace std;

class Programmer {
  private:
    string name;
    int id;

    public:
      Programmer(){};
      Programmer(string name, int id){
        this->name = name;
        this->id = id;
      }
      string getName(){
        return this->name;
      }
      int getID() {
        return this->id;
      }
      string toString(){
        return name + " " + to_string(id);
      }
      ~Programmer()=default;
};



#endif //PROGRAMMER_H
