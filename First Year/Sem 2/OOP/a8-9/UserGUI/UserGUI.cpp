#include <windows.h>
#include "UserGUI.h"
#include "qformlayout.h"
#include "qgridlayout.h"
#include "../Service/Service.h"
//#include "windows.h"
#include <qlabel.h>
#include <QMessageBox>
#include <shellapi.h>

UserModeGUI::UserModeGUI(Service &service, AbstractEventsList* ASB, QWidget* parent): service{service}, ASB{ASB}, QDialog{parent} {
    this->initUserModeGUI();
    this->connectSignalsAndSlots();
}

void UserModeGUI::initUserModeGUI() {
    QFont buttonsFont("Consolas", 13, true);

    this->userListWidget = new QListWidget{};
    this->userListWidget->setFont(buttonsFont);

    this->displayEventsButton = new QPushButton{"Display Events"};
    this->displayEventsButton->setFont(buttonsFont);

    this->displayUserButton = new QPushButton{"Display User List"};
    this->displayUserButton->setFont(buttonsFont);

    // this->displayMonthButton = new QPushButton{"Display List Month"};
    // this->displayMonthButton->setFont(buttonsFont);

    this->displayUserButtonSeparateWindow = new QPushButton("Edit User List");
    this->displayUserButtonSeparateWindow->setFont(buttonsFont);

    this->openApplicationButton = new QPushButton{"Open Application"};
    this->openApplicationButton->setFont(buttonsFont);

    QLabel *space = new QLabel();
    space->setText("");

    QLabel *eventsText = new QLabel();
    eventsText->setText("User list");
    QFont coatsFont("Consolas", 15, true);
    eventsText->setFont(coatsFont);

    QVBoxLayout* userLayout = new QVBoxLayout( this );
    userLayout->addWidget(eventsText);
    userLayout->addWidget(this->userListWidget);

    QGridLayout* buttonsLayout = new QGridLayout();
    buttonsLayout->addWidget(this->displayEventsButton, 0, 0);
    buttonsLayout->addWidget(this->displayUserButton, 1, 0);
    buttonsLayout->addWidget(this->displayUserButtonSeparateWindow, 2, 0);
    buttonsLayout->addWidget(this->openApplicationButton, 3, 0);
    // buttonsLayout->addWidget(this->displayMonthButton, 4, 0);

    userLayout->addLayout(buttonsLayout);

    QWidget *userDisplayWindow = new QWidget();
    userDisplayWindow->setLayout(userLayout);
    userDisplayWindow->show();
}

void UserModeGUI::connectSignalsAndSlots() {
    QObject::connect(this->displayEventsButton, &QPushButton::clicked, this, &UserModeGUI::displayEvents);
    QObject::connect(this->displayUserButton, &QPushButton::clicked, this, &UserModeGUI::populateUserList);
    QObject::connect(this->displayUserButtonSeparateWindow, &QPushButton::clicked, this, &UserModeGUI::displayUserEvents);
    QObject::connect(this->openApplicationButton, &QPushButton::clicked, this, &UserModeGUI::openApplication);

}

void UserModeGUI::connectSignalsAndSlotsDisplayFunction() {
    QObject::connect(this->nextButton, &QPushButton::clicked, this, &UserModeGUI::nextEvent);
    QObject::connect(this->addButton, &QPushButton::clicked, this, &UserModeGUI::addEvent);
}

void UserModeGUI::connectSignalsAndSlotsDisplayFunctionUser(){
  QObject::connect(this->nextButton, &QPushButton::clicked, this, &UserModeGUI::nextEventUserList);
  QObject::connect(this->deleteButton, &QPushButton::clicked, this, &UserModeGUI::deleteEvent);
}

UserModeGUI::~UserModeGUI() {

}

int UserModeGUI::getSelectedIndex() {
    QModelIndexList selectedIndexes = this->eventsListWidget->selectionModel()->selectedIndexes();
    if(selectedIndexes.isEmpty())
        return -1;
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void UserModeGUI::displayEvents() {
    if(this->service.getAdminRepo().size() == 0) {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    else {
        this->initDisplayEvents();
        this->displayUserE();
    }
}

void UserModeGUI::initDisplayEvents() {
    QFont buttonsFont("Consolas", 13, true);

    this->eventsListWidget = new QListWidget{};
    this->eventsListWidget->setFont(buttonsFont);

    this->nextButton = new QPushButton{"Next"};
    this->nextButton->setFont(buttonsFont);

    this->addButton = new QPushButton{"Add"};
    this->addButton->setFont(buttonsFont);


    QLabel *coatsText = new QLabel();
    coatsText->setText("Events");
    QFont coatsFont("Consolas", 15, true);
    coatsText->setFont(coatsFont);

    QVBoxLayout* displayLayout = new QVBoxLayout();
    displayLayout->addWidget(coatsText);
    displayLayout->addWidget(this->eventsListWidget);

    QGridLayout* buttonsLayout = new QGridLayout();
    buttonsLayout->addWidget(this->nextButton, 0, 0);
    buttonsLayout->addWidget(this->addButton, 0, 1);

    displayLayout->addLayout(buttonsLayout);
    QWidget *mainDisplayWindow = new QWidget();
    mainDisplayWindow->setLayout(displayLayout);
    mainDisplayWindow->show();
}



void UserModeGUI::displayUserE() {
    this->position = 0;
    std::vector<Event> events = this->service.getAdminRepo();
    if(events.empty())
    {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    this->populateDisplayEvents(0, events);
    this->connectSignalsAndSlotsDisplayFunction();
}

void UserModeGUI::populateDisplayEvents(int position, std::vector<Event> events) {
    this->eventsListWidget->clear();
    Event e = events[position];
    //    this->position = position;
    this->eventsListWidget->addItem(QString::fromStdString(e.getTitle() + " - " + e.getDescription() + " - " + e.getDateString() + " - " + std::to_string(e.getTime())
                                                              + " - " + std::to_string(e.getAttendance()) + " - " + e.getLink()));
    string link = e.getLink();
    // this->OpenWebsite(link.c_str());
    cout<<"LINK OPENED: "<<link<<endl;
    // ShellExecute(nullptr, TEXT("open"),
    //              reinterpret_cast<LPCWSTR>(link.c_str()), nullptr, nullptr, SW_SHOWNORMAL);
}

void UserModeGUI::OpenWebsite (const char * cpURL) {
    ShellExecute(NULL, reinterpret_cast<LPCWSTR>("open"), reinterpret_cast<LPCWSTR>(cpURL), NULL, NULL, SW_SHOWNORMAL);

}

void UserModeGUI::nextEvent() {
    std::vector<Event> events = this->service.getAdminRepo();
    if(events.empty()) {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    if(this->position == events.size()-1)
        this->position = 0;
    else
        this->position += 1;
    // string link = events[position].getLink();
    // ShellExecute(nullptr, TEXT("open"),
    //              reinterpret_cast<LPCWSTR>(link.c_str()), nullptr, nullptr, SW_SHOWNORMAL);
    this->populateDisplayEvents(this->position, events);

}

void UserModeGUI::addEvent() {
    std::vector<Event> events = this->service.getAdminRepo();
    if(events.empty()) {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    int pos = this->position;
    int i = this->getSelectedIndex();
    if(i == -1){
        QMessageBox::critical(this, "Error", "Please select the event!");
        return;
    }
    else {
        this->service.addServiceUser(events[pos]);
    }
}



void UserModeGUI::populateUserList() {
    this->userListWidget->clear();
    std::vector<Event> events = this->service.getUserRepo();
    for (Event &e: events) {
        this->userListWidget->addItem(QString::fromStdString(e.getTitle() + " - " + e.getDescription() + " - " + e.getDateString() + " - " + std::to_string(e.getTime())
                                                              + " - " + std::to_string(e.getAttendance()) + " - " + e.getLink()));

    }
}

void UserModeGUI::clearPopulatedList() {
    this->eventsListWidget->clear();
}


void UserModeGUI::displayUserEvents() {
    if(this->service.getUserRepo().size() == 0) {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    else {
        this->initDisplayUserEvents();
        this->displayUserList();
    }
}

void UserModeGUI::initDisplayUserEvents() {
    QFont buttonsFont("Consolas", 13, true);

    this->eventsListWidget = new QListWidget{};
    this->eventsListWidget->setFont(buttonsFont);

    this->nextButton = new QPushButton{"Next"};
    this->nextButton->setFont(buttonsFont);

    this->deleteButton = new QPushButton{"Delete"};
    this->deleteButton->setFont(buttonsFont);


    QLabel *coatsText = new QLabel();
    coatsText->setText("Events");
    QFont coatsFont("Consolas", 15, true);
    coatsText->setFont(coatsFont);

    QVBoxLayout* displayLayout = new QVBoxLayout();
    displayLayout->addWidget(coatsText);
    displayLayout->addWidget(this->eventsListWidget);

    QGridLayout* buttonsLayout = new QGridLayout();
    buttonsLayout->addWidget(this->nextButton, 0, 0);
    buttonsLayout->addWidget(this->deleteButton, 0, 1);

    displayLayout->addLayout(buttonsLayout);
    QWidget *mainDisplayWindow = new QWidget();
    mainDisplayWindow->setLayout(displayLayout);
    mainDisplayWindow->show();
}

//USER LIST
void UserModeGUI::displayUserList() {
    this->position = 0;
    //    std::vector<Event> coats = this->service.GetFilteredRepository(this->size);
    std::vector<Event> events = this->service.getUserRepo();
    if(events.empty())
    {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    this->populateDisplayEventsUser(0, events);
    this->connectSignalsAndSlotsDisplayFunctionUser();
}

void UserModeGUI::populateDisplayEventsUser(int position, std::vector<Event> events) {
    this->eventsListWidget->clear();
    this->userListWidget->clear();
    Event e = events[position];
    //    this->position = position;
    this->eventsListWidget->addItem(QString::fromStdString(e.getTitle() + " - " + e.getDescription() + " - " + e.getDateString() + " - " + std::to_string(e.getTime())
                                                              + " - " + std::to_string(e.getAttendance()) + " - " + e.getLink()));
    // ShellExecute(nullptr, TEXT("open"),
    //              TEXT("(events[position].getLink().c_str())"), NULL, NULL, SW_SHOWNORMAL);
}


void UserModeGUI::nextEventUserList() {

    std::vector<Event> events = this->service.getUserRepo();
    if(events.empty()) {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    if(this->position == events.size()-1)
        this->position = 0;
    else
        this->position += 1;
    // this->populateDisplayEvents(this->position, events);
    this->populateDisplayEventsUser(this->position, events);

}

void UserModeGUI::deleteEvent() {
    std::vector<Event> events = this->service.getUserRepo();
    if(events.empty()) {
        QMessageBox::critical(this, "Error", "There are no events!");
        return;
    }
    int pos = this->position;
    int i = this->getSelectedIndex();
    if(i == -1){
        QMessageBox::critical(this, "Error", "Please select the event!");
        return;
    }
    else {
      this->service.deleteServiceAUser(events[pos]);
    }
}

void UserModeGUI::openApplication() {
    this->ASB->set_data(this->service.getUserRepo());
    this->ASB->write();
    this->ASB->open();

}