
#include "GUI.h"
#include "QVBoxLayout"

GUI::GUI(Repository repo){
  this->repo = repo;
  this->init_GUI();
  this->populateList(repo.getAll());
}

void GUI::init_GUI(){
//  QFont buttonsFont("Consolas", 13, true);

  this->weatherListWidget = new QListWidget();
//  this->weatherListWidget->setFont(buttonsFont);

  QVBoxLayout* layout = new QVBoxLayout();
  layout->addWidget(this->weatherListWidget);

  setLayout(layout);
}

void GUI::populateList(vector<weather> elements){
  this->weatherListWidget->clear();
  for(auto element: elements){
    this->weatherListWidget->addItem(QString::fromStdString(element.toString()));
  }
}

GUI::~GUI(){}