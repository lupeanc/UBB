
#ifndef CONSOLE_H
#define CONSOLE_H
#include "Service.h"
#pragma once

class Console{
  private:
//    Service* service;
    Repo repo;
  public:
    // Console();
    Console(Repo repo);

    void mainMenu();
    void addMenu();
    void displayAll();
//    void start();
    ~Console();
};

#endif //CONSOLE_H
