/*The company “Home SmartApps” have decided to design a new intelligent refrigerator.
Besides the hardware, they need a software application to manage the refrigerator.
Each Product that the fridge can store has a name, a category (one of dairy, sweets, meat or fruit), a quantity and an expiration date.
The software application will provide the following functionalities:

(a) Add, delete or update a product.
    A product is uniquely identified by name and category.
    If a product that already exists is added, its quantity will be updated (the new quantity is added to the existing one).

(b) Display all products whose name contains a given string
    (if the string is empty, all products from the refrigerator are considered)
    and show them sorted ascending by the existing quantity.
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "product.h"
#include "repo.h"
#include "service.h"

void menu(){
    printf("===========================\n");
    printf("MENU\n");
    printf("===========================\n");
    printf("1. Add New Item\n");
    printf("2. Remove Item\n");
    printf("3. Update Item\n");
    printf("4. Display\n");
    printf("0. Quit\n");
}

int main() {
    int command, quantity;
    char name[50], category[50], exp[8];
    Product p;
    Repository repo = createRepo();
    Service serv = createService(&repo);

    while (1) {
        menu();
        printf("> ");
        scanf("%d", &command);

        if (command == 1) {
            scanf("%s", name);
            scanf("%s", category);
            scanf("%d", &quantity);
            scanf("%s", exp);
            p = createProduct(name, category, quantity, exp);
            addProductService(&serv, p);
            // added = false;
            //
            // if (getLen(repo) == 0)
            //     addProduct(&repo, p);
            // else {
            //     for (int i = 0; i<sizeof(repo.products)/sizeof(repo.products[0]); i++) {
            //         if (strcmp(repo.products[i].name, name) == 0 && strcmp(repo.products[i].category, category) == 0) {
            //             repo.products[i].quantity += quantity;
            //             added=true;
            //             break;
            //         }
            //     }
            //     if (!added)
            //         addProduct(&repo, p);
            // }
        }
        else if (command == 0)
            break;

    }

  return 0;
}