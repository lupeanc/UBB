
#ifndef TEST_SERVICE_H
#define TEST_SERVICE_H
#pragma once

class testService{
  public:
    void testGetAdminRepo();
    void testGetUserRepo();
    void testAddServiceAdmin();
    void testDeleteServiceAdmin();
    void testUpdateEventStringAdmin();
    void testUpdateEventIntAdmin();
    void testUpdateEventDateAdmin();

    void testAddServiceUser();
    void testDeleteServiceUser();

    void testGetSizeAdmin();
    void testGetSizeUser();

    void testAllService();
};
#endif //TEST_SERVICE_H
