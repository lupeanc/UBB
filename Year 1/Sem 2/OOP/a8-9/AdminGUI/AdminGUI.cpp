
#include "AdminGUI.h"
#include "qformlayout.h"
#include "qgridlayout.h"
#include <qlabel.h>
#include <QMessageBox>
#include "../Validator/validator.h"

AdminModeGUI::AdminModeGUI(Service &service, QWidget* parent): service{service}, QDialog{parent} {
    this->initAdminModeGUI();
    this->populateList();
    this->connectSignalsAndSlots();
}

void AdminModeGUI::initAdminModeGUI() {
    QFont buttonsFont("Consolas", 13, true);

    this->EventsListWidget = new QListWidget{};
    this->EventsListWidget->setFont(buttonsFont);

    this->titleLineEdit = new QLineEdit{};
    this->titleLineEdit->setFont(buttonsFont);

    this->descriptionLineEdit = new QLineEdit{};
    this->descriptionLineEdit->setFont(buttonsFont);

//    this->dateLineEdit = new QLineEdit{};
//    this->dateLineEdit->setFont(buttonsFont);

    this->dayLineEdit = new QLineEdit{};
    this->dayLineEdit->setFont(buttonsFont);

    this->monthLineEdit = new QLineEdit{};
    this->monthLineEdit->setFont(buttonsFont);

    this->yearLineEdit = new QLineEdit{};
    this->yearLineEdit->setFont(buttonsFont);

    this->timeLineEdit = new QLineEdit{};
    this->timeLineEdit->setFont(buttonsFont);

    this->attendanceLineEdit = new QLineEdit{};
    this->attendanceLineEdit->setFont(buttonsFont);

    this->linkLineEdit = new QLineEdit{};
    this->linkLineEdit->setFont(buttonsFont);

    this->addButton = new QPushButton{"Add"};
    this->addButton->setFont(buttonsFont);

    this->deleteButton = new QPushButton{"Delete"};
    this->deleteButton->setFont(buttonsFont);

    this->updateDescriptionButton = new QPushButton{"Update Description"};
    this->updateDescriptionButton->setFont(buttonsFont);

    this->updateLinkButton = new QPushButton{"Update Link"};
    this->updateLinkButton->setFont(buttonsFont);

    this->updateDateButton = new QPushButton{"Update Date"};
    this->updateDateButton->setFont(buttonsFont);

    this->updateTimeButton = new QPushButton{"Update Time"};
    this->updateTimeButton->setFont(buttonsFont);

    this->updateAttendanceButton = new QPushButton{"Update Attendance"};
    this->updateAttendanceButton->setFont(buttonsFont);

    this->displayButton = new QPushButton{"Display"};
    this->displayButton->setFont(buttonsFont);

    QLabel *space = new QLabel();
    space->setText("");

    QLabel *eventsText = new QLabel();
    eventsText->setText("The list of events");
    QFont eventsFont("Consolas", 15, true);
    eventsText->setFont(eventsFont);

    auto *title = new QLabel();
    title->setText("Title");
    title->setFont(buttonsFont);

    auto *description = new QLabel();
    description->setText("Description");
    description->setFont(buttonsFont);

//    auto *date = new QLabel();
//    date->setText("Date");
//    date->setFont(buttonsFont);

    auto *day = new QLabel();
    day->setText("Day");
    day->setFont(buttonsFont);

    auto *month = new QLabel();
    month->setText("Month");
    month->setFont(buttonsFont);

    auto *year = new QLabel();
    year->setText("Year");
    year->setFont(buttonsFont);

    auto *time = new QLabel();
    time->setText("Time");
    time->setFont(buttonsFont);

    auto *attendance = new QLabel();
    attendance->setText("Attendance");
    attendance->setFont(buttonsFont);

    auto *link = new QLabel();
    link->setText("Link");
    link->setFont(buttonsFont);

    auto* adminLayout = new QVBoxLayout();
    adminLayout->addWidget(eventsText);
    adminLayout->addWidget(this->EventsListWidget);

    auto* eventsDetails = new QFormLayout();
    eventsDetails->addRow(title, this->titleLineEdit);
    eventsDetails->addRow(description, this->descriptionLineEdit);
    eventsDetails->addRow(day, this->dayLineEdit);
    eventsDetails->addRow(month, this->monthLineEdit);
    eventsDetails->addRow(year, this->yearLineEdit);
    eventsDetails->addRow(time, this->timeLineEdit);
    eventsDetails->addRow(attendance, this->attendanceLineEdit);
    eventsDetails->addRow(link, this->linkLineEdit);

    adminLayout->addLayout(eventsDetails);

    auto* buttonsLayout = new QGridLayout();
    buttonsLayout->addWidget(this->addButton, 0, 0);
    buttonsLayout->addWidget(this->deleteButton, 0, 1);
    buttonsLayout->addWidget(this->updateDescriptionButton, 1, 0);
    buttonsLayout->addWidget(this->updateDateButton, 1, 1);
    buttonsLayout->addWidget(this->updateTimeButton, 1, 2);
    buttonsLayout->addWidget(this->updateAttendanceButton, 1, 3);
    buttonsLayout->addWidget(this->updateLinkButton, 1, 4);
//    buttonsLayout->addWidget(this->displayButton, 1, 2);

    adminLayout->addLayout(buttonsLayout);

    QWidget *adminDisplayWindow = new QWidget();
    adminDisplayWindow->setLayout(adminLayout);
    adminDisplayWindow->show();
}

void AdminModeGUI::populateList() {
    this->EventsListWidget->clear();
    std::vector<Event> Events = this->service.getAdminRepo();
    for (Event &e: Events) {
        this->EventsListWidget->addItem(QString::fromStdString(e.getTitle() + " - " + e.getDescription() + " - " + e.getDateString() + " - " + std::to_string(e.getTime())
                                                              + " - " + std::to_string(e.getAttendance()) + " - " + e.getLink()));

    }
}

void AdminModeGUI::connectSignalsAndSlots() {
    QObject::connect(this->EventsListWidget, &QListWidget::itemSelectionChanged, [this](){
        int selectedIndex = this->getSelectedIndex();

        if(selectedIndex < 0)
            return;

        Event e = this->service.getAdminRepo()[selectedIndex];
        this->titleLineEdit->setText(QString::fromStdString(e.getTitle()));
        this->descriptionLineEdit->setText(QString::fromStdString(e.getDescription()));
        this->dateLineEdit->setText(QString::fromStdString((e.getDateString())));
        this->timeLineEdit->setText(QString::fromStdString(std::to_string(e.getTime())));
        this->attendanceLineEdit->setText(QString::fromStdString(std::to_string(e.getAttendance())));
        this->linkLineEdit->setText(QString::fromStdString((e.getLink())));
    });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &AdminModeGUI::addEvent);
    QObject::connect(this->deleteButton, &QPushButton::clicked, this, &AdminModeGUI::deleteEvent);
    QObject::connect(this->updateDescriptionButton, &QPushButton::clicked, this, &AdminModeGUI::updateEventStringDescription);
    QObject::connect(this->updateLinkButton, &QPushButton::clicked, this, &AdminModeGUI::updateEventStringLink);
    QObject::connect(this->updateDateButton, &QPushButton::clicked, this, &AdminModeGUI::updateEventDate);
    QObject::connect(this->updateTimeButton, &QPushButton::clicked, this, &AdminModeGUI::updateEventIntTime);
    QObject::connect(this->updateAttendanceButton, &QPushButton::clicked, this, &AdminModeGUI::updateEventIntAttendance);
    QObject::connect(this->displayButton, &QPushButton::clicked, this, &AdminModeGUI::populateList);

}

int AdminModeGUI::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->EventsListWidget->selectionModel()->selectedIndexes();
    if(selectedIndexes.isEmpty())
    {
        this->titleLineEdit->clear();
        this->descriptionLineEdit->clear();
        this->dateLineEdit->clear();
        this->dayLineEdit->clear();
        this->monthLineEdit->clear();
        this->yearLineEdit->clear();
        this->timeLineEdit->clear();
        this->attendanceLineEdit->clear();
        this->linkLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void AdminModeGUI::addEvent() {
    std::string title = this->titleLineEdit->text().toStdString();
    std::string description = this->descriptionLineEdit->text().toStdString();
    //    std::string date = this->dateLineEdit->text().toStdString();
    std::string day = this->dayLineEdit->text().toStdString();
    std::string month = this->monthLineEdit->text().toStdString();
    std::string year = this->yearLineEdit->text().toStdString();
    std::string time = this->timeLineEdit->text().toStdString();
    std::string attendance = this->attendanceLineEdit->text().toStdString();
    std::string link = this->linkLineEdit->text().toStdString();

    if (stoi(day)<0 || stoi(month)<0 || stoi(year)<0 || stoi(day)>30 || stoi(month)>12 || stoi(year)<2024 ||stoi(year)>2025 || stoi(attendance)<0 || stoi(time)<0
|| stoi(time)>23) {
            QMessageBox::critical(this, "Error", "Couldn't add the event!");
            return;
        }

        try{
          Date date(stoi(day), stoi(month), stoi(year));
            this->service.addServiceAdmin(title, description, date, stoi(time), stoi(attendance), link);
        }
        catch (...)
        {
            QMessageBox::critical(this, "Error", "Couldn't add the event!");
            return;
        }

    this->populateList();

    int lastElement = this->service.getAdminRepo().size()-1;
    this->EventsListWidget->setCurrentRow(lastElement);
}

void AdminModeGUI::deleteEvent() {
    std::string title = this->titleLineEdit->text().toStdString();
        try{
            this->service.deleteServiceAdmin(title);
        }
        catch (...)
        {
            QMessageBox::critical(this, "Error", "Couldn't delete the event!");
            return;
        }
    this->populateList();
    int lastElement = this->service.getAdminRepo().size()-1;
    this->EventsListWidget->setCurrentRow(lastElement);

}

void AdminModeGUI::updateEventStringDescription() {
    std::string title = this->titleLineEdit->text().toStdString();
    std::string description = this->descriptionLineEdit->text().toStdString();

        try{
            this->service.updateEventStringAdmin(title, description, 2);
        }
        catch (...)
        {
            QMessageBox::critical(this, "Error", "Couldn't update the Event!");
            return;
        }
    this->populateList();
    int lastElement = this->service.getAdminRepo().size()-1;
    this->EventsListWidget->setCurrentRow(lastElement);

}

void AdminModeGUI::updateEventStringLink() {
    std::string title = this->titleLineEdit->text().toStdString();
    std::string link = this->linkLineEdit->text().toStdString();

    try{
        this->service.updateEventStringAdmin(title, link, 6);
    }
    catch (...)
    {
        QMessageBox::critical(this, "Error", "Couldn't update the Event!");
        return;
    }
    this->populateList();
    int lastElement = this->service.getAdminRepo().size()-1;
    this->EventsListWidget->setCurrentRow(lastElement);

}

void AdminModeGUI::updateEventDate() {
    std::string title = this->titleLineEdit->text().toStdString();
    std::string day = this->dayLineEdit->text().toStdString();
    std::string month = this->monthLineEdit->text().toStdString();
    std::string year = this->yearLineEdit->text().toStdString();

    try{
        this->service.updateEventDateAdmin(title, stoi(day), stoi(month), stoi(year));
    }
    catch (...)
    {
        QMessageBox::critical(this, "Error", "Couldn't update the Event!");
        return;
    }
    this->populateList();
    int lastElement = this->service.getAdminRepo().size()-1;
    this->EventsListWidget->setCurrentRow(lastElement);

}

void AdminModeGUI::updateEventIntTime() {
    std::string title = this->titleLineEdit->text().toStdString();
    std::string time = this->timeLineEdit->text().toStdString();

    try{
        this->service.updateEventIntAdmin(title, stoi(time), 4);
    }
    catch (...)
    {
        QMessageBox::critical(this, "Error", "Couldn't update the Event!");
        return;
    }
    this->populateList();
    int lastElement = this->service.getAdminRepo().size()-1;
    this->EventsListWidget->setCurrentRow(lastElement);

}

void AdminModeGUI::updateEventIntAttendance() {
    std::string title = this->titleLineEdit->text().toStdString();
    std::string attendance = this->attendanceLineEdit->text().toStdString();

    try{
        this->service.updateEventIntAdmin(title, stoi(attendance), 5);
    }
    catch (...)
    {
        QMessageBox::critical(this, "Error", "Couldn't update the Event!");
        return;
    }
    this->populateList();
    int lastElement = this->service.getAdminRepo().size()-1;
    this->EventsListWidget->setCurrentRow(lastElement);

}

AdminModeGUI::~AdminModeGUI() {

}