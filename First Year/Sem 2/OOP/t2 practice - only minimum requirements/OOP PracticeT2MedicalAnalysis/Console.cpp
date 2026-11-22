
#include "Console.h"
Console::Console() {}
Console::Console(Person person) {
  this->person = person;
}

void Console::mainMenu(){
  int command;
  string name;
  cout<<"Name: ";
  cin>>name;
  person.setName(name);
  cout<<endl;
  this->person.initRepo();

  while(true){
    cout<<"1. Add Measurement"<<endl;
    cout<<"2. Dsiplay"<<endl;
    cin>>command;

    if(command == 1){
      addMenu();
    }
    else if(command == 2){
      displayMenu();
    }
    else if(command == 0){
      return;
    }
    else
      cout<<"Invalid command"<<endl;
  }
}

void Console::addMenu() {
  int command;
  string date;
  cout<<"Date: ";
  cin>>date;
  cout<<endl;
  cout<<"1. Add BMI"<<endl;
  cout<<"2. Add BP"<<endl;
  cin>>command;

  if(command == 1){
    double val;
    cin>>val;
    Measurement* measurement = new BMI(date, val);
    this->person.addRepo(measurement);
  }
  else if(command == 2){
    int sistval;
    int diasval;
    cin>>sistval>>diasval;
    Measurement* measurement = new BP(date, sistval, diasval);
    this->person.addRepo(measurement);
  }
  else
    cout<<"Invalid command"<<endl;
}
void Console::displayMenu() {
  cout<<this->person.getName()<<endl;
  for(int i = 0; i < this->person.getRepo().size(); i++){
    cout<<this->person.getRepo()[i]->toString()<<endl;
  }
}

Console::~Console() {}