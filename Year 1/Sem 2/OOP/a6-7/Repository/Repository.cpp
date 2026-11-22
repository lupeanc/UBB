#include "Repository.h"
#include "Repository.h"
#include <string>
#include <utility>
using namespace std;

Repository::Repository() {}


int Repository::getSize() {
    return elements.size();
}

const vector<Event>& Repository::getDynArr() {
    return this->elements;
}

void Repository::initRepo() {
    addRepo("HumanBody", "Biology", Date(1, 2, 2025), 12, 100, "https://en.wikipedia.org/wiki/Organ_%28biology%29");
    addRepo("IT:Websites", "Informatics", Date(23, 12, 2025), 16, 200, "https://www.wix.com/website/design");
    addRepo("RealNumbers", "Mathematics", Date(30, 4, 2025), 10, 70, "www.cuemath.com/numbers/real-numbers/#:~:text=What%20are%20Real%20Numbers%20in,so%20on%20are%20real%20numbers.");
    addRepo("DrawingFundamentals", "Arts", Date(18, 4, 2025), 20, 130, "https://juliabausenhardt.com/how-to-draw-anything-learn-sketching-for-beginners/");
    addRepo("PsychologicalNeeds", "Psychology", Date(21, 4, 2025), 13, 80, "https://www.ljmu.ac.uk/microsites/promoting-healthy-weight-in-pre-school-children/modules/communicating-with-parents/universal-psychological-needs#:~:text=According%20to%20SDT%20there%20are,hunger%2C%20thirst%2C%20sleep).");
}

void Repository::addRepo(string title, string description, Date date, int time, int attandance, string link) {
    int pos;
    pos = checkExistence(title);
    if(pos == -1) {
        Event e(title, description, date, time, attandance, link);
        this->elements.push_back(e);
        // return 0;
    }
    // else throw ExceptionsRepository{"The event already exists."};
    // return 1;

}

int Repository::checkExistence(string title) {
    for (int i = 0; i < this->elements.size(); i++) {
        if ((this->elements)[i].getTitle() == title) {
            return i;
        }
    }
    return -1;
}

void Repository::deleteEvent(string title) {
    int pos = checkExistence(title);
    if(pos != -1) {
        this->elements.erase(this->elements.begin() + pos);
        // return 0;
    }
    else
        throw ExceptionsRepository{"The event does not exist."};
        // return 1;
}

void Repository::updateEventString(string title, string newText, int command) {
    int position = checkExistence(title);
    if(position != -1) {
        if (command == 1) {
            string description = elements[position].getDescription();
            Date date = elements[position].getDate();
            int time = elements[position].getTime();
            int attandance = elements[position].getAttendance();
            string link = elements[position].getLink();
            Event e(newText, description, date, time, attandance,link);
            this->elements[position] = e;
            // return 0;
        }
        if (command == 2) {
            Date date = elements[position].getDate();
            int time = elements[position].getTime();
            int attandance = elements[position].getAttendance();
            string link = elements[position].getLink();
            Event e(title, newText, date, time, attandance, link);
            this->elements[position] = e;
            // return 0;
        }

        if (command == 6) {
            string description = elements[position].getDescription();
            Date date = elements[position].getDate();
            int time = elements[position].getTime();
            int attandance = elements[position].getAttendance();
            Event e(title, description, date, time, attandance,newText);
            this->elements[position] = e;
            // return 0;
        }

    }
    else
        throw ExceptionsRepository{"The event does not exist."};
    // return 1;
}

void Repository::updateEventInt(string title, int newInt, int command) {
    int pos = checkExistence(title);
    if(pos != -1) {
        if (command == 4) {
            string description = elements[pos].getDescription();
            Date date = elements[pos].getDate();
            int attandance = elements[pos].getAttendance();
            string link = elements[pos].getLink();
            Event e(title, description, date, newInt, attandance, link);
            elements[pos] = e;
            // return 0;
        }
        if (command == 5) {
            string description = elements[pos].getDescription();
            Date date = elements[pos].getDate();
            int time = elements[pos].getTime();
            string link = elements[pos].getLink();
            Event e(title, description, date, time, newInt, link);
            elements[pos] = e;
            // return 0;
        }
    }
    else
        throw ExceptionsRepository{"The event does not exist."};
    // return 1;
}

void Repository::updateEventDate(string title, int day, int month, int year) {
    int pos = checkExistence(title);
    if(pos != -1) {
        Date date(day, month, year);
        string description = elements[pos].getDescription();
        int time = elements[pos].getTime();
        int attendance = elements[pos].getAttendance();
        string link = elements[pos].getLink();
        Event e(title, description, date, time, attendance, link);
        elements[pos] = e;
        // return 0;
    }
    else
        throw ExceptionsRepository{"The event does not exist."};
    // return 1;
}

//Repository::~Repository() {
//    delete this->events;
//}
