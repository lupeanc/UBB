
#include "Repository.h"
#include <fstream>
#include <algorithm>

Repository::Repository(){
  this->LoadData();
}

void Repository::LoadData(){
  ifstream fin(R"(F:\\c projects uni\\OOP_PracticeT3Character\\input.txt)");
  int slices;
  string toppings;

  pizzas.clear();
  while(fin>>slices>>toppings){
    Pizza p(slices, toppings);
    pizzas.push_back(p);
  }

  fin.close();

}

bool compare(Pizza p1, Pizza p2){
  return p1.getToppings() < p2.getToppings();
}

vector<Pizza> Repository::getPizzas(){
  std::sort(pizzas.begin(), pizzas.end(), compare);
  return pizzas;
}

Repository::~Repository(){}
