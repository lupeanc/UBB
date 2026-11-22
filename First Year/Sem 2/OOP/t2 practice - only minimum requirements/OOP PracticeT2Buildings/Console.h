
#ifndef CONSOLE_H
#define CONSOLE_H
#include "Controller.h"

class Console{
  private:
    Controller controller;

    public:
      Console();
      Console(Controller controller);
      void mainMenu();
	  void addMenu();
      void displayMenu();

      ~Console();
};

#endif //CONSOLE_H
