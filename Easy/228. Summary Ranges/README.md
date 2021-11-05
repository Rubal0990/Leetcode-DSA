# Summary Ranges
You are given a <b>sorted unique</b> integer array `nums`.

Return <i>the <b>smallest sorted</b> list of ranges that cover all the numbers in the array exactly</i>. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:
* `"a->b"` if `a != b`
* `"a"` if `a == b`
 

## Examples
```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```
```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```
```
Input: nums = []
Output: []
```
```
Input: nums = [-1]
Output: ["-1"]
```
```
Input: nums = [0]
Output: ["0"]
```

## Constraints
* 0 <= nums.length <= 20
* -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1
* All the values of nums are <b>unique</b>.
* `nums` is sorted in ascending order.
