
#ifndef EVENT_H
#define EVENT_H
#include <iostream>
using namespace std;


class Event {
  private:
    string organiser, name, desc, date;
    int xloc, yloc;

    public:
      Event(){}
      Event(string organiser, string name, string desc, int xloc, int yloc, string date) {
        this->organiser = organiser;
        this->name = name;
        this->desc = desc;
        this->xloc = xloc;
        this->yloc = yloc;
        this->date = date;
      }
      string toString();
      string toStringWindow();
      string getDate(){
        return date;
      }
      string getOrganiser(){
        return organiser;
      }
      string getName() {
            return name;
          }
      int getXloc() {
            return xloc;
          }
      int getYloc() {
            return yloc;
          }
      ~Event(){}

};



#endif //EVENT_H
