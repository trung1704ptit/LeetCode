# Database indexing

## 1. What is database index? How is it implemented under the hood?
Database index is a data structure that improves the speed of data operations on a database table at the close of additional writes and storage space to maintain the index data structure.

Database index types:
- Hash indexes
- B+Tree indexes
- SSTables

## 2. Why don’t we index every columns to support fast read?
Because we have several types of data, like boolean, we don’t need to index boolean type. Otherwise, when we update one row, if index all row, database needs to index all row again and need to storge in space => more space for this. So we don’t need to index every column

## 3. How does Hash Indexes work? What is its disadvantages?
- Base on Hash table
- Key: Hash code of the indexed columns, value: pointer to the corresponding row
- Only useful for extract loop up. Cannot support range query, unequal condition(<,>,>=, <=)
- Disadvantages of Hash Indexes:
Hash indexes don’t support partial key matching, that mean only support with single column.
Hash index support only equality comparisons: =, IN(), !=
Performance can be unstable in case of hash collision: Search: O(n), arerage O(1)

## 4. Compare B+Tree and B-Tree
- B-Tree is known as a self-balancing tree as its nodes are sorted in the inorder traversal. In B-tree, a node can have more than two children.  In the B-tree data is sorted in a specific order, with the lowest value on the left and the highest value on the right

- B+Tree eliminates the drawback B-tree used for indexing by storing data pointers only at the leaf nodes of the tree. The leaf nodes store the data pointer.

## 5. Why use B+Tree for index, not BST/AVL/Red-Black Tree
- B+Tree are self-balancing, while BST are not self-balancing => this can lead very tall tree.

- B+trees are much shorter than other balanced binary tree structures such as AVL => fewer disk access.

- If we want a range query, in order by key, B+Tree is much efficient than AVL, BST or Hash Table, because each nodes contains a large number of key with sorted key.

## 6. What is B+Tree indexes ’s disadvantage?
- More complex than Hash indexes
- Write speed is slower than LMS-tree indexes
for equality query, Hash Index is much faster. O(1) on average, B+Tree O(logN)

## 7. given B+Tree index (C1, C2, C3), can B+Tree support query on C2?
B+Tree can support query on (Col1), (Col1, Col2), (Col1, Col2, Col3).
So the anwser is No.

## 8. Compare B+Tree index and Hash index?
## 9. What happens to index when database machine crashes?
## 10.What are diff between clustered index and non-clustered index?

## 11.Should we index boolean column?