# Problem: [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/description/)

## Problem Description
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm follows these steps:

1. **Whitespace**: Ignore any leading whitespace (`" "`).
2. **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`. If neither is present, assume positivity.
3. **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits are read, the result is `0`.
4. **Rounding**: If the integer is out of the 32-bit signed integer range `[-2³¹, 2³¹ - 1]`, round the integer to remain in the range:
   - Integers less than `-2³¹` should be rounded to `-2³¹`.
   - Integers greater than `2³¹ - 1` should be rounded to `2³¹ - 1`.
5. **Return**: Return the integer as the final result.

## Examples

### Example 1
**Input:**
```
s = "42"
```
**Output:**
```
42
```
**Explanation:**
1. No leading whitespace to ignore.
2. No `'-'` or `'+'`, so the number is positive.
3. The integer `"42"` is read in.

---

### Example 2
**Input:**
```
s = "   -042"
```
**Output:**
```
-42
```
**Explanation:**
1. Leading whitespace is ignored.
2. `'-'` is read, so the result should be negative.
3. The integer `"042"` is read in, ignoring leading zeros.

---

### Example 3
**Input:**
```
s = "1337c0d3"
```
**Output:**
```
1337
```
**Explanation:**
1. No leading whitespace to ignore.
2. No `'-'` or `'+'`, so the number is positive.
3. The integer `"1337"` is read in, stopping at the non-digit character `'c'`.

---

### Example 4
**Input:**
```
s = "0-1"
```
**Output:**
```
0
```
**Explanation:**
1. No leading whitespace to ignore.
2. No `'-'` or `'+'` at the start.
3. The integer `"0"` is read in, stopping at the `'-'` character.

---

### Example 5
**Input:**
```
s = "words and 987"
```
**Output:**
```
0
```
**Explanation:**
Reading stops at the first non-digit character `'w'`.

---

## Constraints

- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.

---

## Submission Detail
- Runtime: **9 ms**
- Memory Usage: **43.17 MB**

