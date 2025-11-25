#include "test_domain.h"
#include <assert.h>
#include <iostream>

void testDomain::testGetDay(){
  Date date(1, 2, 2025);
  assert(date.getDay() == 1);
}

void testDomain::testGetMonth(){
  Date date(1, 2, 2025);
  assert(date.getMonth() == 2);
}

void testDomain::testGetYear(){
  Date date(1, 2, 2025);
  assert(date.getYear() == 2025);
}

void testDomain::testToStringDate() {
  Date date(1, 2, 2025);
  string dateString = date.toString();
  // assert(date.toString() == "1.2.2025");
}


void testDomain::testGetTitle(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  assert(event.getTitle() == "title");
}

void testDomain::testGetDescription(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  assert(event.getDescription() == "desc");
}

void testDomain::testGetDate(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  assert(event.getDate().getDay() == 1);
  assert(event.getDate().getMonth() == 2);
  assert(event.getDate().getYear() == 2025);
  }

void testDomain::testGetTime(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  assert(event.getTime() == 12);
}

void testDomain::testGetAttendance(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  assert(event.getAttendance() == 100);
}

void testDomain::testGetLink(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  assert(event.getLink() == "link");
}

void testDomain::testSetDay(){
  Date date(1, 2, 2025);
  date.setDay(10);
  assert(date.getDay() == 10);
}

void testDomain::testSetMonth(){
  Date date(1, 2, 2025);
  date.setMonth(12);
  assert(date.getMonth() == 12);
}

void testDomain::testSetYear(){
  Date date(1, 2, 2025);
  date.setYear(2024);
  assert(date.getYear() == 2024);
}

void testDomain::testSetTitle(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  event.setTitle("new");
  assert(event.getTitle() == "new");
}

void testDomain::testSetDescription(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  event.setDescription("new");
  assert(event.getDescription() == "new");
}
void testDomain::testSetTime(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  event.setTime(20);
  assert(event.getTime() == 20);
}
void testDomain::testSetAttendance(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  event.setAttendance(20);
  event.getDateString();
  assert(event.getAttendance() == 20);
}

void testDomain::testSetLink(){
  Date date(1, 2, 2025);
  Event event("title", "desc", date, 12, 100, "link");
  event.setLink("new");
  assert(event.getLink() == "new");
}

void testDomain::testAllDomain(){
  testGetDay();
  testGetMonth();
  testGetYear();
  testToStringDate();

  testGetTitle();
  testGetDescription();
  testGetDate();
  testGetTime();
  testGetAttendance();
  testGetLink();

  testSetDay();
  testSetMonth();
  testSetYear();

  testSetTitle();
  testSetDescription();
  testSetTime();
  testSetAttendance();
  testSetLink();
}