
#include "GUI.h"
#include <QMessageBox>

GUI::GUI(Repository repository, Programmer programmer){
  this->repository = repository;
  this->programmer = programmer;
  initGUI();
  populateTasks();
  connectSignals();
}

void GUI::initGUI(){
  this->setWindowTitle(QString::fromStdString(programmer.getName()));

  this->layout = new QVBoxLayout();
  this->taskListWidget = new QListWidget();
  this->descLineEdit = new QLineEdit();
  this->programmerLineEdit = new QLineEdit();
  this->addButton = new QPushButton("ADD");
  this->removeButton = new QPushButton("REMOVE");
  this->startButton = new QPushButton("Start");
  this->doneButton = new QPushButton("Done");

  layout->addWidget(taskListWidget);
  layout->addWidget(descLineEdit);
  layout->addWidget(programmerLineEdit);
  layout->addWidget(addButton);
  layout->addWidget(removeButton);
  layout->addWidget(startButton);
  layout->addWidget(doneButton);
  this->setLayout(layout);
}

void GUI::populateTasks(){
  this->taskListWidget->clear();

  for(auto task : repository.getTasks()){
    this->taskListWidget->addItem(QString::fromStdString(task.toString()));
  }

}

void GUI::addTask(){
  string desc = this->descLineEdit->text().toStdString();
  string id = this->programmerLineEdit->text().toStdString();
  string status = "open";

  repository.addTask(Task(desc, status, stoi(id)));
}

void GUI::removeTask(){
  string desc = this->descLineEdit->text().toStdString();
  string id = this->programmerLineEdit->text().toStdString();
  repository.removeTask(Task(desc, "open", stoi(id)));
}

void GUI::start(){
  string desc = this->descLineEdit->text().toStdString();

  for(auto task : repository.getTasks()){
    if(task.getDescription() == desc){
      if(task.getStatus() == "closed"){
        QMessageBox::critical(this, "Error", "The Task is closed!");
        return;
      }
    }
  }

  repository.startTask(Task(desc, "open", programmer.getID()));
}

void GUI::done(){
  string desc = this->descLineEdit->text().toStdString();

  for(auto task : repository.getTasks()){
    if(task.getDescription() == desc){
      if(task.getID() != programmer.getID()){
        QMessageBox::critical(this, "Error", "Cannot complete task!");
      }
      if(task.getStatus() != "inProgress"){
        cout<<task.getStatus();
        QMessageBox::critical(this, "Error", "The Task is NOT in progress!");
        return;
      }
    }
  }

  repository.doneTask(Task(desc, "inProgress", programmer.getID()));

}

void GUI::connectSignals(){
  QObject::connect(this->addButton, &QPushButton::clicked, this, &GUI::addTask);
  QObject::connect(this->removeButton, &QPushButton::clicked, this, &GUI::removeTask);
  QObject::connect(this->startButton, &QPushButton::clicked, this, &GUI::start);
  QObject::connect(this->doneButton, &QPushButton::clicked, this, &GUI::done);
}

void GUI::update(){
  populateTasks();
}