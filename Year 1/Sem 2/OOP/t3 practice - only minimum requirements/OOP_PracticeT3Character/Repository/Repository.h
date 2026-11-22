
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Pizza.h"
#include <vector>

class Repository {

  private:
    vector<Pizza> pizzas;

    public:
      Repository();
      ~Repository();
      vector<Pizza> getPizzas();
      void LoadData();

};



#endif //REPOSITORY_H
