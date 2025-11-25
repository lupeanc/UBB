
#include "Console.h"
Console::Console(){}
Console::Console(Controller controller){
  this->controller = controller;
  }

  void Console::mainMenu(){
    int command;
    while(true){
      cout<<"1.Add Department"<<endl;
      cout<<"2.Display Department"<<endl;
      cin>>command;
      controller.initDepartment();

      if(command==1){
        addMenu();
      }
      else if(command==2){
        displayMenu();
      }
      else if(command==0){
        return;
      }
      else
        cout<<"Invalid Input"<<endl;
    }
}


  void Console::addMenu(){
    int command;
    cout<<"1.Add Natal"<<endl;
    cout<<"2.Add Surgery"<<endl;
    cin>>command;

    if(command==1){
      int nbDr, nbMothers, nbNewborns;
      string name;
      cout<<"Name: ";
      cin>>name;
      cout<<"Nb Dr: ";
      cin>>nbDr;
      cout<<"Nb Mothers: ";
      cin>>nbMothers;
      cout<<"Nb Newborns: ";
      cin>>nbNewborns;

      Department* department = new Natal(name, nbDr, nbMothers, nbNewborns);
      controller.addDepartment(department);
    }
    else if(command==2){
      int nbDr, nbPatients;
      string name;
      cout<<"Name: ";
      cin>>name;
      cout<<"Nb Dr: ";
      cin>>nbDr;
      cout<<"Nb Patients: ";
      cin>>nbPatients;

      Department* department = new Surgery(name, nbDr, nbPatients);
      controller.addDepartment(department);
    }
    else
      cout<<"Invalid Input"<<endl;
  }

  void Console::displayMenu(){
    for(int i = 0; i<controller.getDepartments().size(); i++){
      cout<<controller.getDepartments()[i]->toString()<<endl;
    }
  }

Console::~Console(){}