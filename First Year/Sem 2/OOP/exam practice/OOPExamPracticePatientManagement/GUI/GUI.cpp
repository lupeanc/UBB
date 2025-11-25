
#include "GUI.h"
#include "QMessageBox"

GUI::GUI(Repository repository, Doctor d){
  this->repo = repository;
  this->d = d;
  initGUI();
  populatePatients();
  populateUndiagnosed();
  connectSignals();
}

void GUI::initGUI(){
  //INIT THE Q OBJECTS
  this->setWindowTitle(QString::fromStdString(this->d.getName()));

  this->layout = new QVBoxLayout();

  this->patientListWidget = new QListWidget();
  this->undiagnosedListWidget = new QListWidget();

  this->specLabel = new QLabel();
  specLabel->setText(QString::fromStdString(this->d.getSpecialization()));

  this->checkBox = new QCheckBox();

  this->nameLineEdit = new QLineEdit();
  this->admissionDateLineEdit = new QLineEdit();
  this->diagnosisLineEdit = new QLineEdit();
  this->specializationLineEdit = new QLineEdit();
  this->doctorLineEdit = new QLineEdit();
  this->addPatientPushButton = new QPushButton();
  addPatientPushButton->setText("ADD");

  this->updateButton = new QPushButton();
  this->updateButton->setText("UPDATE");

  //LAYOUT
  layout->addWidget(specLabel);

  layout->addWidget(patientListWidget);
  layout->addWidget(undiagnosedListWidget);

  layout->addWidget(checkBox);

  layout->addWidget(nameLineEdit);
  layout->addWidget(admissionDateLineEdit);
  layout->addWidget(diagnosisLineEdit);
  layout->addWidget(specializationLineEdit);
  layout->addWidget(doctorLineEdit);
  layout->addWidget(addPatientPushButton);

  layout->addWidget(updateButton);

  setLayout(layout);

}

void GUI::populatePatients(){
  this->patientListWidget->clear();
  cout<<"got here"<<endl;

  for(auto p: repo.getPatientsBySpecialization(d.getSpecialization())) {
    if(p.getCurrentDr() == d.getName()){
      QListWidgetItem *item = new QListWidgetItem(QString::fromStdString(p.toString()));
      item->setBackground(Qt::green);
      patientListWidget->addItem(item);
    }
    else
      patientListWidget->addItem(QString::fromStdString(p.toString()));
//    patientListWidget->addItem(QString::fromStdString(p.toString()));
//    if(p.getCurrentDr() == d.getName())
//      patientListWidget;
  }

}
void GUI::populateUndiagnosed(){
  this->undiagnosedListWidget->clear();
  cout<<"undiag"<<endl;

  for(auto p: repo.getPatientsUndiagnosed()) {
    undiagnosedListWidget->addItem(QString::fromStdString(p.toString()));
  }

}

void GUI::populatePatientsByDoctor(){
  this->patientListWidget->clear();

  if(checkBox->isChecked()){
    for(auto p: repo.getPatientsBySpecialization(d.getSpecialization())) {
      if(p.getCurrentDr() == d.getName()){
        QListWidgetItem *item = new QListWidgetItem(QString::fromStdString(p.toString()));
        item->setBackground(Qt::green);
        patientListWidget->addItem(item);
      }
    }
  }
  else
    populatePatients();
}

void GUI::addPatient(){
  string name = this->nameLineEdit->text().toStdString();
  string admissionDate = this->admissionDateLineEdit->text().toStdString();
  string diagnosis = this->diagnosisLineEdit->text().toStdString();
  string specialization = this->specializationLineEdit->text().toStdString();
  string currentDr = this->doctorLineEdit->text().toStdString();

  if(name.size()==0 || admissionDate<"2025.1.1"){
    QMessageBox::critical(this, "Error", "bro come on.");
  return;
  }

  this->repo.addPatient(name, admissionDate, diagnosis, specialization, currentDr);
//  populatePatients();

}

void GUI::updatePatient(){
  string name=nameLineEdit->text().toStdString();
  string diagnosis = this->diagnosisLineEdit->text().toStdString();
  string specialization = this->specializationLineEdit->text().toStdString();

  vector<Patient> patients = repo.getPatients();

  if(diagnosis == "undiagnosed")
    QMessageBox::critical(this, "Error", "u want people to die?");

  for(auto p: patients){
    if(p.getName()==name){
      if(p.getCurrentDr() == d.getName() || p.getDiagnosis() == "undiagnosed"){
        if(diagnosis.size()>0)
          this->repo.updatePatient(name, "diagnosis", diagnosis);
        if(specialization.size()>0)
              this->repo.updatePatient(name, "specialization", specialization);
      }
      break;
    }
  }
//  populatePatients();
}




void GUI::connectSignals(){
  QObject::connect(this->checkBox, &QCheckBox::toggled, this, &GUI::populatePatientsByDoctor);
  QObject::connect(this->addPatientPushButton, &QPushButton::clicked, this, &GUI::addPatient);
  QObject::connect(this->updateButton, &QPushButton::clicked, this, &GUI::updatePatient);

}

void GUI::update(){
  cout<<"cedrq"<<endl;
  patientListWidget->clear();
  undiagnosedListWidget->clear();
  this->populatePatients();
  this->populateUndiagnosed();
  this->populatePatientsByDoctor();

}