
#ifndef CONSOLE_H
#define CONSOLE_H
#pragma once
#include "../Service/Service.h"
#include "../Validator/Validator.h"
// #include <windows.h>
// #include <shellapi.h>

class Console {
    private:
        Service* service;
        Validator* validator;

    public:
        Console();
        Console(Service* service, Validator* validator);
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


        ~Console();

    //USER
    //
    // menu: 1. ur list 2. list of events

    // 1: 1. see list 2. delete event from list 0.exit
    // 1.1: 1. all 2. specific month
        //
    // 1.2.x: 1. delete 2.next 0.exit
    //
    // 2: 1. see list 2. add event from list 0.exit
    // 2.1: 1. all 2. specific month
    // 2.2: 1. all 2. specific month
        //
    // 2.2.x: 1. add 2.next 0.exit
    // !!!!! ADD A CHECKER TO SEE IF THE EVENT IN THE events LIST IS ALSO IN THE user's LIST!!!! if yes - dont show





  };
#endif //CONSOLE_H
