#pragma once
#ifndef PRODUCT_H
#define PRODUCT_H
typedef struct {
    char name[50], category[50], exp[8];
    int quantity;
} Product;

Product createProduct(char name[50], char category[50], int quantity, char exp[8]);

void getName(Product p, char name[50]);

void getCategory(Product p, char category[50]);

int getQuantity(Product p);

void getExp(Product p, char exp[50]);
#endif