
#ifndef CONSOLE_H
#define CONSOLE_H
#include "Service.h"

class Console{
  private:
    Service service;
  public:
    Console();
    ~Console();
    Console(Service service);
    void mainMenu();
    void addMenu();
    void displayMenu();


};


#endif //CONSOLE_H
