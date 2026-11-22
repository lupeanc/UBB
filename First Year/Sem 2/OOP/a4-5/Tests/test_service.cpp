#include "../DynamicArray.h"
#include "test_service.h"
#include "../Repository/Repository.h"
#include "../Service/Service.h"
#include <assert.h>

void testService::testGetAdminRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);

  assert(service->getAdminRepo() == adminDA);
  delete service;
}

void testService::testGetUserRepo(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);

  assert(service->getUserRepo() == userDA);
  delete service;
}

void testService::testAddServiceAdmin(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  assert(service->addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link") == 0);
  delete service;
}

void testService::testDeleteServiceAdmin(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  service->addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
  assert(!service->deleteServiceAdmin("title"));
  assert(service->deleteServiceAdmin("doesntexist"));
  delete service;
}

void testService::testUpdateEventStringAdmin(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  service->addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
  assert(!service->updateEventStringAdmin("title", "new", 1));
  assert(!service->updateEventStringAdmin("new", "new_desc", 2));
  assert(!service->updateEventStringAdmin("new", "new_link", 6));
  assert(service->updateEventStringAdmin("doesntexist", "new_desc", 1));
  delete service;
}

void testService::testUpdateEventIntAdmin(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  service->addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
  assert(!service->updateEventIntAdmin("title", 10, 4));
  assert(!service->updateEventIntAdmin("title", 11, 5));
  assert(service->updateEventIntAdmin("doesntexist", -12, 1));
  delete service;
}

void testService::testUpdateEventDateAdmin(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  service->addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
  assert(!service->updateEventDateAdmin("title", 12, 11, 2024));
  assert(service->updateEventDateAdmin("doesntexist", 1, 2, 2024));
}
//todo
void testService::testAddServiceUser(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  assert(service->addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link")));
  // assert(service->addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link")));
}

void testService::testDeleteServiceUser() {
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  service->addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link"));
  assert(service->deleteServiceAUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link")));
  assert(service->deleteServiceAUser(Event("name", "desc", Date(1, 2, 2025), 1, 1, "link"))==1);
}

void testService::testGetSizeUser() {
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  service->addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link"));
  assert(service->getSizeUser() == 1);
}

void testService::testGetSizeAdmin(){
  DynamicArray<Event>* adminDA = new DynamicArray<Event>(100);
  DynamicArray<Event>* userDA = new DynamicArray<Event>(100);
  Repository* adminRepo = new Repository(adminDA);
  adminRepo->initRepo();
  Repository* userRepo = new Repository(userDA);
  Service* service = new Service(adminRepo, userRepo);
  assert(service->getSizeAdmin() == 5);
}
void testService::testAllService(){
  testGetAdminRepo();
  testGetUserRepo();
  testAddServiceAdmin();
  testDeleteServiceAdmin();
  testUpdateEventStringAdmin();
  testUpdateEventIntAdmin();
  testUpdateEventDateAdmin();
  testGetSizeAdmin();

  testAddServiceUser();
  testDeleteServiceUser();
  testGetSizeUser();

}
