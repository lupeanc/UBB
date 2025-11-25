
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Weather.h"
#include <vector>
#pragma once

class Repository {
    private:
      vector<Weather> elements;
      void LoadData();

    public:
      Repository();
      ~Repository();
      vector<Weather> getAll();
};



#endif //REPOSITORY_H
