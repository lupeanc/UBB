#include "Event.h"

Event::Event(){}
// Date* if shit hits the fan
Event::Event(string title, string description, Date date, int time, int attendance, string link){
  this->title = title;
  this->description = description;
  this->date = date;
  this->time = time;
  this->attendance = attendance;
  this->link =  link;

}

string Event::getTitle(){
  return this->title;
}
string Event::getDescription(){
  return this->description;
}
Date Event::getDate(){
  return this->date;
}
string Event::getDateString() {
  return this->date.toString();
}

int Event::getTime(){
  return this->time;
}
int Event::getAttendance(){
  return this->attendance;
}

string Event::getLink() {
  return this->link;
}

void Event::setTitle(string newTitle){
  this->title = newTitle;
}
void Event::setDescription(string newDescription){
  this->description = newDescription;
}

void Event::setTime(int newTime){
  this->time = newTime;
}
void Event::setAttendance(int newAttendance){
  this->attendance = newAttendance;
}
void Event::setLink(string newLink) {
  this->link = newLink;
}


