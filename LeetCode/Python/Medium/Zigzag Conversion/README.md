# Problem: [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/description/)

[My Solution](https://leetcode.com/problems/zigzag-conversion/solutions/8286467/zigzag-string-conversion-by-matteodalfar-qi4t/)

## Problem Description
Given a string `s` and an integer `numRows`, write the string in a zigzag pattern on numRows rows and then read it line by line.

Instead of explicitly drawing the zigzag, you must simulate the process and return the resulting string.

## Example Pattern
For `s = "PAYPALISHIRING"` and `numRows = 3`:
```
P   A   H   N
A P L S I I G
Y   I   R
```
Reading row by row gives:
```
PAHNAPLSIIGYIR
```

## Examples
**Input:**
```
s = "PAYPALISHIRING", numRows = 3
```
**Output:**
```
"PAHNAPLSIIGYIR"
```

**Input:**
```
s = "PAYPALISHIRING", numRows = 4
```
**Output:**
```
"PINALSIGYAHRPI"
```
**Explanation:**
```
P     I     N
A   L S   I G
Y A   H R
P     I
```

**Input:**
```
s = "A", numRows = 1
```

**Output:**
```
"A"
```

## Constraints
- `1 <= s.length <= 1000`
- `1 <= numRows <= 1000`

`s` contains English letters (lower-case and upper-case), commas, and dots.

## Intuition
The string is not actually rearranged arbitrarily: characters are placed following a **vertical-down then diagonal-up pattern**.

The key idea is to simulate row-by-row construction instead of building the full matrix.

Each character belongs to exactly one row depending on the current direction of traversal.

## Approach
1. Create row containers
We maintain a list of strings:
```python
rows = ["" for _ in range(numRows)]
```
Each element represents a row in the zigzag structure.

2. Simulate movement
We traverse the string and keep track of:
- current row index `p`
- direction (down or up)

Rules:
- Move **down** until last row
- Then move **up** until first row
- Repeat

3. Fill rows
For each character:
- Append it to `rows[p]`
- Update direction and row index accordingly

4. Build final string
Join all rows:
```python
"".join(rows)
```

## Complexity
**Time Complexity:**
$$O(n)$$
Each character is processed once.

**Space Complexity:**
$$O(n)$$
We store characters distributed across rows.

## Submission Detail
- Runtime: **13 ms**
- Memory Usage: **19.26 MB**
