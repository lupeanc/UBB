
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/weather.h"
#include <vector>

class Repository {

  private:
    vector<weather> elements;

    public:
      Repository();
      ~Repository();
      void LoadData();
      vector<weather> getAll();


};



#endif //REPOSITORY_H
