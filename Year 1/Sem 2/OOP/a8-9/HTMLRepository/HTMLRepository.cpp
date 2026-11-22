
#include "HTMLRepository.h"
#include <shellapi.h>
#include <fstream>


void HTMLRepository::write() {
  ofstream fout(this->fileName);
  fout<<"<!DOCTYPE html>\n";
  fout<<"<html>\n";
  fout<<"<head>\n";
  fout<<"\t<title>Events list</title>\n";
  fout<<"</head>\n";
  fout<<"<body>\n";
  fout<<"<table border=\"1\">\n";
  fout<<"\t<tr>\n";
  fout<<"\t\t<td><strong>TITLE</strong></td>\n";
  fout<<"\t\t<td><strong>DESCRIPTION</strong></td>\n";
  fout<<"\t\t<td><strong>DATE</strong></td>\n";
  fout<<"\t\t<td><strong>TIME</strong></td>\n";
  fout<<"\t\t<td><strong>ATTENDANCE</strong></td>\n";
  fout<<"\t\t<td><strong>LINK</strong></td>\n";
  fout<<"\t</tr>\n";
  for(auto CurrentElement: this->elements)
  {
    fout<<"<tr>\n";
    fout<<"\t<td>"<<CurrentElement.getTitle()<<"</td>\n";
    fout<<"\t<td>"<<CurrentElement.getDescription()<<"</td>\n";
    fout<<"\t<td>"<<CurrentElement.getDateString()<<"</td>\n";
    fout<<"\t<td>"<<CurrentElement.getTime()<<"</td>\n";
    fout<<"\t<td>"<<CurrentElement.getAttendance()<<"</td>\n";
    fout<<"\t<td>"<<CurrentElement.getLink()<<"</td>\n";
    fout<<"</tr>\n";
  }
  fout<<"</table>\n";
  fout<<"</body>\n";
  fout<<"</html>\n";
}

void HTMLRepository::open() {
  ifstream fin(this->fileName);
  ShellExecute(nullptr, TEXT("open"),
                TEXT(R"(F:\c projects uni\assignment8-9\EventsList.html)"), nullptr, nullptr, SW_SHOWNORMAL);
}

HTMLRepository::HTMLRepository() {
  this->fileName = R"(F:\c projects uni\assignment8-9\EventsList.html)";
}

void HTMLRepository::set_data(vector<Event> data) {
  this->elements = std::move(data);
}