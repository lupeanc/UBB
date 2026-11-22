
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Person.h"
#include <vector>


class Repository {
    private:
      vector<Person> elements;

      public:
        Repository();
        ~Repository();
        vector<Person> getAll();
        void LoadData();
};



#endif //REPOSITORY_H
