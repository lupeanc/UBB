
#ifndef BP_H
#define BP_H
#include "Measurement.h"

class BP:public Measurement{
  private:
    int sistval;
    int diasval;

    public:
      BP();
      BP(string date, int sistva, int diasval);
      string toString() override;
      ~BP();
};

#endif //BP_H
