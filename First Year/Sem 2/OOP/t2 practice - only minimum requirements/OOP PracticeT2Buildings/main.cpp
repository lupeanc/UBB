#include "Console.h"
#include "Controller.h"

//45 ca-s prost si nu le-am luat un ordine
int main() {
    Controller controller;
    controller.initController();
    Console console(controller);
    console.mainMenu();
    return 0;
}