# Happy Number
Write an algorithm to determine if a number `n` is happy.

A <b>happy number</b> is a number defined by the following process:
* Starting with any positive integer, replace the number by the sum of the squares of its digits.
* Repeat the process until the number equals 1 (where it will stay), or it <b>loops endlessly in a cycle</b> which does not include 1.
* Those numbers for which this process <b>ends in 1</b> are happy.

Return `true` <i>if</i> `n` <i>is a happy number, and</i> `false` <i>if not</i>.

## Examples
```
Input: n = 19
Output: true
```
```
Input: n = 2
Output: false
```

## Constraints
* 1 <= n <= 2<sup>31</sup> - 1
