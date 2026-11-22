
#ifndef GUICOMPANY_H
#define GUICOMPANY_H
#include <QWidget>
#include <QListWidget>
#include <QVBoxLayout>
#include <QListWidgetItem>
#include <QPushButton>
#include <QLineEdit>
#include "../Repository/Repository.h"
#include "../Observer.h"

class GUICompany: public QWidget, public Observer {
private:
    Repository repository;
    QVBoxLayout *layout;
    QListWidget *PackageListWidget;
    QLineEdit *recipientLineEdit, *streetLineEdit, *numberLineEdit, *xlocLineEdit, *ylocLineEdit;
    QPushButton *addButton;

public:
    GUICompany(Repository repository);
    void initGUI();
    void populatePackages();
    void addPackage();
    void update() override;

    void connectSignals();

    ~GUICompany()=default;

};



#endif //GUICOMPANY_H
