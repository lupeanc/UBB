#pragma once
#ifndef SERVICE_H
#define SERVICE_H
#include "repo.h"

typedef struct {
    Repository* repo;
} Service;

Service createService(Repository* repo);
void addProductService(Service* serv, Product p);
#endif