
#ifndef PIZZA_H
#define PIZZA_H
#include <iostream>
using namespace std;


class Pizza {
private:
  int slices;
  string toppings;

  public:
    Pizza();
    Pizza(int slices, string toppings);
    ~Pizza();

    string toString();
    string getToppings();

};



#endif //PIZZA_H
