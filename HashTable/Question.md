# Questions
1. What is a Hash Function?
2. What is Hash Table?
3. What is the space complexity of a Hash Table?
4. What is the time complexity of a Hash Table?
5. When worst case happen?
6. Explain in simple terms how Hash Tables are implemented?
7. Hash Collision? How to prevent?
8. What is load factor? When do we extend the hashtable size?
9. Differentiate hashing, encoding and encryption? When to use what?
10. Why search in hashtable is O(1) on average?

# Awswer
1. What is a Hash Function?
Hash function is any function that can be used to map data of arbitrary size to fixed-size values.

2. What is Hash Table?
- A data structure of which map keys to values
- format: array of slots (buckets)
- hashtable using hash function to compute an index from key.
insert (key1, value1) into hash table T:
index = H(key1)
T[index] = value1

3. What is the space complexity of a Hash Table?
average: O(n)
worst case: O(n)

4. What is the time complexity of a Hash Table?
Search, Insert, Delete => average: O(1)
Search, Insert, Delete => worst case: O(n)

5. When worst case happen?
Hashtable suffer from O(n) worst time complexity due to reasons:
- If too many elements were hashed into the same key: looking inside this key may take O(n) time.
- Once a hash table has passed its load balance - it has to rehash [create a new bigger table, and re-insert each element to the table].

6. Explain in simple terms how Hash Tables are implemented?
Hashtable is unordered collection of key-value pairs, where each key is unique.
Hash table offer a combination of efficient lookup, insert, delete operations.

7. Hash Collision? How to prevent?
Hash collision is that has two elements with different key but has the same hash value.
How to prevent:
- Using chaning:
Each slot of the table is a linked list.
- Using Open addressing:
+ The hash table just an array, one item per slot
+ array's size is number of keys.
++ insert in open addressing:
    compute the index by hash function
    if the index is filled, probing until found an empty/deleted slot
    insert value to the empty slot


8. What is load factor? When do we extend the hashtable size?
Load factor measure how full is the hash table
example: 
hash table has 100 slots, 69 slots are filled => load factor = 69/100 = 69%
- Load factor >= 75% => double size of hash table.

9. Differentiate hashing, encoding and encryption? When to use what?
Encoding: Reversible transformation of data format, used to preserve usability of data.
Hashing: Is a one-way summary of data, cannot be reversed, used to validate the integrity of data.
Encryption: Secure encoding of data used to protect confidentiality of data.

10. Why search in hashtable is O(1) on average?
n is number of keys stored in hash table
m is number of slots in hash table
- average of length of each linked list = n / m
runtime complexity = O(1 + n/m) = O(n/m)
index = H(key)
O(n/m) ~ O(1)