#include <QApplication>
#include <QPushButton>
#include "Repository/Repository.h"
#include "GUI/GUI.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    Repository repo;

    for (auto d: repo.getDrivers()) {
        GUI *gui = new GUI(repo, d);
        gui->setStyleSheet("background-color: red");
        repo.addObserver(gui);
        gui->show();
    }

    return QApplication::exec();
}