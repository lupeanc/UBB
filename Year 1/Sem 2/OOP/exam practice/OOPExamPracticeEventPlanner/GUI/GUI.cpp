
#include "GUI.h"
#include <QMessageBox>
#include <cmath>
GUI::GUI(Repository repo, Person p){
  this->repo = repo;
  this->p = p;
  initGUI();
  connectSignals();
  populateEvents();
}

void GUI::initGUI(){
  this->setWindowTitle(QString::fromStdString(p.getName()));

  layout = new QVBoxLayout();
  label = new QLabel(QString::fromStdString(to_string(p.getXloc()) + " " + to_string(p.getYloc())));
  eventListWidget = new QListWidget();
  nameLineEdit = new QLineEdit();
  descLineEdit = new QLineEdit();
  xlocLineEdit = new QLineEdit();
  ylocLineEdit = new QLineEdit();
  dateLineEdit = new QLineEdit();
  addButton = new QPushButton("Add");
  checkBox = new QCheckBox("Events near you");

  layout->addWidget(label);
  layout->addWidget(eventListWidget);
  if(p.getStatus() == true){
    layout->addWidget(nameLineEdit);
    layout->addWidget(descLineEdit);
    layout->addWidget(xlocLineEdit);
    layout->addWidget(ylocLineEdit);
    layout->addWidget(dateLineEdit);
    layout->addWidget(addButton);
  }
  else{
    layout->addWidget(checkBox);
  }

  setLayout(layout);
}

void GUI::populateEvents(){
  this->eventListWidget->clear();
  for(auto e: repo.getEvents()){
    QListWidgetItem *item = new QListWidgetItem(QString::fromStdString(e.toStringWindow()));
    if(p.getStatus() == true && e.getOrganiser() == p.getName()){
      item->setBackground(Qt::green);
    }
    eventListWidget->addItem(item);
  }

}

void GUI::addEvent(){
  string name = nameLineEdit->text().toStdString();
  string desc = descLineEdit->text().toStdString();
  string xloc = xlocLineEdit->text().toStdString();
  string yloc = ylocLineEdit->text().toStdString();
  string date = dateLineEdit->text().toStdString();

  for(auto e: repo.getEvents()){
    if(e.getName() == name && e.getXloc() == stoi(xloc) && e.getYloc() == stoi(yloc)){
      QMessageBox::critical(this, "Error", "Event already exists!");
      return;
    }
  }

  Event e(p.getName(), name, desc, stoi(xloc), stoi(yloc), date);
  repo.addEvent(e);
}

void GUI::eventsNearYou(){

  if(checkBox->isChecked()){
    int formula;

    eventListWidget->clear();
    for(auto e: repo.getEvents()){
      formula = sqrt(pow(p.getXloc() - e.getXloc(), 2) + pow(p.getYloc() - e.getYloc(), 2));
      if(formula<5){
        eventListWidget->addItem(QString::fromStdString(e.toStringWindow()));
      }
    }
  }
  else
    populateEvents();

}

void GUI::connectSignals(){
  QObject::connect(addButton, &QPushButton::clicked, this, &GUI::addEvent);
  QObject::connect(checkBox, &QCheckBox::toggled, this, &GUI::eventsNearYou);
}

void GUI::update(){
  populateEvents();
}