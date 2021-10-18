# Insert into a Binary Search Tree
You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return <i>the root node of the BST after the insertion</i>. It is <b>guaranteed</b> that the new value does not exist in the original BST.

<b>Notice</b> that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return <b>any of them</b>.

## Examples
![Image 1](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)
```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:
```
![Image 2](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)
```
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```
```
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
```

## Constraints
* The number of nodes in the tree will be in the range [0, 10<sup>4</sup>].
* -10<sup>8</sup> <= Node.val <= 10<sup>8</sup>
* All the values `Node.val` are <b>unique</b>.
* -10<sup>8</sup> <= val <= 10<sup>8</sup>
* It's <b>guaranteed</b> that `val` does not exist in the original BST.
