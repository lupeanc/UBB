
#include "GUIParticipant.h"
GUIParticipant::GUIParticipant(Repository repo, Participant p){
    this->participant = p;
    this->repository = repo;
    initGUI();
    populateQuestions();
}

void GUIParticipant::initGUI(){
    this->setWindowTitle(QString::fromStdString(participant.getName()));

    this->layout = new QVBoxLayout();
    this->questionListWidget = new QListWidget();

    layout->addWidget(this->questionListWidget);
    this->setLayout(layout);

}

void GUIParticipant::populateQuestions(){
    this->questionListWidget->clear();

    for(auto q: repository.getQuestionsByScore()){
        questionListWidget->addItem(QString::fromStdString(q.toStringParticipant()));
    }
}

void GUIParticipant::Update(){
  cout<<"GUIParticipant::update"<<endl;
  this->questionListWidget->clear();
  this->populateQuestions();
}