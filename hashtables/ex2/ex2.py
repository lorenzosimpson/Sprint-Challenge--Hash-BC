#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def __repr__(self):
        return f'source: {self.source}, destination: {self.destination}'


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    
    for t in range(length):
        hash_table_insert(hashtable, tickets[t].source, tickets[t].destination)

    route[0] = hash_table_retrieve(hashtable, 'NONE')


    for i in range(1, len(route)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    route.pop()

    
    return route
    



tickets = [
  Ticket("PIT","ORD"),
  Ticket("XNA", "CID"),
  Ticket("SFO", "BHM"),
  Ticket("FLG", "XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX", "SFO"),
  Ticket("CID", "SLC"),
  Ticket("ORD", "NONE"),
  Ticket("SLC", "PIT"),
  Ticket("BHM", "FLG")
]


ht = HashTable(16)
print(reconstruct_trip(tickets, 10))