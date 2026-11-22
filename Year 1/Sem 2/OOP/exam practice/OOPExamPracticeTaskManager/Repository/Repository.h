
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include"../Domain/Programmer.h"
#include "../Domain/Task.h"
#include <vector>
#include "../Observer.h"

class Repository: public Subject {
  private:
    vector<Programmer> programmers;
    vector<Task> tasks;

    public:
    Repository(){LoadData();}
    vector<Programmer> getProgrammers();
    vector<Task> getTasks();
    void LoadData();
    void writeToFile();
    void addTask(Task t);
    void removeTask(Task t);
    void startTask(Task t);
    void doneTask(Task t);
    ~Repository()=default;

};



#endif //REPOSITORY_H
