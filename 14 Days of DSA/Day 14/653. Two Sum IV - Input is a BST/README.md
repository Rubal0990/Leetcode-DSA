# Two Sum IV - Input is a BST
Given the `root` of a Binary Search Tree and a target number `k`, return `true` <i>if there exist two elements in the BST such that their sum is equal to the given target</i>.

## Examples
![Image 1](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)
```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```
![Image 2](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)
```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```
```
Input: root = [2,1,3], k = 4
Output: true
```
```
Input: root = [2,1,3], k = 1
Output: false
```
```
Input: root = [2,1,3], k = 3
Output: true
```

## Constraints

* The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
* -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
* `root` is guaranteed to be a <b>valid</b> binary search tree.
* -10<sup>5</sup> <= k <= 10<sup>5</sup>
