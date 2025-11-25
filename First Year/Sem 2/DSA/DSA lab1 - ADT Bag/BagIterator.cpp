#include <exception>
#include "BagIterator.h"
#include "Bag.h"

using namespace std;


BagIterator::BagIterator(const Bag& c): bag(c)
{
	index=0;
}

//O(1) - all cases
void BagIterator::first() {
	index = 0;
}

//O(1) - all cases
void BagIterator::next() {
	if (index >= bag.size())
		throw exception();
	index ++;
}

// O(1) - all cases
bool BagIterator::valid() const {
	if (index<bag.size()) {
		return true;
	}
	return false;
}

//O(1) - all cases
TElem BagIterator::getCurrent() const
{
	if (index < bag.size())
		return bag.elements[bag.positions[index]];
	throw exception();
}
