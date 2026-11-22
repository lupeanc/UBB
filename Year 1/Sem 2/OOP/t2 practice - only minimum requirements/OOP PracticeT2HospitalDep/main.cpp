#include <iostream>
using namespace std;
#include "Console.h"
#include "Controller.h"

//35 mins

int main() {
    Controller controller;
    // controller.initDepartment();
    Console console(controller);
    console.mainMenu();
    return 0;
}