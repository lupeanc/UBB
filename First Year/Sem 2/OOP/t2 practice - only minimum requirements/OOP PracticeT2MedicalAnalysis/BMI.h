
#ifndef BMI_H
#define BMI_H
#include "Measurement.h"

class BMI:public Measurement{
private:
    double val;
public:
  BMI();
  BMI(string date, double val);
    string toString() override;
    ~BMI();
};

#endif //BMI_H
