
#ifndef PERSON_H
#define PERSON_H
#include "Measurement.h"
#include "BMI.h"
#include "BP.h"
#include <vector>

class Person {
    private:
    string name;
    vector<Measurement*> measurements;

    public:
    // Person();
    // Person(string name);
    string getName();
    void setName(string nameNew);
    void addRepo(Measurement* measurement);
    void initRepo();
    vector<Measurement*> getRepo();
    // ~Person();

};

#endif //PERSON_H
