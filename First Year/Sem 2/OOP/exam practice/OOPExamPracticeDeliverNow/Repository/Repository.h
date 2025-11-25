
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Courier.h"
#include "../Domain/Package.h"
#include <vector>
#include "../Observer.h"



class Repository: public Subject {
  private:
    vector<Courier> couriers;
    vector<Package> packages;
    // vector<Package> undelivered;

    public:
      Repository(){LoadData();}
      void LoadData();
      vector<Courier> getCouriers();
      vector<Package> getPackages();
      vector<Package> getUndeliveredAssigned(Courier courier);
    void addPackage(Package package);
    void writeToFile();
    void deliverPackage(Courier c, int index);
      ~Repository()=default;

};



#endif //REPOSITORY_H
