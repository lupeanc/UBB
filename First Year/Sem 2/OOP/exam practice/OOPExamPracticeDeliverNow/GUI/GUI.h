
#ifndef GUI_H
#define GUI_H
#include <QWidget>
#include <QListWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include "../Repository/Repository.h"
#include "../Observer.h"


class GUI: public QWidget, public Observer {
    private:
      Repository repository;
      Courier courier;
      QVBoxLayout *layout;
      QListWidget *undeliveredAssignedPackagesListWidget;
        QPushButton *deliverButton;

      public:
        GUI(Repository repository, Courier courier);
        void initGUI();
        void populateUndeliveredAssigned();
        void update() override;

        int getSelectedIndex();
        void deliverPackage();
        void connectSignals();

        ~GUI()=default;
};



#endif //GUI_H
