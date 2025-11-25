
#ifndef PARTICIPANT_H
#define PARTICIPANT_H
#include <iostream>
using namespace std;


class Participant {
  private:
    string name;
    int score;

    public:
      Participant(){}
      Participant(string name, int score){
        this->name = name;
        this->score = score;
      }
      string toString(){
        return name + " " + to_string(score);
      }
      string getName() {
        return name;
      }
      ~Participant()=default;


};



#endif //PARTICIPANT_H
