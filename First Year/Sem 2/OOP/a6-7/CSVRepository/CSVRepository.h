
#ifndef CSVREPOSITORY_H
#define CSVREPOSITORY_H
#include <windows.h>
#include "../AbstractEventsList/AbstractEventsList.h"
#include "../Domain/Event.h"
#include <iostream>
using namespace std;
#include <vector>

class CSVRepository : public AbstractEventsList {
  private:
    vector<Event> elements;
    string fileName;

    public:
      CSVRepository();
      void write() override;
      void open() override;
      void set_data(vector<Event> elements) override;
      ~CSVRepository() override =  default;
};


#endif //CSVREPOSITORY_H
