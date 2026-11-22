
#include "GUISecondWindow.h"
#include <QVBoxLayout>
GUISecondWindow::GUISecondWindow(Repository repository){
  repository = repository;
  initGUI();
  populate();
}

void GUISecondWindow::initGUI(){
  QVBoxLayout *layout = new QVBoxLayout();
  this->listWidget = new QListWidget();

  layout->addWidget(this->listWidget);
  setLayout(layout);

}

void GUISecondWindow::populate(){
  this->listWidget->clear();

  for(auto d: repository.getDepNrVol()){
    this->listWidget->addItem(QString::fromStdString(d.toString()));
}
}
