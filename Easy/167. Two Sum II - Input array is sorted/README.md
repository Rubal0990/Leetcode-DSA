# Two Sum II - Input array is sorted
Given a <b>1-indexed</b> array of integers `numbers` that is already <b>sorted in non-decreasing order</b>, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= first < second <= numbers.length`.

Return <i>the indices of the two numbers,</i> `index1` <i>and</i> `index2`<i>, as an integer array</i> `[index1, index2]` <i>of length 2</i>.

The tests are generated such that there is <b>exactly one solution</b>. You <b>may not</b> use the same element twice.

 

## Examplea
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
```
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
```

## Constraints
* 2 <= numbers.length <= 3 * 10<sup>4</sup>
* -1000 <= numbers[i] <= 1000
* `numbers` is sorted in <b>non-decreasing order</b>.
* -1000 <= target <= 1000
* The tests are generated such that there is <b>exactly one solution</b>.
