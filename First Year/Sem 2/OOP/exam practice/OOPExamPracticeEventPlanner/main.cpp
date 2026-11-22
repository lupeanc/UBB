#include <QApplication>
#include <QPushButton>
#include "Repository/Repository.h"
#include "GUI/GUI.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    Repository repo;

    for (auto p: repo.getPersons()) {
        GUI *gui = new GUI(repo, p);
        repo.addObserver(gui);
        gui->show();
    }

    return QApplication::exec();
}