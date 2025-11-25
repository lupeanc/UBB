#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

// theta(1)
SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	this->currentNode = b.head;
	this->currentFreq = 1;
}

// theta(1)
TComp SortedBagIterator::getCurrent() {
	if (this->currentNode == nullptr)
		throw exception();
	return this->currentNode->info.first;
}

// theta(1)
bool SortedBagIterator::valid() {
	if(this->currentNode == nullptr)
          return false;
    return true;
}

//theta(1)
void SortedBagIterator::next() {
	if(this->currentNode != nullptr){
          if(this->currentFreq == this->currentNode->info.second){
            this->currentNode = this->currentNode->next;
            this->currentFreq = 1;
          }
          else
            this->currentFreq++;
    }
    else
      throw exception();
}

//theta(1)
void SortedBagIterator::first() {
	this->currentNode = this->bag.head;
    this->currentFreq = 1;
}

