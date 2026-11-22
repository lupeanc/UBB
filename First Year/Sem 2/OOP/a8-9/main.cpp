#include <windows.h>
#include <QApplication>
#include <QPushButton>
#include "GUI/GUI.h"
#include <iostream>
#include <string>
#include "Repository/Repository.h"
#include "DynamicArray.h"
#include "Domain/Event.h"
#include "Validator/Validator.h"
#include "Service/Service.h"
#include "Console/Console.h"
#include "Tests/test_domain.h"
#include "Tests/test_dyn_arr.h"
#include "Tests/test_repo.h"
#include "Tests/test_service.h"
#include "Tests/test_validation.h"
#include "FileRepository/FileRepository.h"
#include "Exceptions/Exceptions.h"
#include <vector>
#include "AbstractEventsList/AbstractEventsList.h"
#include "HTMLRepository/HTMLRepository.h"
using namespace std;

int main(int argc, char *argv[]) {
    // QApplication a(argc, argv);
    // QPushButton button("Hello world!", nullptr);
    // button.resize(200, 100);
    // button.show();
    // return QApplication::exec();

    QApplication a(argc, argv);
    Validator* validator = new Validator();
    FileRepository adminRepo("F:\\c projects uni\\assignment8-9\\input.txt");
    Repository userRepo;
    Service service(adminRepo, userRepo);
    // Console console(service, validator);

    GUI gui{service};
    gui.setStyleSheet("QMainWindow {background: 'white';}");
    //    AbstractShoppingBasket* abs;
    //    UserModeGUI umg{service, abs};
    //    umg.show();

    gui.show();

    return a.exec();
}