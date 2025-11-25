
#ifndef TEST_REPO_H
#define TEST_REPO_H
#pragma once
#include "../Repository/Repository.h"

class testRepository{
  public:
    void testGetDynamicArray();
    void testGetSize();

    void testInitRepo();
    void testAddRepo();
    void testCheckExistance();
    void testDeleteRepo();
    void testUpdateStringRepo();
    void testUpdateIntRepo();
    void testUpdateDateRepo();

    void testAllRepository();


};
#endif //TEST_REPO_H
