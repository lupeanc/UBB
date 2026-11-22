
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
#include "FileRepository/FileRepository.h"
#include "Exceptions/Exceptions.h"
#include <vector>
#include "AbstractEventsList/AbstractEventsList.h"
#include "HTMLRepository/HTMLRepository.h"
using namespace std;

int main() {
    Validator* validator = new Validator();

    FileRepository adminRepo("F:\\c projects uni\\assignment_6_7\\input.txt");
    // Repository adminRepo;
    // adminRepo.initRepo();

    Repository userRepo;
    Service service(adminRepo, userRepo);

    Console console(service, validator);

    // testDomain D;
    // D.testAllDomain();
    // Test_DynamicArray DA;
    // DA.TestAllDynamicArray();
    // testRepository R;
    // R.testAllRepository();
    // testService S;
    // S.testAllService();
    // testValidation V;
    // V.testAllValidation();

    console.Start();
    return 0;
}

