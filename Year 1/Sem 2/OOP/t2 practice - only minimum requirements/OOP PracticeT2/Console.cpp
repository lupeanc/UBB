
#include "Console.h"
//Console::Console(){}
Console::Console(Repo repo){
  this->repo = repo;
}
void Console::mainMenu(){
  int command;
  while(true){
    cout<<"============================="<<endl;
    cout<<"Menu"<<endl;
    cout<<"============================="<<endl;
    cout<<"1. Add Appliance"<<endl;
    cout<<"2. Display"<<endl;
    cout<<"0. Exit"<<endl;

    cin>>command;
    if(command == 1){
      addMenu();
    }
    else if(command == 2){
      displayAll();
    }
    else if(command == 0){
      return;
    }
    else
      cout<<"Invalid Command"<<endl;
  }
}

void Console::addMenu(){
  int command;
  string usageClass;
  // bool hasFreezer;
  int hasFreezer;
  double consumedElecHour;
  string id;
  cout<<"ID: ";
  cin>>id;
  cout<<endl;

  cout<<"Add:"<<endl;
  cout<<"1. Refrigerator"<<endl;
  cout<<"2. Dishwasher"<<endl;

  cin>>command;
  if(command == 1){
    cout<<"Class: ";
    cin>>usageClass;
    cout<<endl<<"Has freezer (1 for true, 0 for false): ";
    cin>>hasFreezer;
    if (hasFreezer == 1) {
      Appliance* appliance = new Refrigerator(id, usageClass, true);
      this->repo.addRepo(appliance);
    }
    else {
      Appliance* appliance = new Refrigerator(id, usageClass, false);
      this->repo.addRepo(appliance);
    }
    cout<<endl;

    // Appliance* appliance = new Refrigerator(id, usageClass, hasFreezer);
    // this->repo.addRepo(appliance);
  }
  else if(command == 2){
    cout<<"Consumed elec: ";
    cin>>consumedElecHour;
    cout<<endl;

    Appliance* appliance = new Dishwasher(id, consumedElecHour);
    this->repo.addRepo(appliance);
  }
  else
    cout<<"Invalid Command"<<endl;
}

void Console::displayAll(){
  for(int i = 0; i < this->repo.getAllRepo().size(); i++){
    cout << this->repo.getAllRepo()[i]->toString() << endl;
  }
}

//void Console::start(){
//  while(true){
//    mainMenu();
//  }
//}

Console::~Console(){}