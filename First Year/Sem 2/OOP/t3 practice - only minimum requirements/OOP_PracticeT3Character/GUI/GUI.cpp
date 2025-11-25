
#include "GUI.h"
#include "QVBoxLayout"

GUI::GUI(Repository repo){
  this->repo = repo;
  init_GUI();
  populateList(repo.getPizzas());
}

void GUI::init_GUI(){
  this->listWidget = new QListWidget();
  QVBoxLayout* layout = new QVBoxLayout();
  layout->addWidget(this->listWidget);
  setLayout(layout);
}

void GUI::populateList(vector<Pizza> pizzas){
  this->listWidget->clear();

  for(auto element : pizzas){
    this->listWidget->addItem(QString::fromStdString(element.toString()));
  }

}

GUI::~GUI(){}