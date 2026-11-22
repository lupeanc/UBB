
#ifndef GUI_H
#define GUI_H
#include <windows.h>
#include "../Service/Service.h"
#include "../Validator/Validator.h"
#include "../AbstractEventsList/AbstractEventsList.h"
#include <QVBoxLayout>
//#include "AdminModeGUI.h"
//#include "UserModeGUI.h"
#pragma once

#include <qwidget.h>
#include <qlistwidget.h>
#include <qlineedit.h>
#include <qpushbutton.h>
#include <QComboBox>
#include <QMainWindow>

class GUI: public QMainWindow
{
    Q_OBJECT
    private:
    std::string type = "empty";
    Service& service;
    AbstractEventsList* ASB;
    void initGUI();
    ///Graphical elements
    QComboBox *filetypeComboBox;
    QPushButton* adminModeButton, * userModeButton, *saveButton;

public:
    GUI(Service& service, QWidget *parent = 0);
    ~GUI();
    void connectSignalsAndSlots();
    void startUserModeGUI();
    void startAdminModeGUI();
    void saveFileType();
    //void createChart();

};
#endif //GUI_H
