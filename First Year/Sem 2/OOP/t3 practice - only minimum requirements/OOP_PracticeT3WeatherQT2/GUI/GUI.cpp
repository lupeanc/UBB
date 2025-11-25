
#include "GUI.h"
#include "QVBoxLayout"
GUI::GUI(Repository repo) {
    this->repo = repo;
    this->init();
    this->populateList(repo.getAll());
}

void GUI::init() {
    this->list = new QListWidget();
    QVBoxLayout* layout = new QVBoxLayout();
    layout->addWidget(this->list);
    setLayout(layout);
}

void GUI::populateList(vector <Weather> elements) {
    this->list->clear();

    for (auto element : elements) {
        this->list->addItem(QString::fromStdString(element.toString()));
    }

}

GUI::~GUI(){}
