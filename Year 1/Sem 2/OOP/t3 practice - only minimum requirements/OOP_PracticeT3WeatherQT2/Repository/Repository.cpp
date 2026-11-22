
#include "Repository.h"
#include <fstream>
Repository::Repository() {
    this->LoadData();
}

vector<Weather> Repository::getAll() {
    return elements;
}

void Repository::LoadData() {
    ifstream fin(R"(F:\\c projects uni\\OOP_PracticeT3WeatherQT2\\input.txt)");
    int start;
    string desc;

    this->elements.clear();

    while (fin>>start>>desc) {
        this->elements.push_back(Weather(start,desc));
    }

}

Repository::~Repository() {

}

