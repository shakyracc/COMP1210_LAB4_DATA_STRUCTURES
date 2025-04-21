#NOTE: Constructor: A function that creates a new instance of an ADT (like a new queue, stack, or bus object).
# makeQueue()
def makeQueue():
    return ("queue", [])
print(makeQueue())

# NOTE: Selector: A function that retrieves information from an ADT without changing it.
# contents(q)
q = ("queue", [1, 2, 3, 4, 5])
def contents(q):
    return q[1]
print(contents(q))

# NOTE: Predicate: A function that returns True or False based on some condition.
# isQueue(obj)
def isQueue(q):

    #check if type is type
    isTuple = isinstance(q, tuple)

    # check that object has two items only
    length_correct = len(q) == 2
    
    #check if first part of tuple is tagged queue
    is_queue = q[0] == "queue"
        
    #check if second part of tuple is a list
    islist = isinstance(q[1], list)

    # check all conditions
    return (isTuple and length_correct and islist and is_queue)

print(isQueue(q))

# NOTE: Mutator: A function that modifies the ADT (adds or removes something).
# enqueue(q, el)
def enqueue(q, el):
    q[1].append(el)

# NOTE: Mutator: A function that modifies the ADT (adds or removes something).
# dequeue(q, el)
def dequeue(q):
    q[1].pop(0)

# front(q)
def front(q):
    return q[1][0]

def isQueueEmpty(q):
    return len(q[1]) == 0


