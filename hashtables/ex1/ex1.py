#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for w in weights:
        hash_table_insert(ht, w, weights.index(w))
    print(ht)

    for num in weights:
        print(hash_table_retrieve(ht, num))
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

new_table = HashTable(2)
get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)