#include "Service.h"
Service::Service(Repository& adminRepo, Repository& userRepo): adminRepo{adminRepo}, userRepo{userRepo}{}

const vector<Event>& Service::getAdminRepo() {
    return this->adminRepo.getDynArr();
}

vector<Event> Service::getUserRepo() {
    return this->userRepo.getDynArr();
}

//! ADMIN
void Service::addServiceAdmin(string title, string description, Date date, int time, int attendance, string link) {
    this->adminRepo.addRepo(title, description, date, time, attendance, link);
}

void Service::deleteServiceAdmin(string title) {
    int deleted_admin;
    // deleted_admin = this->adminRepo.deleteEvent(title);
    this->userRepo.deleteEvent(title);
    // if (!deleted_admin)
    //     return 0;
    // return 1;
}

void Service::updateEventStringAdmin(string title, string newText, int command) {
    int updated_admin;
    // updated_admin = this->adminRepo.updateEventString(title, newText, command);
    this->userRepo.updateEventString(title, newText, command);
    // if (!updated_admin)
    //     return 0;
    // return 1;
}
void Service::updateEventIntAdmin(string title, int newInt, int command) {
    int updated_admin;
    // updated_admin = this->adminRepo.updateEventInt(title, newInt, command);
    this->userRepo.updateEventInt(title, newInt, command);
    // if (!updated_admin)
    //     return 0;
    // return 1;
}
void Service::updateEventDateAdmin(string title, int day, int month, int year) {
    int updated_admin;
    // updated_admin = this->adminRepo.updateEventDate(title, day, month, year);
    this->userRepo.updateEventDate(title, day, month, year);
    // if (!updated_admin)
    //     return 0;
    // return 1;

}

//! USER
void Service::addServiceUser(Event e) {
    int added, updated, new_attendance = e.getAttendance()+1;
    // updated = this->adminRepo.updateEventInt(e.getTitle(), new_attendance, 5);
    // added = this->userRepo.addRepo(e.getTitle(), e.getDescription(), e.getDate(), e.getTime(), e.getAttendance(), e.getLink());
    this->userRepo.addRepo(e.getTitle(), e.getDescription(), e.getDate(), e.getTime(), e.getAttendance()+1, e.getLink());
    this->adminRepo.updateEventInt(e.getTitle(), new_attendance, 5);

    // if (!added && !updated)
    //     return 0;
    // return 1;
}

void Service::deleteServiceAUser(Event e) {
    // int deleted, updated, new_attendance = e.getAttendance()-1, exists = this->adminRepo.checkExistence(e.getTitle());
    // deleted = this->userRepo.deleteEvent(e.getTitle());
    this->userRepo.deleteEvent(e.getTitle());
    this->adminRepo.updateEventInt(e.getTitle(), e.getAttendance()-1, 5);
    // this->adminRepo.updateEventInt(e.getTitle(), new_attendance, 5);
    // updated = this->adminRepo.updateEventInt(e.getTitle(), new_attendance, 5);
    // if (!deleted && !updated && exists!=-1)
    //     return 0;
    // return 1;
}

int Service::getSizeAdmin() {
    return this->adminRepo.getSize();
}

int Service::getSizeUser() {
    return this->userRepo.getSize();
}

//Service::~Service() {
//    delete this->adminRepo;
//    delete this->userRepo;
//}