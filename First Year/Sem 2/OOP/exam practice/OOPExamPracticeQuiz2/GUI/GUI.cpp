
#include "GUI.h"
#include <QMessageBox>

GUI::GUI(Repository repo){
  this->repository = repo;
  initGUI();
  populateQuestions();
  connectSignals();
}

void GUI::initGUI(){
  this->setWindowTitle(QString::fromStdString("Presenter"));

  this->layout = new QVBoxLayout();
  this->questionListWidget = new QListWidget();
  this->addButton = new QPushButton("Add Question");
  this->idLineEdit = new QLineEdit();
  this->textLineEdit = new QLineEdit();
  this->answerLineEdit = new QLineEdit();
  this->scoreLineEdit = new QLineEdit();

  layout->addWidget(this->questionListWidget);
  layout->addWidget(this->idLineEdit);
  layout->addWidget(this->textLineEdit);
  layout->addWidget(this->answerLineEdit);
  layout->addWidget(this->scoreLineEdit);
  layout->addWidget(this->addButton);
  this->setLayout(layout);

}

void GUI::populateQuestions(){
  this->questionListWidget->clear();

  for(auto q: repository.getQuestionsByID()){
    questionListWidget->addItem(QString::fromStdString(q.toString()));
  }
}

void GUI::addQuestion(){
  string id = this->idLineEdit->text().toStdString();
  string text = this->textLineEdit->text().toStdString();
  string answer = this->answerLineEdit->text().toStdString();
  string score = this->scoreLineEdit->text().toStdString();

  bool found=false;

  for(auto q: repository.getQuestions()){
    if(q.getID() == stoi(id)){
      found = true;
      break;
    }
  }

  if(text.size()==0 || found){
    QMessageBox::critical(this, "ERROR", QString::fromStdString("INVALID"));
    return;
  }

  Question question(stoi(id), text, answer, stoi(score));
  repository.addQuestion(question);
  this->Update();
}

void GUI::connectSignals(){
  QObject::connect(addButton, &QPushButton::clicked, this, &GUI::addQuestion);
}

void GUI::Update(){
  cout<<"update GUI"<<endl;
  this->questionListWidget->clear();
  populateQuestions();
}