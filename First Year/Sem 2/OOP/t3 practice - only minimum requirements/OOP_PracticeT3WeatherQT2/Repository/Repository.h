
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Weather.h"
#include <vector>

class Repository {
private:
    vector <Weather> elements;

public:
    Repository();
    ~Repository();
    vector <Weather> getAll();
    void LoadData();
};



#endif //REPOSITORY_H
