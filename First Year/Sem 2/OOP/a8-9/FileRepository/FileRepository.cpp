
#include "FileRepository.h"

FileRepository::FileRepository(string fileName) {
  this->fileName = fileName;
  this->elements = loadData();
}

void FileRepository::addRepo(string title, string description, Date date, int time, int attendance, string link) {

    int position;
    position = this->checkExistence(title);
    if(position != -1)
    {
      throw ExceptionsRepository{"The event already exists."};
        // return 1;
    }
    else
    {
        Event e(title, description, date, time, attendance, link);
        elements.push_back(e);
        writeData();
        // return 0;
    }
}

void FileRepository::deleteEvent(string title) {
    int position = this->checkExistence(title);
    if(position != -1)
    {
        elements.erase(elements.begin() + position);
        writeData();
        // return 0;
    }
    else
        throw ExceptionsRepository{"The event doesn't exist."};
        // return 1;
}

void FileRepository::updateEventString(string title, string newText, int command) {
    int position = this->checkExistence(title);
    if(position != -1)
    {
      if (command == 1) {
        string description = elements[position].getDescription();
        Date date = elements[position].getDate();
        int time = elements[position].getTime();
        int attandance = elements[position].getAttendance();
        string link = elements[position].getLink();
        Event e(newText, description, date, time, attandance,link);
        elements[position] = e;
        writeData();

        // return 0;
        }

        if (command == 2) {
            Date date = elements[position].getDate();
            int time = elements[position].getTime();
            int attandance = elements[position].getAttendance();
            string link = elements[position].getLink();
            Event e(title, newText, date, time, attandance, link);
            elements[position] = e;
            writeData();

            // return 0;
        }

        if (command == 6) {
            string description = elements[position].getDescription();
            Date date = elements[position].getDate();
            int time = elements[position].getTime();
            int attandance = elements[position].getAttendance();
            Event e(title, description, date, time, attandance,newText);
            elements[position] = e;
            writeData();

            // return 0;
        }
     }
    else
        throw ExceptionsRepository{"The event doesn't exist."};
    // return 1;
}


    void FileRepository::updateEventInt(string title, int newInt, int command) {
        int pos = checkExistence(title);
        if(pos != -1) {
            if (command == 4) {
                string description = elements[pos].getDescription();
                Date date = elements[pos].getDate();
                int attandance = elements[pos].getAttendance();
                string link = elements[pos].getLink();
                Event e(title, description, date, newInt, attandance, link);
                elements[pos] = e;
                writeData();
                // return 0;
            }
            if (command == 5) {
                string description = elements[pos].getDescription();
                Date date = elements[pos].getDate();
                int time = elements[pos].getTime();
                string link = elements[pos].getLink();
                Event e(title, description, date, time, newInt, link);
                elements[pos] = e;
                writeData();
                // return 0;
            }
        }
        else
            throw ExceptionsRepository{"The event doesn't exist."};
        // return 1;
    }

void FileRepository::updateEventDate(string title, int day, int month, int year) {
    int pos = checkExistence(title);
    if(pos != -1) {
        Date date(day, month, year);
        string description = elements[pos].getDescription();
        int time = elements[pos].getTime();
        int attendance = elements[pos].getAttendance();
        string link = elements[pos].getLink();
        Event e(title, description, date, time, attendance, link);
        elements[pos] = e;
        writeData();
        // return 0;
    }
    else
        throw ExceptionsRepository{"The event doesn't exist."};
    // return 1;
}

int FileRepository::checkExistence(string title) {
    getEvent(0);
    for(int i = 0; i < elements.size(); i++)
        if(elements[i].getTitle() == title)
            return i;
    return -1;
}

int FileRepository::getSize() {
    return elements.size();
}

void FileRepository::writeData() {

    ofstream fout(this->fileName);
    for(auto CurrentElement: this->elements)
    {
        fout << CurrentElement<<'\n';
    }
}

vector<Event> FileRepository::loadData() {
    ifstream fin(this->fileName);
    vector<Event> elements;
    Event CurrentElement;
    while (fin >> CurrentElement)
    {
        elements.push_back(CurrentElement);
    }
    return elements;
}

const vector<Event> &FileRepository::getDynArr() {
    return elements;
}

Event FileRepository::getEvent(int position) {
    vector<Event> elements = loadData();
    // if (elements.size() <= position)

    return elements[position];
}
