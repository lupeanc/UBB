
#ifndef TASK_H
#define TASK_H
#include <iostream>
using namespace std;


class Task {
  private:
    string desc, status;
    int id;

    public:
      Task(){};
      Task(string desc, string status, int id){
        this->desc = desc;
        this->status = status;
        this->id = id;
      }

      string getDescription() {
        return this->desc;
      }

      string getStatus(){
        return status;
      }

      int getID() {
        return this->id;
      }

      void setStatus(string s) {
        this->status = s;
      }

      void setID(int ID) {
        this->id = ID;
      }

      string toString(){
        return desc + " " + status + " " + to_string(id);
      }
      ~Task()=default;


};



#endif //TASK_H
