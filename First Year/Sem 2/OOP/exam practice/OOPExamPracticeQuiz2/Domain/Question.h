
#ifndef QUESTION_H
#define QUESTION_H
#include <iostream>
using namespace std;

class Question {
  private:
    int id, score;
    string text, answer;

    public:
      Question(){}
      Question(int id, string text, string answer, int score);
      string toString();
      string toStringParticipant();
      int getID(){
        return id;
      }
      int getScore(){
        return score;
      }
      ~Question()=default;

};



#endif //QUESTION_H
