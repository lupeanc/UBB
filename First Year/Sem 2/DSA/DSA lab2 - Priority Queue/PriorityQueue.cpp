
#include "PriorityQueue.h"
#include <exception>
using namespace std;

//0(capacity)
PriorityQueue::PriorityQueue(Relation r) {
	this->rel = r;
	this->capacity = 10;
	this->head = -1;
	this->tail = -1;
	this->firstEmpty = 0;
	this->nodes = new Node[capacity];
	for(int i = 0; i < capacity - 1; i++) {
		nodes[i].next = i+1;
	}
	nodes[capacity - 1].next = -1;
	this->size = 0;
}

//0(capacity)
void PriorityQueue::resize() {
	Node* newNodes = new Node[this->capacity * 2];
	int index;
	for (index = 0; index < this->capacity; index++) {
		newNodes[index] = this->nodes[index];
	}
	for(index = this->capacity; index < this->capacity * 2 -1; index++) {
		newNodes[index].next = index + 1;
	}
	this->firstEmpty = this->capacity;
	this->capacity *= 2;
	newNodes[this->capacity - 1].next = -1;
	delete[] this->nodes;
	this->nodes = newNodes;
}

//0(1)
void PriorityQueue::push(TElem e, TPriority p) {
	if (this->size == this->capacity)
		this->resize();
	int newNodePos = this->firstEmpty;
    //first empty gets the position of the next spot in the array
	this->firstEmpty = this->nodes[firstEmpty].next;
	this->size++;
    //if queue is empty and e is the first elem
	if (this->tail == -1) {
		this->nodes[newNodePos].info.first = e;
		this->nodes[newNodePos].info.second = p;
		this->nodes[newNodePos].next = -1;
		this->head = newNodePos;
		this->tail = newNodePos;
	} else {
		this->nodes[tail].next = newNodePos;
		this->nodes[newNodePos].prev = tail;
		this->nodes[newNodePos].info.first = e;
		this->nodes[newNodePos].info.second = p;
		this->nodes[newNodePos].next = -1;
		this->tail = newNodePos;
	}
}


//0(size)
Element PriorityQueue::top() const {
	if (this->size == 0)
		throw exception();
	int current = this->head;
	Element elem = this->nodes[this->head].info;
	while (current != this->nodes[this->tail].next) {
		if(this->rel(this->nodes[current].info.second, elem.second)) {
			elem.first = this->nodes[current].info.first;
			elem.second = this->nodes[current].info.second;
		}
		current = this->nodes[current].next;
	}
	return elem;
}

//BC: 0(1)
//WC: 0(size)
Element PriorityQueue::pop() {
	if (this->size == 0) {
		throw exception();
	} else {
		int current = this->head;
		Element topValue = top();
		//finds the elem
		while (current != this->nodes[this->tail].next && !(this->nodes[current].info.first == topValue.first &&
			   this->nodes[current].info.second == topValue.second)) {
			current = this->nodes[current].next;
			   }
		Element ret;
		if (current == this->head) {
			ret.first = this->nodes[this->head].info.first;
			ret.second = this->nodes[this->head].info.second;
			if (this->size == 1) {
				this->head = -1;
				this->tail = -1;
				this->nodes[current].next = this->firstEmpty;
				this->firstEmpty = current;
			} else {
				this->head = this->nodes[current].next;
				this->nodes[this->head].prev = -1;
				this->nodes[current].next = this->firstEmpty;
				this->firstEmpty = current;
			}
			this->size--;
		} else if (current == this->tail) {
			ret.first = this->nodes[this->tail].info.first;
			ret.second = this->nodes[this->tail].info.second;
			this->tail = this->nodes[current].prev;
			this->nodes[this->tail].next = -1;
			this->nodes[current].next = this->firstEmpty;
			this->firstEmpty = current;
			this->size--;
		} else if (current != this->nodes[this->tail].next) {
			ret.first = this->nodes[current].info.first;
			ret.second = this->nodes[current].info.second;
			this->nodes[this->nodes[current].prev].next = this->nodes[current].next;
			this->nodes[this->nodes[current].next].prev = this->nodes[current].prev;
			this->nodes[current].next = this->firstEmpty;
			this->firstEmpty = current;
			this->size--;
		}
		return ret;
	}
}

//BC: 0(1)
//WC: 0(size)
bool PriorityQueue::search(TElem elem) const{
	int currentPos = this->head;
	bool found = false;
	//while the elem has not been found, and we have not finished going through the list...
	while (found == false && currentPos != this->nodes[this->tail].next) {
		//if we have found the elem, found becomes true
		if (this->nodes[currentPos].info.first == elem) {
			//return true;
			found = true;
		}
		//current ++
		currentPos = this->nodes[currentPos].next;
	}
	//returns true if the elem has been found, false if otherwise
	return found;
	//return false;
}

//0(1)
bool PriorityQueue::isEmpty() const {
	if (this->size == 0)
		return true;
	return false;
}

//0(1)
PriorityQueue::~PriorityQueue() {
	delete[] this->nodes;
};

