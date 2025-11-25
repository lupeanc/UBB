#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;

Bag::Bag() {
	//elements bag
	this->capacityE = 10;
	this->elements = new TElem[capacityE];
	this->current_sizeE = 0;

//positions bag
	this->capacityP = 10;
	this->positions = new TElem[capacityP];
	this->current_sizeP = 0;
}
//todo e = nr elem, p = nr pos

//	O(e) - best: if the capacity is not maxed out
// O(e+p) -worst/general
void Bag::add(TElem elem) {
	//resize elements array
	if (current_sizeE + 1 == capacityE) {
		capacityE *= 2;
		TElem* tempE = new TElem[capacityE];
		for (int i = 0; i < current_sizeE; i++)
			tempE[i] = elements[i];
		delete[] elements;
		elements = tempE;
	}

	//resize positions array
	if (current_sizeP + 1 == capacityP) {
		capacityP *= 2;
		TElem* tempP = new TElem[capacityP];
		for (int i = 0; i < current_sizeP; i++)
			tempP[i] = positions[i];
		delete[] positions;
		positions = tempP;
	}

	//insert
	bool found = false;
	for (int i = 0; i < current_sizeE; i++) {
		if (elements[i] == elem) {
			positions[current_sizeP++] = i;
			found = true;
			break;
		}
	}
	if (!found) {
		elements[current_sizeE++] = elem;
		positions[current_sizeP++] = current_sizeE - 1;
	}
}

//O(p) - best: elem is first in the elements list
// O(e*p) - worst: elem is last in the elements list
// O(e*p) - general
bool Bag::remove(TElem elem) {
	bool found_once = false, multiple_occurrences = false;

	for (int i = 0; i < current_sizeE; i++) {
		if (elements[i] == elem) {

			for (int j = 0; j<current_sizeP; j++) {
				if (positions[j] == i) {
					if (found_once == false) {
						positions[j] = positions[current_sizeP - 1];
						current_sizeP--;
						found_once = true;
					}
					else
						multiple_occurrences = true;
				}

			}

			if (found_once == true && multiple_occurrences == false) {
				elements[i] = elements[current_sizeE - 1];
				current_sizeE--;
				int pos_to_replace = current_sizeE;
				for (int j = 0; j < current_sizeP; j++) {
					if (positions[j] == pos_to_replace) {
						positions[j] = i;
					}
				}
			}
		}
	}

	if (found_once == true) {
		return true;
	}
	return false;
}

//O(1) - best
//O(e) - worst
//O(e) - general
bool Bag::search(TElem elem) const {
	for (int i = 0; i < current_sizeE; i++) {
		if (elements[i] == elem) {
			return true;
		}
	}
	return false;
}

//O(p) - best: elem is first in the elements list => only the positions list is 'walked through' fully
//O(e*p) - worst: elem is the last in the elements list
//O(e*p) - geneal
int Bag::nrOccurrences(TElem elem) const {
	int ct = 0;
	for (int i = 0; i < current_sizeE; i++) {
		if (elements[i] == elem) {
			for (int j = 0; j < current_sizeP; j++) {
				if (positions[j] == i)
					ct++;
			}
			return ct;
		}
	}

	return 0; 
}

// O(1) - all cases
int Bag::size() const {
	return current_sizeP;
}
//O(1) - all cases
int Bag::sizeE() const {
	return current_sizeE;
}
//O(1) - all cases
bool Bag::isEmpty() const {
	if (current_sizeE == 0 && current_sizeP == 0)
		return true;
	return false;
}
//O(1) - all cases
BagIterator Bag::iterator() const {
	return BagIterator(*this);
}

//O(1) - all cases
Bag::~Bag() {
	delete[] elements;
	delete[] positions;
}

//O(p) - best: the elem to be removed is the first in the list -> only complexity comes from rearranging the positions list
// O(e*p) - worst: the elem is in the last place in the list
// O(e*p) - general
int Bag::removeAllOccurrences(TElem elem) {
	bool found_once = false;
	int nrOc =0;
	//moves everything back once
	for (int i = 0; i < current_sizeE; i++) {
		if (elements[i] == elem) {
			nrOc = nrOccurrences(elem);
			for (int j = i+1; j<current_sizeE; j++) {
				elements[j-1] = elements[j];
			}
			current_sizeE--;
			found_once = true;

			for (int j = 0; j<current_sizeP; j++) {
				// if it finds the position of the deleted elem, it moves the row back one space
				if (positions[j]==i) {
					for (int k = j; k<current_sizeP; k++) {
						positions[k] = positions[k+1];
					}
					current_sizeP--;
				}
			}
			for (int j = 0; j<current_sizeP; j++) {
				// if the position is bigger than that of the deleted element => it has been -1 in the elements list
				if (positions[j]> i) {
					positions[j] = positions[j]-1;
				}
			}
			break;
		}
	}
	if (found_once == true) {
		return nrOc;
	}
	return 0;
}
