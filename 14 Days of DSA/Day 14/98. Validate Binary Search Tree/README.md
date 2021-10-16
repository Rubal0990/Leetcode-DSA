# Validate Binary Search Tree
Given the `root` of a binary tree, <i>determine if it is a valid binary search tree (BST)</i>.

A <b>valid BST</b> is defined as follows:
* The left subtree of a node contains only nodes with keys <b>less than</b> the node's key.
* The right subtree of a node contains only nodes with keys <b>greater than</b> the node's key.
* Both the left and right subtrees must also be binary search trees.
 

## Examples
![Image 1](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)
```
Input: root = [2,1,3]
Output: true
```
![Image 2](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)
```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## Constraints
* The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
* -2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1
