
#ifndef ADMINGUI_H
#define ADMINGUI_H
#pragma once
#include <QWidget>
#include <qlistwidget.h>
#include <qlineedit.h>
#include <qpushbutton.h>
#include <QComboBox>
#include <QVBoxLayout>
#include "../Service/Service.h"
#include <QDialog>

class AdminModeGUI: public QDialog {

private:
    Service& service;
    QListWidget* EventsListWidget;
    QLineEdit * titleLineEdit, * descriptionLineEdit, * dateLineEdit, * timeLineEdit, * attendanceLineEdit, * linkLineEdit,
    *dayLineEdit, *monthLineEdit, *yearLineEdit;
    //todo for update: add all of the updates independently
    QPushButton* addButton, * deleteButton, *updateDescriptionButton, *updateLinkButton, * updateDateButton, * updateTimeButton, *updateAttendanceButton, *displayButton;

public:
    AdminModeGUI(Service& service, QWidget* parent = NULL);
    ~AdminModeGUI();
    void connectSignalsAndSlots();
    int getSelectedIndex() const;
    void populateList();
    void addEvent();
    void deleteEvent();
    void updateEventStringDescription();
    void updateEventStringLink();
    void updateEventDate();
    void updateEventIntTime();
    void updateEventIntAttendance();
    void initAdminModeGUI();

};
#endif //ADMINGUI_H
