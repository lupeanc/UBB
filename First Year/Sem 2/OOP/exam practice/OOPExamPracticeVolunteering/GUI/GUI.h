
#ifndef GUI_H
#define GUI_H
#include <QApplication>
#include <QWidget>
#include <QListWidget>
#include "../Repository/Repository.h"
#include <QVBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QLineEdit>
#include "../Observer.h"

class GUI: public QWidget, public Observer {
  private:
    Repository repository;
    Department department;
    QVBoxLayout *layout;
    QLabel *label;
    QListWidget *volunteerDepListWidget, *volunteerListWidget;
    QPushButton *addButton;
    QLineEdit *nameLineEdit, *emailLineEdit, *i1LineEdit, *i2LineEdit, *i3LineEdit, *departmentLineEdit;

  public:
    GUI(Department d, Repository repository);
    void init_GUI();
    void populateVolunteerDep();
    void populateVolunteerNonDep();
    void populateAll();
    void addVolunteer();
    void connectSignals();

    void update() override;

    ~GUI();


};



#endif //GUI_H
