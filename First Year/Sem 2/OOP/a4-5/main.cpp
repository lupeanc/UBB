// You will be given one of the problems below to solve
// The application must be implemented in C++ and use layered architecture.
// Provide tests and specifications for non-trivial functions outside the UI. Test coverage must be at least 98% for all layers,
// except the UI
// Have at least 10 entities in your memory repository
//
// Lectures, seminars and labs ... school in general must be taken seriously; BUT so must be your social life and leisure time. To manage the latter and be always informed about the interesting events happening in your city you will implement a software application. The application can be used in two modes: administrator and user. When the application is started, it will offer the option to choose the mode.
// Administrator mode: The application will have a database which holds all the interesting events in your area.
// You must be able to update the database, meaning: add a new event, delete an event and update the information of an event.
// Each Event has a title, a description, a date and time, a number of people who are going and a link towards
// the online resource containing the event. The administrators will also have the option to see all the events in the database.

// User mode: A user can create a list with the events that he/she is interested in. The application will allow the user to:
// See the events in the database for a given month (if there is no month given, see all the events, ordered chronologically), one by one. When the user chooses this option, the data of the first event (title, description, date and time, number of people who are going) is displayed, and the event is opened in the browser (e.g. Facebook event).
// If the user wants to participate in the event he/she can choose to add it to his/her events list. When this happens, the number of people who are going to the event increases (for the event in the repository).
// If the event seems uninteresting, the user can choose not to add it to the list and continue to the next. In this case, the information corresponding to the next event is shown, and the user is again offered the possibility to add it to his/her list. This can continue as long as the user wants, as when arriving to the end of the list of events for the given month, if the user chooses next, the application will again show the first event.
// Delete an event from the list. When the user deletes an event from his/her list, the number of people who are going to the event decreases.
// See the list of events the user wants to attend.

#include <iostream>
#include <string>
#include <windows.h>
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
using namespace std;

int main() {
    DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
    DynamicArray<Event>* userDA = new DynamicArray<Event>(100);

    Repository* adminRepo = new Repository(adminDA);
    Repository* userRepo = new Repository(userDA);
    adminRepo->initRepo();
    Service* service = new Service(adminRepo, userRepo);
    Validator* validator = new Validator();
    Console* console = new Console(service, validator);

    testDomain D;
    D.testAllDomain();
    Test_DynamicArray DA;
    DA.TestAllDynamicArray();
    testRepository R;
    R.testAllRepository();
    testService S;
    S.testAllService();
    testValidation V;
    V.testAllValidation();

    console->Start();
    delete console;
}

