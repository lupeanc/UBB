#include <windows.h>
#include <fstream>
#include <shellapi.h>
#include "CSVRepository.h"
using namespace std;

CSVRepository::CSVRepository(){
  this->fileName = R"(F:\\c projects uni\\assignment8-9\\EventsList.csv)";
  }

void CSVRepository::write(){
  ofstream fout(this->fileName);
  for (auto CurrentElement: this->elements) {
      fout<<CurrentElement.getTitle()<<","<<CurrentElement.getDescription()<<","<<CurrentElement.getDateString()<<","<<CurrentElement.getTime()<<","<<CurrentElement.getAttendance()<<","<<CurrentElement.getLink()<<endl;
  }
  fout.close();
  this->elements.clear();
}

void CSVRepository::open(){
  ifstream fin(this->fileName);

  ShellExecute(nullptr, TEXT("open"),
                 TEXT(R"(F:\\c projects uni\\assignment8-9\\EventsList.csv)"), nullptr,
                 nullptr, SW_SHOWNORMAL);
}

void CSVRepository::set_data(vector<Event> data){
  this->elements = std::move(data);
}