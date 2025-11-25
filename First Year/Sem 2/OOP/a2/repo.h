#pragma once
#ifndef REPO_H
#define REPO_H

#include "product.h"

typedef struct {
  Product products[100];
  int len;
} Repository;

Repository createRepo();
int getLen(Repository repo);
void addProduct(Repository* repo, Product p);
#endif