#include <QApplication>
#include <QPushButton>
#include "Repository/Repository.h"
#include "GUI/GUI.h"
#include "GUI/GUIParticipant.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    Repository repository;

    for (auto p: repository.getParticipants()) {
        GUIParticipant *guiP = new GUIParticipant(repository, p);
        repository.addObserver(guiP);
        guiP->show();
    }

    GUI *gui = new GUI(repository);
    repository.addObserver(gui);
    gui->show();

    return QApplication::exec();
}