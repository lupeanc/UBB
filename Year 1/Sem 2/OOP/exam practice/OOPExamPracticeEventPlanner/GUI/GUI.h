
#ifndef GUI_H
#define GUI_H
#include <QWidget>
#include "../Repository/Repository.h"
#include <QLabel>
#include <QListWidget>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLineEdit>
#include <QCheckBox>
#include "../Observer.h"

class GUI: public QWidget, public Observer {
  private:
    Repository repo;
    Person p;

    QVBoxLayout *layout;
    QLabel *label;
    QListWidget *eventListWidget;
    QLineEdit *nameLineEdit, *descLineEdit, *xlocLineEdit, *ylocLineEdit, *dateLineEdit;
    QPushButton *addButton;
    QCheckBox *checkBox;

    public:
      GUI(Repository repo, Person p);
      void initGUI();
      void populateEvents();
      void addEvent();
        void eventsNearYou();
      void connectSignals();
      void update() override;
      ~GUI() = default;

};



#endif //GUI_H
