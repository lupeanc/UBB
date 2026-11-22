
#ifndef ABSTRACTEVENTSLIST_H
#define ABSTRACTEVENTSLIST_H
#include "../Domain/Event.h"
#include <vector>

class AbstractEventsList{
  public:
    virtual void write() = 0;
    virtual void open() = 0;
    virtual void set_data(vector<Event> elements) = 0;
    virtual ~AbstractEventsList() = default;
};



#endif //ABSTRACTEVENTSLIST_H
