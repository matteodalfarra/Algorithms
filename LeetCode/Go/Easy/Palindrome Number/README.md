# Problem: [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)

## Problem Description
A number is called a palindrome if it reads the same backward as forward. Given an integer `x`, the task is to determine whether it is a palindrome.

### Example
**Input:**
```plaintext
x = 121
```
**Output:**
```plaintext
true
```
**Explanation:**
```plaintext
121 reads as 121 from left to right and from right to left, so it is a palindrome.
```

**Input:**
```plaintext
x = -121
```
**Output:**
```plaintext
false
```
**Explanation:**
```plaintext
From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.
```

**Input:**
```plaintext
x = 10
```
**Output:**
```plaintext
false
```
**Explanation:**
```plaintext
Reads 01 from right to left. Therefore, it is not a palindrome.
```

### Constraints
- `-2^31 <= x <= 2^31 - 1`

## Submission Detail
- Runtime: **15 ms**
- Memory Usage: **6.3 MB**