
#include "Repository.h"
#include <fstream>
#include <algorithm>

void Repository::LoadData(){
  ifstream finQ(R"(F:\c projects uni\OOPExamPracticeQuiz2\questions)");
  int id, score;
  string text, answer;

  while(finQ>>id>>text>>answer>>score){
    questions.push_back(Question(id,text,answer, score));
  }
  finQ.close();

  ifstream finP(R"(F:\c projects uni\OOPExamPracticeQuiz2\participants.txt)");

  string name;
  while(finP>>name>>score){
    participants.push_back(Participant(name,score));
  }
  finP.close();

}

bool compare(Question question1, Question question2) {
  return question1.getID() < question2.getID();
}

vector<Question> Repository::getQuestionsByID(){
  questions.clear();
  LoadData();
  std::sort(questions.begin(), questions.end(), compare);
  return questions;
}


bool compareScore(Question question1, Question question2){
  return question1.getScore() > question2.getScore();
}

vector<Question> Repository::getQuestionsByScore(){
  questions.clear();
  LoadData();
  std::sort(questions.begin(), questions.end(), compareScore);
  return questions;
}

void Repository::writeToFile(){
  ofstream fout(R"(F:\c projects uni\OOPExamPracticeQuiz2\questions)");

  for(auto question: questions){
    fout<<question.toString()<<endl;
  }
  fout.close();
//  LoadData();
//  this->notify();
}

void Repository::addQuestion(Question q){
  questions.push_back(q);
  writeToFile();
//  LoadData();
  //or maybe just leave  the one in the wTF
  this->notify();
}