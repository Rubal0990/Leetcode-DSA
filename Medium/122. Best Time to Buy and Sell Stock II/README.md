# Best Time to Buy and Sell Stock II
You are given an array `prices` where `prices[i]` is the price of a given stock on the i<sup>th</sup> day.

On each day, you may decide to buy and/or sell the stock. You can only hold <b>at most one</b> share of the stock at any time. However, you can buy it then immediately sell it on the <b>same day</b>.

Find and <i>return the <b>maximum</b> profit you can achieve</i>.

## Examples
```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```

## Contraints
* 1 <= prices.length <= 3 * 10<sup>4</sup>
* 0 <= prices[i] <= 10<sup>4</sup>
