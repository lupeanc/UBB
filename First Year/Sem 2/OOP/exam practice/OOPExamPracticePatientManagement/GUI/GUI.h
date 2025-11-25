
#ifndef GUI_H
#define GUI_H
#include <QWidget>
#include <QListWidget>
#include "../Repository/Repository.h"
#include <QLayout>
#include <QLabel>
#include <QCheckBox>
#include <QPushButton>
#include <QLineEdit>
#include "../Observer.h"


class GUI: public Observer, public QWidget {
  private:
    Repository repo;
    Doctor d;

    QListWidget *patientListWidget, *undiagnosedListWidget;
    QVBoxLayout *layout;
    QLabel *specLabel;
    QCheckBox *checkBox;
    QPushButton *addPatientPushButton, *updateButton;
    QLineEdit *nameLineEdit, *admissionDateLineEdit, *diagnosisLineEdit, *specializationLineEdit, *doctorLineEdit;


   public:
     GUI(Repository repository, Doctor d);
     void initGUI();
     void populatePatients();
     void populateUndiagnosed();

    void populatePatientsByDoctor();

    void addPatient();

    void updatePatient();

    void connectSignals();

    void update() override;
     ~GUI()=default;


};



#endif //GUI_H
