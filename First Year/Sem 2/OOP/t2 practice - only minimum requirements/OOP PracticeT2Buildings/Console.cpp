
#include "Console.h"
Console::Console(){}
Console::Console(Controller controller) {
  this->controller = controller;
}

void Console::mainMenu(){
  int command;

  while(true){
     cout<<"1. Add Building"<<endl;
  	cout<<"2. Display Buildings"<<endl;
  	cout<<"0. Exit"<<endl;
    cin>>command;

  if(command ==1){
    addMenu();
  }
  else if(command ==2){
    displayMenu();
  }
  else if(command ==0){
    return;
  }
  else
    cout<<"Invalid Command"<<endl;
 }
}
void Console::addMenu(){
  int command, constrYear;
  string address;
  cout<<"1. Add Block"<<endl;
  cout<<"2. Add House"<<endl;
  cin>>command;

  if(command ==1){
    int nbAp, occupied;
    cout<<"Address: ";
    cin>>address;
    cout<<"ConstrYear: ";
    cin>>constrYear;
    cout<<"NbAp: ";
    cin>>nbAp;
    cout<<"Occupied: ";
    cin>>occupied;

    Building* building = new Block(address, constrYear, nbAp, occupied);
    this->controller.addBuilding(building);
  }
  else if(command ==2){
    string type;
    int historical;
    cout<<"Address: ";
    cin>>address;
    cout<<"ConstrYear: ";
    cin>>constrYear;
    cout<<"Type: ";
    cin>>type;
    cout<<"Historical (0 for false, 1 for true): ";
    cin>>historical;

    if(historical){
      Building* building = new House(address, constrYear, type, true);
      this->controller.addBuilding(building);
    }
    else{
      Building* building = new House(address, constrYear, type, false);
      this->controller.addBuilding(building);
      }
  }
  else
    cout<<"Invalid Command"<<endl;
}
void Console::displayMenu(){
  for(int i = 0; i < controller.getBuildings().size(); i++){
    cout<<controller.getBuildings()[i]->toString()<<endl;
  }
}


Console::~Console()= default;