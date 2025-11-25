
// You may need to build the project (run Qt uic code generator) to get "ui_idk.h" resolved

#include "idk.h"
#include "ui_idk.h"


idk::idk(QWidget *parent) :
    QWidget(parent), ui(new Ui::idk) {
    ui->setupUi(this);
}

idk::~idk() {
    delete ui;
}
