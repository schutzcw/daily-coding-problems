#include <iostream>

/*
Assumption is that r and l have an intersection point. If they don't, 
intersection() loops infinitely. Could stop with a while( i < r.size() + l.size())
check. 
*/
struct Node
{
	Node()
		: data(-1),
		  next(NULL)
	{}

	Node(int v)
		: data(v),
		  next(NULL)
	{}

	int data;
	Node* next;
};

class SinglyLinkedList
{
public:

	SinglyLinkedList()
		: mHead(NULL)
	{}

	~SinglyLinkedList()
	{}

	Node* append(int v)
	{
		Node* node = new Node(v);
		if(mHead == NULL)
		{
			mHead = node;
			mEnd  = node;
		}
		else
		{
			mEnd->next = node;
			mEnd = node;
		}
	}

	void append(Node* n)
	{
		mEnd->next = n;
	}

	Node* head() const
	{
		return mHead;
	}

	Node* node(std::size_t idx) const
	{
		std::size_t cIdx = 0;
		Node* current = mHead;
		while(current != NULL)
		{
			current = current->next;
			if(++cIdx == idx)
				break;
		}
		return current;
	}

	Node* intersection(SinglyLinkedList other)
	{
		Node* l = mHead;
		Node* r = other.head();

		while(l != r)
		{
			if(l == NULL)
			{
				l = other.head();
			}
			else
			{
				l = l->next;
			}

			if(r == NULL)
			{
				r = mHead;
			}
			else
			{
				r = r->next;	
			}
		}

		return l;
	}

	friend std::ostream& operator<<(std::ostream& os, const SinglyLinkedList& l)
	{
		Node* head = l.mHead;
		while(head != NULL)
		{
			os << head->data;
			head = head->next;
			if(head != NULL)
				os << ", ";
		}
		return os;
	}

private:

	Node* mHead;
	Node* mEnd;
};

int main(int argc, char* argv[])
{
	SinglyLinkedList l;
	l.append(3);
	l.append(6);
	l.append(8);
	l.append(15);
	l.append(30);
	l.append(50);

	SinglyLinkedList r;
	r.append(2);
	r.append(4);
	r.append(5);
	r.append(7);
	r.append(10);
	Node* meet = l.node(3);
	r.append(meet);

	std::cout << "l: " << l << std::endl;
	std::cout << "r: " << r << std::endl;

	Node* intersection = l.intersection(r);
	std::cout << "Intesection: " << intersection << ", " << intersection->data << std::endl;
	return 0;
}