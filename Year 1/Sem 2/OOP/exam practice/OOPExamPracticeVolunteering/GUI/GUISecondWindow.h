
#ifndef GUISECONDWINDOW_H
#define GUISECONDWINDOW_H
#include <QWidget>
#include <QListWidget>
#include "../Repository/Repository.h"

class GUISecondWindow: public QWidget {
  private:
    Repository repository;

    QListWidget *listWidget;

    public:
      GUISecondWindow(Repository repository);
      void initGUI();
      void populate();
      ~GUISecondWindow()=default;

};



#endif //GUISECONDWINDOW_H
