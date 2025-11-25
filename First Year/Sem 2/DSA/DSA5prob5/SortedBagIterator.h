#pragma once
#include "SortedBag.h"

class SortedBag;

struct Stack
{
	BSTNode** array;
	int size;
};

class SortedBagIterator
{
	friend class SortedBag;

private:
	const SortedBag& bag;
	SortedBagIterator(const SortedBag& b);
	BSTNode* currentNode;
	Stack stack;
	int currentPosition;
	void InOrderTraversal(BSTNode* node);


public:
	TComp getCurrent();
	bool valid();
	void next();
	void first();

};
