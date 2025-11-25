#include "Domain/weather.h"
#include "Repository/Repository.h"
#include "GUI/GUI.h"
#include <QApplication>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    Repository repository;
    GUI gui(repository);

    gui.show();
    return app.exec();
}