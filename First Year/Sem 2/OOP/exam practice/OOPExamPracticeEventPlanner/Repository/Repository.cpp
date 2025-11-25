
#include "Repository.h"
#include <fstream>
#include <algorithm>

void Repository::LoadData(){
  ifstream finE(R"(F:\c projects uni\OOPExamPracticeEventPlanner\events)");
  string organiser, name, desc, date;
  int xloc, yloc;

  events.clear();
  while(finE>>organiser>>name>>desc>>xloc>>yloc>>date){
    events.push_back(Event(organiser, name, desc, xloc, yloc, date));
  }
  finE.close();

  ifstream finP(R"(F:\c projects uni\OOPExamPracticeEventPlanner\persons)");
  string status;

  persons.clear();
  while(finP>>name>>xloc>>yloc>>status){
    if(status == "true")
      persons.push_back(Person(name, xloc, yloc, true));
    else
      persons.push_back(Person(name, xloc, yloc, false));
  }
  finP.close();

}

bool compare(Event e1, Event e2){
  return e1.getDate()<e2.getDate();
}

vector<Event> Repository::getEvents(){
  LoadData();
  std::sort(events.begin(), events.end(), compare);
  return events;
}

vector<Person> Repository::getPersons(){
  LoadData();
  return persons;
}

void Repository::writeToFile(){
  ofstream fout(R"(F:\c projects uni\OOPExamPracticeEventPlanner\events)");

  for(auto e: events){
    fout<<e.toString()<<endl;
  }
  fout.close();

  this->notify();
}

void Repository::addEvent(Event e){
  events.push_back(e);
  writeToFile();
}