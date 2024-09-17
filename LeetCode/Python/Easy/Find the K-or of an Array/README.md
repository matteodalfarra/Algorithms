# Problem: [Find the K-or of an Array](https://leetcode.com/problems/find-the-k-or-of-an-array/description/)

## Problem Description
You are given an integer array `nums` and an integer `k`. The K-or operation extends the standard bitwise OR operation. In K-or, a bit position in the result is set to 1 if at least `k` numbers in `nums` have a 1 in that position.
Return the K-or of `nums`.

### Example
**Input:**
```plaintext
nums = [7,12,9,8,9,15]
k = 4
```
**Output:**
```plaintext
9
```
**Explanation:**
| Number | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
|--------|-------|-------|-------|-------|
| 7      | 0     | 1     | 1     | 1     |
| 12     | 1     | 1     | 0     | 0     |
| 9      | 1     | 0     | 0     | 1     |
| 8      | 1     | 0     | 0     | 0     |
| 9      | 1     | 0     | 0     | 1     |
| 15     | 1     | 1     | 1     | 1     |
Result = 9 (1001 in binary)

Bit 0 is set in 7, 9, 9, and 15. Bit 3 is set in 12, 9, 8, 9, and 15. Only bits 0 and 3 qualify. The result is (1001)₂ = 9.

**Input:**
```plaintext
nums = [2,12,1,11,4,5]
k = 6
```
**Output:**
```plaintext
0
```
**Explanation:**
No bit appears as 1 in all six array numbers, as required for K-or with k = 6. Thus, the result is 0.

### Constraints
- `1 <= nums.length <= 50`
- `0 <= nums[i] < 2^31`
- `1 <= k <= nums.length`

## Submission Detail
- Runtime: **78 ms**
- Memory Usage: **11.9 MB**