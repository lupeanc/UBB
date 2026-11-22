#include "Car.h"
#include "Console.h"

int main() {
    Service service;
    Console console(service);
    console.mainMenu();

    return 0;
}