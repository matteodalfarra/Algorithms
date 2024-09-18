# Problem: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)

## Problem Description
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. The task is to convert a given Roman numeral string into its corresponding integer value.

### Symbols and Values
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

### Rules
- Roman numerals are usually written from largest to smallest from left to right.
- There are six instances where subtraction is used:
  - I before V (5) and X (10) results in 4 and 9.
  - X before L (50) and C (100) results in 40 and 90.
  - C before D (500) and M (1000) results in 400 and 900.

### Examples:
**Input:**
```plaintext
s = "III"
```
**Output:**
```plaintext
3
```
**Explanation:**
```plaintext
III = 3.
```

**Input:**
```plaintext
s = "MCMXCIV"
```
**Output:**
```plaintext
1994
```
**Explanation:**
```plaintext
M = 1000, CM = 900, XC = 90, IV = 4. Hence, 1000 + 900 + 90 + 4 = 1994.
```

### Constraints
- `1 <= s.length <= 15`
- `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999].

## Submission Detail
- Runtime: **34 ms**
- Memory Usage: **11.6 MB**