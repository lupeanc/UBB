
#include "GUI.h"
#include <QMessageBox>

GUI::GUI(Repository repo, Driver d){
  this->repo=repo;
  this->d=d;
  initGUI();
  connectSignals();
  populateReports();
}

void GUI::initGUI(){
  this->setWindowTitle(QString::fromStdString(d.getName()));

  this->layout=new QVBoxLayout();
  this->reportListWidget=new QListWidget();
  this->label=new QLabel(QString::fromStdString(d.getAllStr()));
  this->descLineEdit=new QLineEdit();
  this->xlocLineEdit=new QLineEdit();
  this->ylocLineEdit=new QLineEdit();
  this->addButton=new QPushButton("ADD");
  this->validateButton=new QPushButton("VALIDATE");

  this->layout->addWidget(reportListWidget);
  this->layout->addWidget(label);
  this->layout->addWidget(descLineEdit);
  this->layout->addWidget(xlocLineEdit);
  this->layout->addWidget(ylocLineEdit);
  this->layout->addWidget(addButton);
  this->layout->addWidget(validateButton);
  this->setLayout(layout);
}

void GUI::populateReports(){
  this->reportListWidget->clear();

  for(auto r: repo.getReportsRegion(d)){
    QListWidgetItem *item = new QListWidgetItem(QString::fromStdString(r.toString()));

    if(r.getStatus() == true){
      QFont font;
      font.setBold(true);
      item->setFont(font);
    }
    this->reportListWidget->addItem(item);
  }
}

void GUI::addReport(){
  string desc = descLineEdit->text().toStdString();
  string xloc = xlocLineEdit->text().toStdString();
  string yloc = ylocLineEdit->text().toStdString();

  int formula = sqrt(pow((d.getXloc()-stoi(xloc)), 2)+pow((d.getYloc()-stoi(yloc)), 2));

  if(desc.size() == 0 || formula>20){
    QMessageBox::critical(this, "error", "invalid");
  }

  repo.addReport(Report(desc, d.getName(), stoi(xloc), stoi(yloc), false));

}

void GUI::validateReport(){
  int a;
  //nu mai am chef :))))))
}

void GUI::connectSignals(){
  QObject::connect(this->addButton, &QPushButton::clicked, this, &GUI::addReport);
  QObject::connect(this->validateButton, &QPushButton::clicked, this, &GUI::validateReport);
}

void GUI::update(){
  populateReports();
}