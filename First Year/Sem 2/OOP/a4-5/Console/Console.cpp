#include <windows.h>
#include <shellapi.h>
#include "Console.h"
#include <iostream>

using namespace std;
Console::Console(){}

Console::Console(Service* service, Validator* validator){
  this->service = service;
  this->validator = validator;
}

void Console::AddAdmin(){
  string title, description, link;
  int day, month, year, time, attendance;
  int is_valid = 0, is_added = 0;
  cout<<"Title:";
  cin>>title;

  cout<<"Description:";
  cin>>description;

  cout<<"Date"<<endl<<"Day:";
  cin>>day;
  cout<<"Month:";
  cin>>month;
  cout<<"Year:";
  cin>>year;
  is_valid = this->validator->validateDate(day, month, year);
  Date date(day, month, year);

  if(!is_valid){
    cout<<"Invalid Date"<<endl;
    return;
  }

  cout<<"Time:";
  cin>>time;
  is_valid = this->validator->validateTime(time);
  if(!is_valid){
    cout<<"Invalid Time"<<endl;
    return;
  }

  cout<<"Attendance:";
  cin>>attendance;
  is_valid = this->validator->validateAttendance(attendance);
  if(!is_valid){
    cout<<"Invalid Attendance"<<endl;
    return;
  }

  cout<<"Link: ";
  cin>>link;

  is_added = this->service->addServiceAdmin(title, description, date, time, attendance, link);
  if(is_added == 1){
    cout<<"Event already exists"<<endl;
  }
  else
    cout<<"Event added"<<endl;

}

void Console::DeleteAdmin(){
  string title;
  int is_deleted = 0;
  cout<<"Title:";
  cin>>title;

  is_deleted = this->service->deleteServiceAdmin(title);
  if(!is_deleted){
    cout<<"Event not found"<<endl;
  }
  else
    cout<<"Event deleted"<<endl;
}

void Console::UpdateAdmin(){
  string title, newText;
  int cmd, newInt, is_updated = 0, day, month, year, exists = 0;
  cout<<"Title:";
  cin>>title;
  cout<<"What would you like to update?"<<endl;
  cout<<"1. Title"<<endl<<"2. Description"<<endl<<"3. Date"<<endl<<"4. Time"<<endl<<"5. Attendance"<<endl<<"6. Link"<<endl;
  cin>>cmd;
  if(cmd == 1 || cmd == 2 || cmd == 6){
    cout<<"New Text:"<<endl;
    cin>>newText;
    is_updated = this->service->updateEventStringAdmin(title, newText, cmd);
    if(is_updated){
      cout<<"Event not found"<<endl;
    }
    else
      cout<<"Event updated"<<endl;
  }
  else if(cmd == 3){
    cout<<"New Day:"<<endl;
    cin>>day;
    cout<<"New Month:"<<endl;
    cin>>month;
    cout<<"New Year:"<<endl;
    cin>>year;
    if(validator->validateDate(day, month, year)){
      is_updated = this->service->updateEventDateAdmin(title, day, month, year);
    }
    else
      cout<<"Invalid Date"<<endl;
    if(is_updated){
      cout<<"Event not found"<<endl;
    }
    else
      cout<<"Event updated"<<endl;
  }
  else if(cmd == 4){
    cout<<"New Int:"<<endl;
    cin>>newInt;
    if(validator->validateTime(newInt)){
      is_updated = this->service->updateEventIntAdmin(title, newInt, cmd);
      if(is_updated == 1){
        cout<<"Event not found"<<endl;
      }
      else
        cout<<"Event updated"<<endl;
    }
  }
  else if(cmd == 5){
    cout<<"New Int:"<<endl;
    cin>>newInt;
    if(validator->validateAttendance(newInt)){
      is_updated = this->service->updateEventIntAdmin(title, newInt, cmd);
      if(is_updated == 1){
        cout<<"Event not found"<<endl;
      }
      else
        cout<<"Event updated"<<endl;
    }
  }
  else
    cout<<"Invalid Command"<<endl;
}
void Console::DisplayAdminList(){
  int n = this->service->getSizeAdmin();

  for(int i = 0; i < n; i++){
    cout<<"Title: "<<(*this->service->getAdminRepo())[i].getTitle()<<endl;
    cout<<"Description: "<<(*this->service->getAdminRepo())[i].getDescription()<<endl;
    cout<<"Date: "<<(*this->service->getAdminRepo())[i].getDateString()<<endl;
    cout<<"Time: "<<(*this->service->getAdminRepo())[i].getTime()<<endl;
    cout<<"Attendance: "<<(*this->service->getAdminRepo())[i].getAttendance()<<endl;
    cout<<"Link: "<<(*this->service->getAdminRepo())[i].getLink()<<endl;
    cout<<endl;
  }
}
void Console::AdminMode(){
  int command;
  while(true){
    cout<<"==============================="<<endl;
    cout<<"ADMIN MENU"<<endl;
    cout<<"==============================="<<endl;

    cout<<"1. Add"<<endl<<"2. Delete"<<endl<<"3. Update"<<endl<<"4. Display"<<endl<<"0. Exit"<<endl;
    cin>>command;

    if(command == 1){
      AddAdmin();
    }
    else if(command == 2){
      DeleteAdmin();
    }
    else if(command == 3){
      UpdateAdmin();
    }
    else if(command == 4){
      DisplayAdminList();
    }
    else if(command == 0){
      return;
    }
    else
      cout<<"Invalid Command"<<endl;
  }
}

void Console::Start(){
  int command;
  while(true){
    cout<<"==============================="<<endl;
    cout<<"MAIN MENU"<<endl;
    cout<<"==============================="<<endl;

    cout<<"1. Admin Mode"<<endl<<"2. User Mode"<<endl<<"0. Exit"<<endl;
    cin>>command;
    if(command == 1){
      AdminMode();
    }
    else if(command == 2){
      UserMode();
    }
    else if(command == 0){
      break;
    }
    else
      cout<<"Invalid Command"<<endl;
  }

}

void Console::UserMode() {
  int command;
  while (true) {
    cout<<"1. Your List"<<endl<<"2. List of Events"<<endl<<"0. Exit"<<endl;
    cin>>command;
    if(command == 1) {
      UsersOwnListMenu();
    }
    else if(command == 2) {
      DisplayUserListAll();
    }
    else if(command == 0) {
      return;
    }
    else
      cout<<"Invalid Command"<<endl;
  }

}

void Console::UsersOwnListMenu() {
  int command, month;
  while (true) {
    cout<<"1. See list of all events one by one"<<endl<<"2. See list of events happening during a certain month"<<endl
    <<"3. See all events at once"<<endl<<"0. Exit"<<endl;
    cin>>command;
    if(command == 1) {
      DisplayUserList();
    }
    else if(command == 2) {
      cout<<"Month: ";
      cin>>month;
      if (validator->validateDate(1, month, 2025)) {
        DisplayUserListMonth(month);
      }
      else
        cout<<"Invalid Month"<<endl;
    }
    else if (command == 3) {
      DisplayUserListAllAtOnce();
    }
    else if(command == 0) {
      return;
    }
    else cout<<"Invalid Command"<<endl;
  }
}

void OpenWebsite (const char * cpURL) {
  ShellExecute (NULL, "open", cpURL, NULL, NULL, SW_SHOWNORMAL);
}

void Console::DisplayUserList() {
  //has the add option as the user goes through the list + open in browser option
  string title, desc, link;
  int time, attendance;
  Date date;
  int n = this->service->getSizeUser(), command = -1;
  if (n == 0)
    cout<<"There is no list"<<endl;
  else {
    int i = 0;
    while (command !=0) {
      cout<<"Title: "<<(*this->service->getUserRepo())[i].getTitle()<<endl;
      title = (*this->service->getUserRepo())[i].getTitle();
      cout<<"Description: "<<(*this->service->getUserRepo())[i].getDescription()<<endl;
      desc = (*this->service->getUserRepo())[i].getDescription();
      cout<<"Date: "<<(*this->service->getUserRepo())[i].getDateString()<<endl;
      date = (*this->service->getUserRepo())[i].getDate();
      cout<<"Time: "<<(*this->service->getUserRepo())[i].getTime()<<endl;
      time = (*this->service->getUserRepo())[i].getTime();
      cout<<"Attendance: "<<(*this->service->getUserRepo())[i].getAttendance()<<endl;
      attendance = (*this->service->getUserRepo())[i].getAttendance();
      cout<<"Link: "<<(*this->service->getUserRepo())[i].getLink()<<endl;
      link = (*this->service->getUserRepo())[i].getLink();
      cout<<endl;
      Event e = Event(title, desc, date, time, attendance, link);
      cout<<"Options:"<<endl;
      cout<<"1.Next     2.Delete    3.Open in Browser    0.Exit"<<endl;
      cin>>command;

      if(command != 1 && command != 2 && command != 3 && command != 0) {
        cout<<"Invalid Command"<<endl;
      }
      else if(command == 2) {
        this->service->deleteServiceAUser(e);
      }
      else if(command == 3) {
        // int placeholder;
        OpenWebsite(link.c_str());
      }

      i++;
      if (i==n)
        i = 0;
    }
  }
}

void Console::DisplayUserListMonth(int month) {
  string title, desc, link;
  int time, attendance, current_event_month;
  Date date;
  int n = this->service->getSizeUser(), command = -1;
  if (n == 0)
    cout<<"There is no list"<<endl;
  else {
    int i = 0;
    while (command !=0) {
      current_event_month = (*this->service->getUserRepo())[i].getDate().getMonth();
      if (current_event_month == month) {
        cout<<"Title: "<<(*this->service->getUserRepo())[i].getTitle()<<endl;
        title = (*this->service->getUserRepo())[i].getTitle();
        cout<<"Description: "<<(*this->service->getUserRepo())[i].getDescription()<<endl;
        desc = (*this->service->getUserRepo())[i].getDescription();
        cout<<"Date: "<<(*this->service->getUserRepo())[i].getDateString()<<endl;
        date = (*this->service->getUserRepo())[i].getDate();
        cout<<"Time: "<<(*this->service->getUserRepo())[i].getTime()<<endl;
        time = (*this->service->getUserRepo())[i].getTime();
        cout<<"Attendance: "<<(*this->service->getUserRepo())[i].getAttendance()<<endl;
        attendance = (*this->service->getUserRepo())[i].getAttendance();
        cout<<"Link: "<<(*this->service->getUserRepo())[i].getLink()<<endl;
        link = (*this->service->getUserRepo())[i].getLink();
        cout<<endl;
        Event e = Event(title, desc, date, time, attendance, link);
        cout<<"Options:"<<endl;
        cout<<"1.Next     2.Delete    3.Open in Browser    0.Exit"<<endl;
        cin>>command;

        if(command != 1 && command != 2 && command != 3 && command != 0) {
          cout<<"Invalid Command"<<endl;
        }
        else if(command == 2) {
          this->service->deleteServiceAUser(e);
        }
        else if(command == 3) {
          OpenWebsite(link.c_str());
        }
      }

      i++;
      if (i==n)
        i = 0;
    }
  }
}

void Console::DisplayUserListAllAtOnce() {
  int n = this->service->getSizeUser();
  if (n == 0)
    cout<<"There is no list"<<endl;
  else {
    for(int i = 0; i < n; i++){
      cout<<"Title: "<<(*this->service->getUserRepo())[i].getTitle()<<endl;
      cout<<"Description: "<<(*this->service->getUserRepo())[i].getDescription()<<endl;
      cout<<"Date: "<<(*this->service->getUserRepo())[i].getDateString()<<endl;
      cout<<"Time: "<<(*this->service->getUserRepo())[i].getTime()<<endl;
      cout<<"Attendance: "<<(*this->service->getUserRepo())[i].getAttendance()<<endl;
      cout<<"Link: "<<(*this->service->getUserRepo())[i].getLink()<<endl;
      cout<<endl;
    }
  }

}

void Console::DisplayUserListAll() {
  string title, desc, link;
  int time, attendance, added = 0;
  Date date;
  int n = this->service->getSizeAdmin(), command = -1;
  if (n == 0)
    cout<<"There is no list"<<endl;
  else {
    int i = 0;
    while (command !=0) {
      cout<<"Title: "<<(*this->service->getAdminRepo())[i].getTitle()<<endl;
      title = (*this->service->getAdminRepo())[i].getTitle();
      cout<<"Description: "<<(*this->service->getAdminRepo())[i].getDescription()<<endl;
      desc = (*this->service->getAdminRepo())[i].getDescription();
      cout<<"Date: "<<(*this->service->getAdminRepo())[i].getDateString()<<endl;
      date = (*this->service->getAdminRepo())[i].getDate();
      cout<<"Time: "<<(*this->service->getAdminRepo())[i].getTime()<<endl;
      time = (*this->service->getAdminRepo())[i].getTime();
      cout<<"Attendance: "<<(*this->service->getAdminRepo())[i].getAttendance()<<endl;
      attendance = (*this->service->getAdminRepo())[i].getAttendance();
      cout<<"Link: "<<(*this->service->getAdminRepo())[i].getLink()<<endl;
      link = (*this->service->getAdminRepo())[i].getLink();
      cout<<endl;
      Event e = Event(title, desc, date, time, attendance, link);
      cout<<"Options:"<<endl;
      cout<<"1.Next     2.Add    3.Open in Browser    0.Exit"<<endl;
      cin>>command;

      if(command != 1 && command != 2 && command != 3 && command != 0) {
        cout<<"Invalid Command"<<endl;
      }
      else if(command == 2) {
        for(int i = 0; i < this->service->getSizeUser(); i++) {
          if (title == (*this->service->getUserRepo())[i].getTitle()) {
            cout<<endl<<"Already added!";
            added = 1;
          }
        }
        if (!added)
          this->service->addServiceUser(e);
      }
      else if(command == 3) {
        OpenWebsite(link.c_str());
      }

      i++;
      if (i==n)
        i = 0;
    }
  }
}

Console::~Console(){
  delete service;
  delete validator;
}
