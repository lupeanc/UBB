
#ifndef EVENT_H
#define EVENT_H
#include <string>
#include "Date.h"
#include <istream>
#pragma once
using namespace std;
//TODO IF SHIT NO WORK, ADD POINTER TO Date
class Event{
    private:
        string title;
        string description;
        Date date;
        int time;
        int attendance;
        string link;

    public:
    //constructors
        Event();

        Event(string title, string description, Date date, int time, int attendance, string link);

    // Gets the title from the struct Event and returns it
        string getTitle();
    // Gets the description from the struct Event and returns it
        string getDescription();
    // Gets the date from the struct Event and returns it
        Date getDate();
    // Gets the date from the struct Event and returns it as a string
        string getDateString();
    // Gets the time from the struct Event and returns it
        int getTime();
    // Gets the attendance from the struct Event and returns it
        int getAttendance();
    // Gets the link from the struct Event and returns it
        string getLink();
    //Sets the title for a struct type Event; param = new value for title
        void setTitle(string newTitle);
    //Sets the description for a struct type Event; param = new value for description
        void setDescription(string newDescription);
    //Sets the time for a struct type Event; param = new value for time
        void setTime(int newTime);
    //Sets the attendance for a struct type Event; param = new value for attendance
        void setAttendance(int newAttendance);
    //Sets the link for a struct type Event; param = new value for link
        void setLink(string newLink);

};
#endif //EVENT_H
