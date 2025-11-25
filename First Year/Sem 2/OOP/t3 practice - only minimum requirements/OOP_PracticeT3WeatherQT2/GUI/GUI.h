
#ifndef GUI_H
#define GUI_H
#include "QtWidgets"
#include "QListWidget"
#include "../Repository/Repository.h"


class GUI: public QWidget {
    // Q_OBJECT
private:
    Repository repo;
    QListWidget* list;

public:
    GUI(Repository repo);
    ~GUI();
    void init();
    void populateList(vector <Weather> elements);

};



#endif //GUI_H
