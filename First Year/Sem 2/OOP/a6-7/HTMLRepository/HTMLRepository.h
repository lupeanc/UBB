
#ifndef HTMLREPOSITORY_H
#define HTMLREPOSITORY_H
#include <windows.h>
#include "../Repository/Repository.h"
#pragma once
#include "../AbstractEventsList/AbstractEventsList.h"

class HTMLRepository : public AbstractEventsList {

  private:
    vector<Event> elements;
    string fileName;

  public:
    HTMLRepository();
    void write() override;
    void open() override;
    void set_data(vector<Event> elements) override;
    ~HTMLRepository() override = default;

};


#endif //HTMLREPOSITORY_H
