
#include "GUI.h"
GUI::GUI(Repository repo, Courier c){
  this->repository=repo;
  this->courier=c;
  this->initGUI();
  this->populateUndeliveredAssigned();
  this->connectSignals();
}

void GUI::initGUI(){
  this->setWindowTitle(QString::fromStdString(courier.getName()));

  this->layout = new QVBoxLayout();
  this->undeliveredAssignedPackagesListWidget = new QListWidget();
  this->deliverButton = new QPushButton("DELIVER");

  layout->addWidget(undeliveredAssignedPackagesListWidget);
  layout->addWidget(deliverButton);
  this->setLayout(layout);

}

void GUI::populateUndeliveredAssigned(){
  this->undeliveredAssignedPackagesListWidget->clear();

  for(auto p: repository.getUndeliveredAssigned(this->courier)){
    this->undeliveredAssignedPackagesListWidget->addItem(QString::fromStdString(p.toString()));
  }
}

void GUI::update() {
  populateUndeliveredAssigned();
}

int GUI::getSelectedIndex() {
  QModelIndexList selectedIndices = this->undeliveredAssignedPackagesListWidget->selectionModel()->selectedIndexes();
  if (selectedIndices.empty())
    return -1;
  int selectedIndex = selectedIndices.at(0).row();
  return selectedIndex;
}

void GUI::deliverPackage() {
  int selectedIndex = getSelectedIndex();
  cout<<selectedIndex<<endl;
  if (selectedIndex == -1)
    return;
  this->repository.deliverPackage(courier, selectedIndex);
}

void GUI::connectSignals() {
  QObject::connect(this->deliverButton, &QPushButton::clicked, this, &GUI::deliverPackage);
}

