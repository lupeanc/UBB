// #include "../DynamicArray.h"
// #include "test_service.h"
// #include "../Repository/Repository.h"
// #include "../Service/Service.h"
// #include <assert.h>
//
// void testService::testAddServiceAdmin(){
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   assert(service.addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link") == 0);
// }
//
// void testService::testDeleteServiceAdmin(){
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   service.addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
//   assert(!service.deleteServiceAdmin("title"));
//   assert(service.deleteServiceAdmin("doesntexist"));
// }
//
// void testService::testUpdateEventStringAdmin(){
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);\
//   service.getUserRepo();
//   service.addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
//   assert(!service.updateEventStringAdmin("title", "new", 1));
//   assert(!service.updateEventStringAdmin("new", "new_desc", 2));
//   assert(!service.updateEventStringAdmin("new", "new_link", 6));
//   assert(service.updateEventStringAdmin("doesntexist", "new_desc", 1));
// }
//
// void testService::testUpdateEventIntAdmin(){
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   service.addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
//   assert(!service.updateEventIntAdmin("title", 10, 4));
//   assert(!service.updateEventIntAdmin("title", 11, 5));
//   assert(service.updateEventIntAdmin("doesntexist", -12, 1));
// }
//
// void testService::testUpdateEventDateAdmin(){
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   service.getAdminRepo();
//   service.addServiceAdmin("title", "desc", Date(1, 2, 2025), 1, 1, "link");
//   assert(!service.updateEventDateAdmin("title", 12, 11, 2024));
//   assert(service.updateEventDateAdmin("doesntexist", 1, 2, 2024));
// }
// //todo
// void testService::testAddServiceUser(){
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   assert(service.addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link")));
//   // assert(service->addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link")));
// }
//
// void testService::testDeleteServiceUser() {
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   service.addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link"));
//   assert(service.deleteServiceAUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link")));
//   assert(service.deleteServiceAUser(Event("name", "desc", Date(1, 2, 2025), 1, 1, "link"))==1);
// }
//
// void testService::testGetSizeUser() {
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   service.addServiceUser(Event("title", "desc", Date(1, 2, 2025), 1, 1, "link"));
//   assert(service.getSizeUser() == 1);
// }
//
// void testService::testGetSizeAdmin(){
//   Repository adminRepo;
//   Repository userRepo;
//   Service service(adminRepo, userRepo);
//   adminRepo.initRepo();
//   assert(service.getSizeAdmin() == 5);
// }
// void testService::testAllService(){
//   // testAddServiceAdmin();
//   // testDeleteServiceAdmin();
//   // testUpdateEventStringAdmin();
//   // testUpdateEventIntAdmin();
//   // testUpdateEventDateAdmin();
//   // testGetSizeAdmin();
//   //
//   // testAddServiceUser();
//   // testDeleteServiceUser();
//   // testGetSizeUser();
//
// }
