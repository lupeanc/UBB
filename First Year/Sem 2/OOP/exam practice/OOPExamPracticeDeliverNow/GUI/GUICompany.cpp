
#include "GUICompany.h"


GUICompany::GUICompany(Repository repo){
    this->repository=repo;
    this->initGUI();
    this->populatePackages();
    this->connectSignals();
}

void GUICompany::initGUI(){
    this->setWindowTitle(QString::fromStdString("Company"));

    this->layout = new QVBoxLayout();
    this->PackageListWidget = new QListWidget();
    this->recipientLineEdit = new QLineEdit();
    this->streetLineEdit = new QLineEdit();
    this->numberLineEdit = new QLineEdit();
    this->xlocLineEdit = new QLineEdit();
    this->ylocLineEdit = new QLineEdit();
    this->addButton = new QPushButton("ADD");

    layout->addWidget(PackageListWidget);
    layout->addWidget(recipientLineEdit);
    layout->addWidget(streetLineEdit);
    layout->addWidget(numberLineEdit);
    layout->addWidget(xlocLineEdit);
    layout->addWidget(ylocLineEdit);
    layout->addWidget(addButton);
    this->setLayout(layout);

}

void GUICompany::populatePackages(){
    this->PackageListWidget->clear();

    for(auto p: repository.getPackages()){
          QListWidgetItem *item = new QListWidgetItem(QString::fromStdString(p.toString()));
          if(p.getStatus() == "1")
            item->setBackground(Qt::green);
        this->PackageListWidget->addItem(item);
    }
}

void GUICompany::addPackage(){
  string recipient = this->recipientLineEdit->text().toStdString();
  string street = this->streetLineEdit->text().toStdString();
  string number = this->numberLineEdit->text().toStdString();
  string xloc = this->xlocLineEdit->text().toStdString();
  string yloc = this->ylocLineEdit->text().toStdString();

  this->repository.addPackage(Package(recipient, street, stoi(number), stoi(xloc), stoi(yloc), false));
  populatePackages();
}

void GUICompany::connectSignals(){
  QObject::connect(this->addButton, &QPushButton::clicked, this, &GUICompany::addPackage);
}

void GUICompany::update(){
  populatePackages();
}

