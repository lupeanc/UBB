
#ifndef CAR_H
#define CAR_H
#include "Engine.h"

class Car{
    private:
      string bodyStyle;
      Engine* engine;

      public:
        Car();
        Car(string bodyStyle, Engine* engine);
//        string getBodyStyle();
        ~Car() = default;
        string toString();
};

#endif //CAR_H
