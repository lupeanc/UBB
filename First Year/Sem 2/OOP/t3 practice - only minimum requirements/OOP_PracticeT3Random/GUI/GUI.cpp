
#include "GUI.h"
#include "QVBoxLayout"

GUI::GUI(Repository repo){
  this->repo = repo;
  init_GUI();
  populateList(repo.getAll());
}

GUI::~GUI(){}

void GUI::init_GUI(){
  this->personListWidget = new QListWidget();
  QVBoxLayout *layout = new QVBoxLayout();
  layout->addWidget(personListWidget);
  this->setLayout(layout);
}

void GUI::populateList(vector<Person> elements){
  this->personListWidget->clear();
  for(auto element : elements){
    personListWidget->addItem(QString::fromStdString(element.toString()));
  }
}