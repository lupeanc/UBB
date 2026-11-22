
#ifndef FILEREPOSITORY_H
#define FILEREPOSITORY_H
#pragma once
#include "../Repository/Repository.h"
#include <fstream>
using namespace std;

class FileRepository: public Repository{
  private:
    string fileName;
    Event getEvent(int position);
    vector<Event> loadData();
    void writeData();

//TODO - CHANGE INT TYPES INTO VOID TYPES WHEN ADDING THE EXCEPTIONS
    public:
      FileRepository(string fileName);
      const vector<Event>& getDynArr() override;
      void addRepo(string title, string description, Date date, int time, int attendance, string link) override;
      int checkExistence(string title) override;
      void deleteEvent(string title) override;
      void updateEventString(string title, string newText, int command) override;
      void updateEventInt(string title, int newInt, int command) override;
      void updateEventDate(string title, int day, int month, int year) override;
      int getSize() override;

};

#endif //FILEREPOSITORY_H
