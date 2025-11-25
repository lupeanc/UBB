#include <fstream>
#include "CSVRepository.h"
using namespace std;

CSVRepository::CSVRepository(){
  this->fileName = R"(F:\\c projects uni\\assignment_6_7\\EventsList.csv)";
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

  ShellExecute(nullptr, nullptr,
                 R"(F:\\c projects uni\\assignment_6_7\\EventsList.csv)",
                 nullptr, nullptr, SW_SHOWNORMAL);
}

void CSVRepository::set_data(vector<Event> data){
  this->elements = std::move(data);
}