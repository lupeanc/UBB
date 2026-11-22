#include <string.h>
#include "product.h"

Product createProduct(char name[50], char category[50], int quantity, char exp[8]) {
    Product p;
    strcpy(p.name, name);
    strcpy(p.category, category);
    p.quantity = quantity;
    strcpy(p.exp, exp);

    return p;
}

void getName(Product p, char name[50]) {
  strcpy(p.name, name);
}

void getCategory(Product p, char category[50]) {
    strcpy(p.category, category);
}

int getQuantity(Product p) {
  return p.quantity;
}

void getExp(Product p, char exp[50]) {
    strcpy(p.exp, exp);
}