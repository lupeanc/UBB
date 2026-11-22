
#ifndef CONSOLE_H
#define CONSOLE_H
#pragma once
#include <windows.h>
#include "../Service/Service.h"
#include "../Validator/Validator.h"
// #include <windows.h>
// #include <shellapi.h>
#include "../Exceptions/Exceptions.h"
#include "../AbstractEventsList/AbstractEventsList.h"
#include "../HTMLRepository/HTMLRepository.h"
#include "../CSVRepository/CSVRepository.h"

class Console {
    private:
        Service& service;
        Validator* validator;
        AbstractEventsList* eventsList;

    public:
        Console();
        Console(Service& service, Validator* validator);
        // Console(Service& s);
        void Start(); // 1. admin 2. user

        void AdminMode(); // 1. add 2. delete 3. update 4.display ->DELETE FROM USER AS WELL
        void AddAdmin();
        void DeleteAdmin();
        void UpdateAdmin();
        void DisplayAdminList(); //shows them all at once

        void UserMode(); //1. ur list 2. list of events

        void UsersOwnListMenu();
        void DisplayUserList(); //shows them one by one
        void DisplayUserListMonth(int month); //shows them one by one
        void DisplayUserListAllAtOnce();
        void DisplayUserListAll();

    void openApp();


        // ~Console();
  };
#endif //CONSOLE_H
