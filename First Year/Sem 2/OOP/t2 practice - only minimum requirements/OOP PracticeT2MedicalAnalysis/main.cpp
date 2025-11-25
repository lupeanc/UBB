#include <iostream>
using namespace std;
#include "Person.h"
#include "Console.h"

//50 mins

int main() {
Person person;
    // person.initRepo();
    Console console(person);
    console.mainMenu();
    return 0;
}