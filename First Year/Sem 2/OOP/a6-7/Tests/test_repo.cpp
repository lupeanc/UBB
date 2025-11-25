//
// #include "test_repo.h"
// #include "../DynamicArray.h"
// #include <assert.h>
//
// #include "../FileRepository/FileRepository.h"
//
// void testRepository::testGetSize(){
//   FileRepository fileRepo("test_file.txt");
//   Repository adminRepo;
//   adminRepo.initRepo();
//   fileRepo.initRepo();
//   assert(adminRepo.getSize() == 5);
// }
// void testRepository::testInitRepo(){
//   FileRepository fileRepo("test_file.txt");
//   Repository adminRepo;
//   adminRepo.initRepo();
//   fileRepo.initRepo();
//   assert(adminRepo.getSize() == 5);
// }
//
// void testRepository::testAddRepo(){
//   FileRepository fileRepo("test_file.txt");
//   Repository adminRepo;
//   assert(adminRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link")==0);
//   assert(adminRepo.getSize() == 1);
//   assert(adminRepo.addRepo("title", "d", Date(1, 3, 2024), 12, 3, "link2"));
//   assert(!fileRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link")==0);
//   assert(fileRepo.addRepo("title", "d", Date(1, 3, 2024), 12, 3, "link2"));
// }
//
// void testRepository::testCheckExistance(){
//   FileRepository fileRepo("test_file.txt");
//   Repository adminRepo;
//   adminRepo.initRepo();
//   fileRepo.initRepo();
//   assert(adminRepo.checkExistance("title"));
//   assert(!adminRepo.checkExistance("HumanBody"));
//   assert(fileRepo.checkExistance("title"));
//   assert(fileRepo.checkExistance("HumanBody"));
// }
//
// void testRepository::testDeleteRepo(){
//   Repository adminRepo;
//   FileRepository fileRepo("test_file.txt");
//   adminRepo.initRepo();
//   fileRepo.initRepo();
//   assert(!adminRepo.deleteEvent("HumanBody"));
//   assert(!fileRepo.deleteEvent("HumanBody"));
// }
//
// void testRepository::testUpdateStringRepo(){
//   Repository adminRepo;
//   FileRepository fileRepo("test_file.txt");
//   adminRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
//   fileRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
//   assert(!adminRepo.updateEventString("title", "new", 1));
//   assert((adminRepo)[0].getTitle() == "new");
//   assert(!adminRepo.updateEventString("new", "new_desc", 2));
//   assert(!adminRepo.updateEventString("new", "new_link", 6));
//
//   assert(!fileRepo.updateEventString("title", "new", 1));
//   assert(!fileRepo.updateEventString("new", "new_desc", 2));
//   assert(!fileRepo.updateEventString("new", "new_link", 6));
// }
//
// void testRepository::testUpdateIntRepo(){
//   Repository adminRepo;
//   FileRepository fileRepo("test_file.txt");
//   adminRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
//   fileRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
//   fileRepo.getDynArr();
//   assert(!adminRepo.updateEventInt("title", 20, 4));
//   assert((adminRepo)[0].getTime() == 20);
//   assert(!adminRepo.updateEventInt("title", 20, 5));
//
//   assert(!fileRepo.updateEventInt("title", 20, 4));
//   assert(!fileRepo.updateEventInt("title", 20, 5));
// }
//
// void testRepository::testUpdateDateRepo(){
//   FileRepository fileRepo("test_file.txt");
//   Repository adminRepo;
//   fileRepo.getSize();
//   adminRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
//   fileRepo.addRepo("title", "desc", Date(1, 2, 2025), 16, 100, "link");
//   assert(!adminRepo.updateEventDate("title", 10, 12, 2024));
//   assert(!fileRepo.updateEventDate("title", 10, 12, 2024));
// }
//
// void testRepository::testAllRepository(){
//   // testGetSize();
//   // testInitRepo();
//   // testAddRepo();
//   // testCheckExistance();
//   // testDeleteRepo();
//   // testUpdateStringRepo();
//   // testUpdateIntRepo();
//   // testUpdateDateRepo();
// }
