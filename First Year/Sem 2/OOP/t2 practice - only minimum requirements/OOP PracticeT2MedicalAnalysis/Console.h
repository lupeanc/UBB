
#ifndef CONSOLE_H
#define CONSOLE_H
#include "Person.h"
class Console {
    private:
    Person person;

    public:
    Console();
    Console(Person person);
    void mainMenu();
    void addMenu();
    void displayMenu();
    ~Console();
};

#endif //CONSOLE_H
