
#ifndef GUI_H
#define GUI_H
#include <QWidget>
#include "../Repository/Repository.h"
#include <QVBoxLayout>
#include <QListWidget>
#include <QListWidgetItem>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>>
#include "../Observer.h"



class GUI: public QWidget, public Observer {
  private:
    Repository repo;
    Driver d;
    QVBoxLayout *layout;
    QLabel *label;
    QListWidget *reportListWidget;
    QLineEdit *descLineEdit, *xlocLineEdit, *ylocLineEdit;
    QPushButton *addButton, *validateButton;

    public:
      GUI(Repository repo, Driver d);
      void initGUI();
      void populateReports();
      void addReport();
      void validateReport();
      void connectSignals();
        void update() override;
      ~GUI()=default;

};



#endif //GUI_H
