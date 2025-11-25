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

const string Event::getTitle(){
  return this->title;
}
const string Event::getDescription(){
  return this->description;
}
 Date Event::getDate(){
  return this->date;
}
const string Event::getDateString() {
  return this->date.toString();
}

const int Event::getTime(){
  return this->time;
}
const int Event::getAttendance(){
  return this->attendance;
}

const string Event::getLink() {
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

//TODO IN CASE OF ERROR: I CHANGED THE PRIVATE ATTRIBUTES OF DATE TO PUBLIC SO I CAN USE THEM HERE
ostream &operator<<(ostream &output, const Event &e) {
  output<<e.title<<" "<<e.description<<" "<<e.date.day<<" "<<e.date.month<<" "<<e.date.year<<" "<<e.time<<" "<<e.attendance<<" "<<e.link;
  return output;
}

istream &operator>>(istream &input, Event &e) {
  input>>e.title>>e.description>>e.date.day>>e.date.month>>e.date.year>>e.time>>e.attendance>>e.link;
  return input;
}

