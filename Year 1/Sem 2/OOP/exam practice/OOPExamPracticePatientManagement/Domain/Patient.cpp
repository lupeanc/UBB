
#include "Patient.h"
string Patient::toString() {
    string str;
    str=name+" "+admissionDate + " " +diagnosis+ " " + specialization+ " " + currentDr;
    return str;
}