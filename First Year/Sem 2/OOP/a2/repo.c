#include "repo.h"

Repository createRepo() {
  Repository repo;
  repo.len = 0;
  return repo;
}

int getLen(Repository repo) {
  return repo.len;
}

void addProduct(Repository* repo, Product p) {
  repo->products[repo->len++] = p;
}