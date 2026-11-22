
#ifndef GUI_H
#define GUI_H
#include <QWidget>
#include "../Repository/Repository.h"
#include <QVBoxLayout>
#include <QListWidget>
#include <QPushButton>
#include <QLineEdit>
#include "../Observer.h"


class GUI: public QWidget, public Observer {
  private:
    Repository repository;
    Programmer programmer;
    QVBoxLayout *layout;
    QListWidget *taskListWidget;
    QLineEdit *descLineEdit, *programmerLineEdit;
    QPushButton *addButton, *removeButton, *startButton, *doneButton;


    public:
      GUI(Repository repository, Programmer programmer);
      void initGUI();
      void populateTasks();
      void connectSignals();
      void addTask();
      void removeTask();
      void start();
      void done();
      void update() override;
      ~GUI()=default;

};



#endif //GUI_H
