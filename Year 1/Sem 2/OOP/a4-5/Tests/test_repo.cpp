
#include "test_repo.h"
#include "../DynamicArray.h"
#include <assert.h>

void testRepository::testGetDynamicArray(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  assert(adminDA == adminRepo->getDynamicArray());
  delete adminRepo;
}

void testRepository::testGetSize(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->initRepo();
  assert(adminRepo->getSize() == 5);
}

void testRepository::testInitRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->initRepo();
  assert(adminRepo->getSize() == 5);
}

void testRepository::testAddRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  assert(adminRepo->addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link")==0);
  assert(adminRepo->getSize() == 1);
  assert(adminRepo->addRepo("title", "d", Date(1, 3, 2024), 12, 3, "link2"));
}

void testRepository::testCheckExistance(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->initRepo();
  assert(adminRepo->checkExistance("title"));
  assert(!adminRepo->checkExistance("HumanBody"));
}

void testRepository::testDeleteRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->initRepo();
  assert(!adminRepo->deleteEvent("HumanBody"));
}

void testRepository::testUpdateStringRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
  assert(!adminRepo->updateEventString("title", "new", 1));
  assert((*adminRepo)[0].getTitle() == "new");
  assert(!adminRepo->updateEventString("new", "new_desc", 2));
  assert(!adminRepo->updateEventString("new", "new_link", 6));
}

void testRepository::testUpdateIntRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
  assert(!adminRepo->updateEventInt("title", 20, 4));
  assert((*adminRepo)[0].getTime() == 20);
  assert(!adminRepo->updateEventInt("title", 20, 5));
}

void testRepository::testUpdateDateRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
  assert(!adminRepo->updateEventDate("title", 10, 12, 2024));
}

void testRepository::testAllRepository(){
  testGetDynamicArray();
  testGetSize();
  testInitRepo();
  testAddRepo();
  testCheckExistance();
  testDeleteRepo();
  testUpdateStringRepo();
  testUpdateIntRepo();
  testUpdateDateRepo();
}
