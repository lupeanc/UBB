
#ifndef SERVICE_H
#define SERVICE_H
#pragma once
#include "../Repository/Repository.h"
#include "../DynamicArray.h"
#include "../Domain/Event.h"
using namespace std;

class Service {
    private:
        Repository*adminRepo = nullptr;
        Repository*userRepo = nullptr;

    public:
        //constructor
        Service(Repository* adminRepo, Repository* userRepo);
        //Gets admin repo
        DynamicArray<Event>* getAdminRepo();
        //Gets user repo
        DynamicArray<Event>* getUserRepo();

    //adds elements to repo
    //title - the title of the event (one word)
    //description - the description of the event (one word)
    //date - the date of the event
    //time - the time of the event (between 0-24)
    //attendance - nb of people attending
    //link -  a link to the event
        int addServiceAdmin(string title, string description, Date date, int time, int attendance, string link);
    //deletes an event based on the title
        int deleteServiceAdmin(string title);
    //updates the string parts of the event struct (title, desc, link)
    // title - the title of the event we want to change
    //newText - the text we replace it with
    //command - what to replace
        int updateEventStringAdmin(string title, string newText, int command);
    //updates the int parts of the event struct (time, attendance)
    // title - the title of the event we want to change
    //newInt - the int we replace it with
    //command - what to replace
        int updateEventIntAdmin(string title, int newInt, int command);
    //updates the Date part of the event struct
    // title - the title of the event we want to change
    // day - new day
    // month - new month
    // year - new year
        int updateEventDateAdmin(string title, int day, int month, int year);
        //
        int addServiceUser(Event e);
        int deleteServiceAUser(Event e);

        int getSizeAdmin();
        int getSizeUser();
        ~Service();
};

#endif //SERVICE_H
