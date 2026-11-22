
#ifndef GUI_H
#define GUI_H
#include "QListWidget"
#include "../Repository/Repository.h"


class GUI: public QWidget {
    Q_OBJECT
private:
    Repository repo;
    QListWidget *personListWidget;

public:
    GUI(Repository repo);
    ~GUI();
    void init_GUI();
    void populateList(vector<Person> elements);

};



#endif //GUI_H
