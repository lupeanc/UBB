
#include "Console.h"
Console::Console(){}
Console::~Console(){}
Console::Console(Service service){}

void Console::mainMenu(){
  int command;
  this->service.init();
  while(true){
    cout<<"1.add"<<endl;
    cout<<"2.display"<<endl;
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
      cout<<"Invalid Command"<<endl;
  }
}

void Console::addMenu(){
  string bodyStyle;
  int command, autonomy;
  double price;
  cout<<"Body: ";
  cin>>bodyStyle;

  cout<<"1.Turbo"<<endl;
  cout<<"2.Electric"<<endl;
  cin>>command;

  if(command == 1){
    cout<<"Enter Price: ";
    cin>>price;
    Engine* engine = new Turbo(price);
    Car* car = new Car(bodyStyle, engine);
    service.addCar(car);
  }
  else if(command == 2){
    cout<<"Enter Price: ";
    cin>>price;
    cout<<"Enter Autonomy: ";
    cin>>autonomy;
    Engine* engine = new Electric(price, autonomy);
    Car* car = new Car(bodyStyle, engine);
    service.addCar(car);
  }
  else
    cout<<"Invalid Command"<<endl;

}

void Console::displayMenu(){
  for(int i = 0; i<service.getCars().size(); i++){
    cout<<service.getCars()[i]->toString()<<endl;
  }
}