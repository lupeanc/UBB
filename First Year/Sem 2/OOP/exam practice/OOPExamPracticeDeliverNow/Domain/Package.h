
#ifndef PACKAGE_H
#define PACKAGE_H
#include <iostream>
using namespace std;


class Package {
  private:
    string recipient;
    string str;
    int nr;
    int xloc, yloc;
    bool status;

    public:
      Package();
      Package(string recipient, string str, int nr, int xloc, int yloc, bool status){
        this->recipient=recipient;
        this->str=str;
        this->nr=nr;
        this->xloc=xloc;
        this->yloc=yloc;
        this->status=status;
      }
      string getRecipient(){
        return recipient;
      }
      string getStr(){
        return str;
      }
      string getStatus(){
        return to_string(status);
      }
      void setStatus(string value) {
        if (value == "true")
          this->status = true;
        else
          this->status = false;
      }
      string toString();
      ~Package()=default;


};



#endif //PACKAGE_H
