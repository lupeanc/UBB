
#include "Report.h"

string Report::toString(){
  if(status == true)
    return desc + " " + name + " " + to_string(xloc) + " " + to_string(yloc) + " true";
  else
    return desc + " " + name + " " + to_string(xloc) + " " + to_string(yloc)+ " false";

}


