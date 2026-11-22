
#ifndef GUI_H
#define GUI_H
#include "QListWidget"
#include "../Repository/Repository.h"


class GUI: public QWidget {
  private:
    Repository repo;
    QListWidget* listWidget;

    public:
      GUI(Repository repo);
      ~GUI();
      void init_GUI();
      void populateList(vector <Pizza> pizzas);

};



#endif //GUI_H
