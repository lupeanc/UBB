
#include "Package.h"
string Package::toString(){
  return recipient + " " + str + " " + to_string(nr) + " " + to_string(xloc) + " " + to_string(yloc) + " " + to_string(status);
}