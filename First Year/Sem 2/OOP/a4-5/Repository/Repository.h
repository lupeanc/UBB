
#ifndef REPOSITORY_H
#define REPOSITORY_H
#pragma once
#include "../DynamicArray.h"
#include "../Domain/Event.h"

class Repository {
    private:
        DynamicArray<Event>* events;
    public:
    //Constructor
    Repository(DynamicArray<Event>* dynamic_array);

    //gets the dynamic array from the repo and returns it
    DynamicArray<Event>* getDynamicArray();
    //Returns the size of the repository
    int getSize();

    //Declares a few inputs and adds them to the repo
    void initRepo();

    //adds elements to repo
    //params:
    //title - the title of the event (one word)
    //description - the description of the event (one word)
    //date - the date of the event
    //time - the time of the event (between 0-24)
    //attendance - nb of people attending
    //link -  a link to the event
    int addRepo(string title, string description, Date date, int time, int attendance, string link);

    //checks if a certain event has already been registered, if yes, it doesnt add it again
    //unique id: title
    int checkExistance(string title);
    //deletes an event based on the title
    int deleteEvent(string title);
    //updates the string parts of the event struct (title, desc, link)
    // title - the title of the event we want to change
    //newText - the text we replace it with
    //command - what to replace
    int updateEventString(string title, string newText, int command);
    //updates the int parts of the event struct (time, attendance)
    // title - the title of the event we want to change
    //newInt - the int we replace it with
    //command - what to replace
    int updateEventInt(string title, int newInt, int command);
    //updates the Date part of the event struct
    // title - the title of the event we want to change
    // day - new day
    // month - new month
    // year - new year
    int updateEventDate(string title, int day, int month, int year);

    //make repo iterable
    Event& operator [] (int index) {
        return (*this->events)[index];
    }
    //destructor
    ~Repository();
};


#endif //REPOSITORY_H
