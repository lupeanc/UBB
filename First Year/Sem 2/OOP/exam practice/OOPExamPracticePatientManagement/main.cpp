#include <QApplication>
#include <QPushButton>
#include "Repository/Repository.h"
#include "GUI/GUI.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    // QPushButton button("Hello world!", nullptr);
    // button.resize(200, 100);
    // button.show();
    Repository repository;
    for (auto d: repository.getDoctors()) {
        //!!! MUST BE POINTER!!!
        GUI* gui =  new GUI(repository, d);
        repository.addObserver(gui);
        gui->show();
    }

    // cout<<repository.getDoctors().size();
    return QApplication::exec();

}