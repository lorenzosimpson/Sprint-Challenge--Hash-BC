# Hash Tables Sprint Challenge

For the hash tables portion of the sprint challenge, you'll be working through some algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the `.py` skeleton file, then make sure your code passes the tests by running the test script with `-v`.

A hash table implementation has been included for you already. Your task is to get the tests passing by using hash table. You can remind yourself of what hash table functions are available by looking at the `hashtable.py` file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly). 

Explain in detail the workings of a dynamic array:
What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
    -O(1) for the end, O(n) for the front
What is the worse case scenario if you try to extend the storage size of a dynamic array?
    -OS tells you there's no more contiguous memory
Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
    -Blocks are snippets of data that contain information like transactions that occured while that block was being mined, as well as a hash representation of the previous block
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?