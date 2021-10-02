# Ransom Note
Given two stings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

## Examples
```
Input: ransomNote = "a", magazine = "b"
Output: false
```
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

## Constraints
* 1 <= ransomNote.length, magazine.length <= 10<sup>5</sup>
* `ransomNote` and `magazine` consist of lowercase English letters.
