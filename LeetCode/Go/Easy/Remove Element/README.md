# Problem: [Remove Element](https://leetcode.com/problems/remove-element/description/)

## Problem Description
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

### Example
**Input:**
```plaintext
nums = [3,2,2,3]
val = 3
```
**Output:**
```plaintext
2, nums = [2,2,_,_]
```
**Explanation:**
Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

**Input:**
```plaintext
nums = [0,1,2,2,3,0,4,2]
val = 2
```
**Output:**
```plaintext
5, nums = [0,1,4,0,3,_,_,_]
```
**Explanation:**
Your function should return k = 5, with the first five elements containing 0, 1, 4, 0, and 3.
The order of these elements can vary, and the remaining elements do not matter.

### Constraints
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Submission Detail
- Runtime: **2 ms**
- Memory Usage: **2.37 MB**

## Approach
To solve this algorithm, I decided to iterate through each element of the array. If the current element is different from the one passed as a parameter (`val`), I place it in the first available position, incrementing the variable that tracks the next available index. If the current element is equal to the given number, I simply continue to the next iteration.

This approach allows the array to be modified in-place without needing to move elements manually or shift them, optimizing the overall performance.