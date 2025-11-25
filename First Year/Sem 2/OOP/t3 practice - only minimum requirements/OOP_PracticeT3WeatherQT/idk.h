
#ifndef IDK_H
#define IDK_H

#include <QWidget>


QT_BEGIN_NAMESPACE
namespace Ui { class idk; }
QT_END_NAMESPACE

class idk : public QWidget {
Q_OBJECT

public:
    explicit idk(QWidget *parent = nullptr);
    ~idk() override;

private:
    Ui::idk *ui;
};


#endif //IDK_H
