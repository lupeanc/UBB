#include <QVBoxLayout>
#include <QMessageBox>
#include "GUI.h"
GUI::GUI(Department d, Repository repository){
  this->department = d;
  this->repository = repository;
  init_GUI();
  populateAll();
  connectSignals();
}

void GUI::init_GUI(){
  this->setWindowTitle(QString::fromStdString(department.getName()));
  layout = new QVBoxLayout();

  this->label = new QLabel(QString::fromStdString(department.getDescription()));

  this->volunteerDepListWidget = new QListWidget();
  this->volunteerListWidget = new QListWidget();

  this->addButton = new QPushButton(QString::fromStdString("ADD"));
  this->nameLineEdit = new QLineEdit();
  this->emailLineEdit = new QLineEdit();
  this->i1LineEdit = new QLineEdit();
  this->i2LineEdit = new QLineEdit();
  this->i3LineEdit = new QLineEdit();
  this->departmentLineEdit = new QLineEdit();


  layout->addWidget(label);
  layout->addWidget(volunteerDepListWidget);
  layout->addWidget(volunteerListWidget);

  layout->addWidget(nameLineEdit);
  layout->addWidget(emailLineEdit);
  layout->addWidget(i1LineEdit);
  layout->addWidget(i2LineEdit);
  layout->addWidget(i3LineEdit);
  layout->addWidget(departmentLineEdit);
  layout->addWidget(addButton);
  setLayout(layout);

}

void GUI::populateVolunteerDep(){
  this->volunteerDepListWidget->clear();
  for(auto volunteer : repository.getVolunteersDep(department.getName())){
    volunteerDepListWidget->addItem(QString::fromStdString(volunteer.toString()));
  }
}

void GUI::populateVolunteerNonDep(){
  this->volunteerListWidget->clear();
  for(auto v: repository.getVolunteersNonDep()){
    volunteerListWidget->addItem(QString::fromStdString(v.toString()));
  }
}

void GUI::populateAll(){
  populateVolunteerDep();
  populateVolunteerNonDep();
}

void GUI::addVolunteer(){
  string name = this->nameLineEdit->text().toStdString();
  string email = this->emailLineEdit->text().toStdString();
  string i1 = this->i1LineEdit->text().toStdString();
  string i2 =this->i2LineEdit->text().toStdString();
  string i3 =this->i3LineEdit->text().toStdString();
  string dep = this->departmentLineEdit->text().toStdString();

  if(dep.size() == 0)
    dep = "none";

  if(i1.size() == 0)
    i1 = "none";
  if(i2.size() == 0)
    i2 = "none";
  if(i3.size() == 0)
    i3 = "none";

  if(name.size() == 0 || email.size() == 0){
    QMessageBox::critical(this, "Error", "ba.");
    return;
    }

    this->repository.addVolunteer(name, email, i1, i2, i3, dep);

}

void GUI::connectSignals(){
  QObject::connect(this->addButton, &QPushButton::clicked, this, &GUI::addVolunteer);
}

void GUI::update(){
  populateAll();
}

GUI::~GUI(){}
