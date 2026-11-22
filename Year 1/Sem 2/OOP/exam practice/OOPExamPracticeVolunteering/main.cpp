#include <QApplication>
#include <QPushButton>
#include <QTableView>
#include <QVBoxLayout>
#include <QStandardItemModel>
#include "Repository/Repository.h"
#include "GUI/GUI.h"
#include "GUI/GUISecondWindow.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    Repository repository;

    for (auto d: repository.getDepartments()) {
        GUI *gui = new GUI(d, repository);
        repository.addObserver(gui);
        gui->show();
    }

    GUISecondWindow *guiS = new GUISecondWindow(repository);
    guiS->show();


    return QApplication::exec();
}