
#ifndef USERGUI_H
#define USERGUI_H
#pragma once
#include <QVBoxLayout>
#include <qwidget.h>
#include <qlistwidget.h>
#include "../AbstractEventsList/AbstractEventsList.h"
#include "../Service/Service.h"
#include <qlineedit.h>
#include <qpushbutton.h>
#include <QDialog>
#include <shellapi.h>

class UserModeGUI: public QDialog {

private:
    int position;
    AbstractEventsList* ASB;
    Service& service;
    QListWidget* eventsListWidget;
    QListWidget* userListWidget;
    QLineEdit *monthLineEdit;
    QPushButton* displayEventsButton, * openApplicationButton, * displayUserButton, *deleteEventButton, *displayUserButtonSeparateWindow, *displayMonthButton;
    QPushButton* nextButton, * addButton, *deleteButton;

public:
    UserModeGUI(Service& service, AbstractEventsList* ASB, QWidget* parent = nullptr);
    void initUserModeGUI();

    void connectSignalsAndSlots();
    void connectSignalsAndSlotsDisplayFunction();
    void connectSignalsAndSlotsDisplayFunctionUser();

    int getSelectedIndex();

    void displayEvents();
    void initDisplayEvents();
    void displayUserE();
    void populateDisplayEvents(int position, std::vector<Event> events);
    void nextEvent();
    void addEvent();

    void populateUserList();
    void clearPopulatedList();

    void displayUserEvents();
    void initDisplayUserEvents();
    void displayUserList();
    void populateDisplayEventsUser(int position, std::vector<Event> events);
    void nextEventUserList();
    void deleteEvent();

    void OpenWebsite (const char * cpURL);
    void openApplication();
    ~UserModeGUI();

};
#endif //USERGUI_H
