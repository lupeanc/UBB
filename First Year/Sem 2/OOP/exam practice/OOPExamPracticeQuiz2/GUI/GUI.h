
#ifndef GUI_H
#define GUI_H
#include <QWidget>
#include "../Repository/Repository.h"
#include <QListWidget>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLineEdit>
#include "../Observer.h"


class GUI: public QWidget, public Observer {
  private:
    Repository repository;
    QVBoxLayout *layout;
    QListWidget *questionListWidget;
    QPushButton *addButton;
    QLineEdit *idLineEdit, *textLineEdit, *answerLineEdit, *scoreLineEdit;

    public:
      GUI(Repository repository);
      void initGUI();
      void populateQuestions();
      void addQuestion();
      void connectSignals();
    void Update() override;
      ~GUI()=default;

};



#endif //GUI_H
