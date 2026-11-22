#include "Console.h"
#include "Repo.h"

int main(){
  Repo repo;
  repo.init();
  Console console(repo);
  console.mainMenu();
  return 0;
}
