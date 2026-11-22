
#include "Validator.h"
#include <iostream>
//#include <windows.h>
//#include <shellapi.h>

bool Validator::validateDate(int day, int month, int year) {
    if(day > 31 || month > 12 || month < 1 || day < 1 || month<1 || year<2024 || year>2025) {
      return false;
    }
    return true;
}
bool Validator::validateTime(int time) {
   if(time > 24 || time < 0)
     return false;
   return true;
}
bool Validator::validateAttendance(int attendance) {
  if(attendance >= 0)
    return true;
  return false;
}
//void OpenWebsite (const char * cpURL)
//{
//  ShellExecute (NULL, "open", cpURL, NULL, NULL, SW_SHOWNORMAL);
//}
//bool Validator::validateLink(string link) {
//    try{
//      OpenWebsite(link.c_str());
//      throw(true);
//    }
//    catch(...){
//      return false;
//    }
//}

