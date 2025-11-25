#include "service.h"
#include "repo.h"
#include <stdbool.h>
#include <string.h>

Service createService(Repository* repo){
    Service service;
    service.repo = repo;
    return service;
}

void addProductService(Service* serv, Product p) {
    bool added = false;


    for (int i = 0; i<sizeof(serv->repo->products)/sizeof(serv->repo->products[0]); i++) {
        if (strcmp(serv->repo->products[i].name, p.name) == 0 && strcmp(serv->repo->products[i].category, p.category) == 0) {
            serv->repo->products[i].quantity += p.quantity;
            added=true;
            break;
        }
    }
    if (!added)
        addProduct(serv->repo, p);

//    if (getLen(service) == 0)
//        addProduct(&repo, p);
//    else {
//        for (int i = 0; i<sizeof(repo.products)/sizeof(repo.products[0]); i++) {
//            if (strcmp(repo.products[i].name, p.name) == 0 && strcmp(repo.products[i].category, p.category) == 0) {
//                repo.products[i].quantity += p.quantity;
//                added=true;
//                break;
//            }
//        }
//        if (!added)
//            addProduct(service -> repo, p);
//    }
    //addProduct(service -> repo, p);
}