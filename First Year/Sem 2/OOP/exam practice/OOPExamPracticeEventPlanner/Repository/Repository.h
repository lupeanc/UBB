
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Event.h"
#include "../Domain/Person.h"
#include <vector>
#include "../Observer.h"


class Repository: public Subject {
  private:
  vector<Event> events;
  vector<Person> persons;

  public:
    Repository(){LoadData();}
    void LoadData();
    void writeToFile();
    vector<Event> getEvents();
    vector<Person> getPersons();
    void addEvent(Event e);
    ~Repository() = default;

};



#endif //REPOSITORY_H
