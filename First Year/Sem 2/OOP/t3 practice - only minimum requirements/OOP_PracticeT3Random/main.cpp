#include <QApplication>
#include <QPushButton>
#include "Repository/Repository.h"
#include "GUI/GUI.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    Repository repo;
    GUI gui(repo);

    gui.show();

    return app.exec();
}