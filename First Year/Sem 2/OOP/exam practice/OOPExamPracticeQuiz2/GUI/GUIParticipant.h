
#ifndef GUIPARTICIPANT_H
#define GUIPARTICIPANT_H
#include <QWidget>
#include "../Repository/Repository.h"
#include <QVBoxLayout>
#include <QListWidget>
#include "../Observer.h"



class GUIParticipant: public QWidget, public Observer {
  private:
    Repository repository;
    Participant participant;
    QVBoxLayout *layout;
    QListWidget *questionListWidget;

public:
    GUIParticipant(Repository repository, Participant p);
    void initGUI();
    void populateQuestions();
    void Update() override;
    ~GUIParticipant()=default;



};



#endif //GUIPARTICIPANT_H
