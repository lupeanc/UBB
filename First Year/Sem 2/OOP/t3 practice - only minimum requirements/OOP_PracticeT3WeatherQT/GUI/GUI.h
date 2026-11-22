
#ifndef GUI_H
#define GUI_H
#include <QApplication>
#include "QWidget"
#include "QListWidget"
#include "../Repository/Repository.h"

class GUI: public QWidget {
    private:
      Repository repo;
      QListWidget *weatherListWidget;

      public:
        GUI(Repository repository);
        ~GUI();
        void init_GUI();
        void populateList(vector<weather> elements);

};



#endif //GUI_H
