
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Question.h"
#include "../Domain/Participant.h"
#include <vector>
#include "../Observer.h"

class Repository: public Subject {
  private:
    vector<Question> questions;
    vector<Participant> participants;

    public:
      Repository(){LoadData();}
      void LoadData();
      void writeToFile();
      vector<Question> getQuestions(){return questions;}
      vector<Participant> getParticipants(){return participants;}
      vector<Question> getQuestionsByID();
      vector<Question> getQuestionsByScore();
        void addQuestion(Question q);
      ~Repository()=default;

};



#endif //REPOSITORY_H
