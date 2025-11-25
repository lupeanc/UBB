#include <QApplication>
#include <QPushButton>

#include "GUI/GUI.h"
#include "Repository/Repository.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    Repository repo;
    GUI gui(repo);

    gui.show();

    return app.exec();
}
