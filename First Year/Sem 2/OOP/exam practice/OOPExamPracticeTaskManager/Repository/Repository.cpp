
#include "Repository.h"
#include <fstream>
#include <algorithm>

void Repository::LoadData() {
  ifstream finP(R"(F:\c projects uni\OOPExamPracticeTaskManager\programmers)");

  string name;
  int id;

  programmers.clear();
  while(finP >> name >> id) {
    programmers.push_back(Programmer(name, id));
  }
  finP.close();

  ifstream finT(R"(F:\c projects uni\OOPExamPracticeTaskManager\tasks)");

  string desc, status;

  tasks.clear();
  while(finT >> desc >> status>>id) {
    tasks.push_back(Task(desc, status, id));
  }
  finT.close();

}

vector<Programmer> Repository::getProgrammers() {
  LoadData();
  return programmers;
}

bool compare(Task t1, Task t2) {
  return t1.getStatus() < t2.getStatus();
}

vector<Task> Repository::getTasks() {
  LoadData();
  std::sort(tasks.begin(), tasks.end(), compare);
  return tasks;
}

void Repository::writeToFile() {
  ofstream fout(R"(F:\c projects uni\OOPExamPracticeTaskManager\tasks)");

  for(auto task : tasks) {
    fout<<task.toString()<<endl;
  }
  fout.close();
//  this->notify();

}

void Repository::addTask(Task t) {
  this->tasks.push_back(t);
  writeToFile();
  this->notify();
}

void Repository::removeTask(Task t) {
  vector<Task> newTasks;
  for(auto task : tasks) {
    if(task.getDescription() != t.getDescription() || task.getID() != t.getID()) {
      newTasks.push_back(task);
    }
  }
  tasks = newTasks;
  writeToFile();
  this->notify();
}

void Repository::startTask(Task t) {
  vector<Task> newTasks;
  for(auto task : tasks) {
    if(task.getDescription() == t.getDescription()) {
      task.setStatus("inProgress");
      task.setID(t.getID());
    }
    newTasks.push_back(task);
  }
  tasks = newTasks;
  writeToFile();
  this->notify();
}

void Repository::doneTask(Task t) {
  vector<Task> newTasks;
  for(auto task : tasks) {
    if(task.getDescription() == t.getDescription()) {
      task.setStatus("closed");
    }
    newTasks.push_back(task);
  }
  tasks = newTasks;
  writeToFile();
  this->notify();
}