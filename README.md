# COMP1210_LAB4_DATA_STRUCTURES

Tuples, Sets, Dictionaries, Lists, Linked Lists, Stacks
and Queues
1. Brief Discussion on Tuples, Sets, Dictionaries, Lists, Linked Lists, Stacks and Queues.
2. One way to determine whether an integer is even is to divide the number by two and check the remainder. Write a one-line program that prompts for a number, converts the input to an integer, and prints a zero if the number is even and a one if the number is odd.
3. Using list comprehension create an expression that sums up all the factors of a number that you input. (Hint: If you input 6, it should print 12 (i.e., 1 + 2 + 3 + 6 = 12).)
4. Given x=‘March 7, 2024’:
(a) Using list comprehension, create a list of all the letters used in x.
(b) In one line, add to your list comprehension so the resulting list is sorted.
5. In Queues the insertion and deletion of elements occur at different ends of the list. The items in the queue that are inserted first will be removed first (FIFO). A queue data structure can be represented as a tuple, where the first part of the tuple is a tag ‘queue’ and the second part is a list of items in the queue.

Implement the following functions for the queue ADT:
- makeQueue() – Constructor – Return an empty queue as a tuple, where first part of the tuple is a tag ‘queue’ and second part of the tuple is an empty list.
- contents(q) – Selector – Takes a queue as input and returns the list of items in the queue.
- isQueue(obj) – Predicate – Checks to determine if a given object is queue. A given object is of type queue if it is a tuple, if the first part of the tuple is a tag ‘queue’ and the second part of the tuple is a list.
- enqueue(q, el) – Mutator – Takes a queue and an element as input and adds the given element to the back of the queue.
- dequeue(q) – Mutator – Takes a queue as input and removes the first element in the list.
- front (q) – Selector – Takes a queue as an input and returns the element in the front of the list.
- isQueueEmpty(q) – Predicate – Checks to see if a given queue is empty.

