# Length of Last Word
Given a string `s` consists of some words separated by spaces, <i>return the length of the <b>last</b> word in the string</i>. If the last word does not exist, return `0`.

A <b>word</b> is a maximal substring consisting of non-space characters only.

## Examples
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```
```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```
```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

## Contraints
* 1 <= s.length <= 10<sup>4</sup>
* `s` consists of only English letters and spaces `' '`.
* There will be at least one word in `s`.
