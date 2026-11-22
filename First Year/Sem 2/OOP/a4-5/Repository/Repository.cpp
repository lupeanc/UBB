#include "Repository.h"
#include "Repository.h"
#include <string>
using namespace std;

// void::initRepo() {
//
// }
Repository::Repository(DynamicArray<Event>* dynamic_array) {
    this->events = dynamic_array;
}

DynamicArray<Event>*Repository::getDynamicArray() {
    return this->events;
}

int Repository::getSize() {
    return this->events->GetSize();
}

void Repository::initRepo() {
    addRepo("HumanBody", "Biology", Date(1, 2, 2025), 12, 100, "https://en.wikipedia.org/wiki/Organ_%28biology%29");
    addRepo("IT:Websites", "Informatics", Date(23, 12, 2025), 16, 200, "https://www.wix.com/website/design");
    addRepo("RealNumbers", "Mathematics", Date(30, 4, 2025), 10, 70, "www.cuemath.com/numbers/real-numbers/#:~:text=What%20are%20Real%20Numbers%20in,so%20on%20are%20real%20numbers.");
    addRepo("DrawingFundamentals", "Arts", Date(18, 4, 2025), 20, 130, "https://juliabausenhardt.com/how-to-draw-anything-learn-sketching-for-beginners/");
    addRepo("PsychologicalNeeds", "Psychology", Date(21, 4, 2025), 13, 80, "https://www.ljmu.ac.uk/microsites/promoting-healthy-weight-in-pre-school-children/modules/communicating-with-parents/universal-psychological-needs#:~:text=According%20to%20SDT%20there%20are,hunger%2C%20thirst%2C%20sleep).");
}

int Repository::addRepo(string title, string description, Date date, int time, int attandance, string link) {
    int pos;
    pos = checkExistance(title);
    if(pos == -1) {
        Event e(title, description, date, time, attandance, link);
        this->events->Add(e);
        return 0;
    }
    return 1;
}

int Repository::checkExistance(string title) {
    for (int i = 0; i < this->events->GetSize(); i++) {
        if ((*this->events)[i].getTitle() == title) {
            return i;
        }
    }
    return -1;
}

int Repository::deleteEvent(string title) {
    int pos = checkExistance(title);
    if(pos != -1) {
        this->events->Delete(pos);
        return 0;
    }
    else
        return 1;
}

int Repository::updateEventString(string title, string newText, int command) {
    int pos = checkExistance(title);
    if(pos != -1) {
        if (command == 1) {
            string description = (*this->events)[pos].getDescription();
            Date date = (*this->events)[pos].getDate();
            int time = (*this->events)[pos].getTime();
            int attandance = (*this->events)[pos].getAttendance();
            string link = (*this->events)[pos].getLink();
            Event e(newText, description, date, time, attandance,link);
            this->events->Update(e, pos);
            return 0;
        }
        if (command == 2) {
            Date date = (*this->events)[pos].getDate();
            int time = (*this->events)[pos].getTime();
            int attandance = (*this->events)[pos].getAttendance();
            string link = (*this->events)[pos].getLink();
            Event e(title, newText, date, time, attandance, link);
            this->events->Update(e, pos);
            return 0;
        }

        if (command == 6) {
            string description = (*this->events)[pos].getDescription();
            Date date = (*this->events)[pos].getDate();
            int time = (*this->events)[pos].getTime();
            int attandance = (*this->events)[pos].getAttendance();
            Event e(title, description, date, time, attandance,newText);
            this->events->Update(e, pos);
            return 0;
        }

    }
    return 1;
}

int Repository::updateEventInt(string title, int newInt, int command) {
    int pos = checkExistance(title);
    if(pos != -1) {
        if (command == 4) {
            string description = (*this->events)[pos].getDescription();
            Date date = (*this->events)[pos].getDate();
            int attandance = (*this->events)[pos].getAttendance();
            string link = (*this->events)[pos].getLink();
            Event e(title, description, date, newInt, attandance, link);
            this->events->Update(e, pos);
            return 0;
        }
        if (command == 5) {
            string description = (*this->events)[pos].getDescription();
            Date date = (*this->events)[pos].getDate();
            int time = (*this->events)[pos].getTime();
            string link = (*this->events)[pos].getLink();
            Event e(title, description, date, time, newInt, link);
            this->events->Update(e, pos);
            return 0;
        }
    }
    return 1;
}

int Repository::updateEventDate(string title, int day, int month, int year) {
    int pos = checkExistance(title);
    if(pos != -1) {
        Date date(day, month, year);
        string description = (*this->events)[pos].getDescription();
        int time = (*this->events)[pos].getTime();
        int attendance = (*this->events)[pos].getAttendance();
        string link = (*this->events)[pos].getLink();
        Event e(title, description, date, time, attendance, link);
        this->events->Update(e, pos);
        return 0;
    }
    return 1;
}



Repository::~Repository() {
    delete this->events;
}
