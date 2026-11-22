
#include "Question.h"

Question::Question(int id, string text, string answer, int score){
  this->id = id;
  this->text = text;
  this->answer = answer;
  this->score = score;

}

string Question::toString(){
  return to_string(this->id) + " " + this->text + " " + this->answer + " " + to_string(this->score);
}

string Question::toStringParticipant(){
  return to_string(this->id) + " " + this->text + " " + to_string(this->score);
}