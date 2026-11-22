
#ifndef TEST_DOMAIN_H
#define TEST_DOMAIN_H
#pragma once
#include <string>
#include "../Domain/Event.h"
using namespace std;

class testDomain {
  public:
    void testGetDay();
    void testGetMonth();
    void testGetYear();
    void testToStringDate();

    void testGetTitle();
    void testGetDescription();
    void testGetDate();
    void testGetTime();
    void testGetAttendance();
    void testGetLink();

    void testSetDay();
    void testSetMonth();
    void testSetYear();

    void testSetTitle();
    void testSetDescription();
    void testSetTime();
    void testSetAttendance();
    void testSetLink();

    void testAllDomain();

};
#endif //TEST_DOMAIN_H
