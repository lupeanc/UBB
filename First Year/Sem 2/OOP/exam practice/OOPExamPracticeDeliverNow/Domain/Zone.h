
#ifndef ZONE_H
#define ZONE_H
#include <iostream>
using namespace std;


class Zone {
  public:
    int xcentre, ycentre;
    int radius;
    Zone(){};
    Zone(int xcentre, int ycentre, int radius){
      this->xcentre = xcentre;
      this->ycentre = ycentre;
      this->radius = radius;
    }
    string toString(){
      return to_string(xcentre) + to_string(ycentre) + to_string(radius);
    }
    ~Zone()=default;

};



#endif //ZONE_H
