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
    if length > 1:
        for w in range(length):
            hash_table_insert(ht, weights[w], w)
            
        for i in range(length):
            x = hash_table_retrieve(ht, (limit - weights[i]))
            if x:
                if x > i:
                    print([x, i])
                    return [x, i]
                else:
                    print([i, x])
                    return [i, x]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

new_table = HashTable(2)
get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
