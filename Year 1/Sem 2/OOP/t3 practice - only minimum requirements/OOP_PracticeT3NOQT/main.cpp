#include <iostream>
using namespace std;
#include "Domain/Weather.h"
#include "Repository/Repository.h"
int main() {
    Repository repository;
    for (auto i: repository.getAll()) {
        cout<<i.getStart()<<endl;
        cout<<i.getEnd()<<endl;
        cout<<i.getPp()<<endl;
        cout<<i.getDescription()<<endl;
    }
}