#include <QApplication>
#include <QPushButton>
#include "Repository/Repository.h"
#include "GUI/GUI.h"
#include "GUI/GUICompany.h"
int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    Repository repo;

    GUICompany *guiCompany = new GUICompany(repo);
    repo.addObserver(guiCompany);
    guiCompany->show();

    for (auto c: repo.getCouriers()) {
        GUI *gui = new GUI(repo, c);
        repo.addObserver(gui);
        gui->show();
    }


    return QApplication::exec();
}