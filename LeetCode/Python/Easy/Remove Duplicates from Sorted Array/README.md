# Problem: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Problem Description
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.
Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following things:
1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
2. Return `k`.

### Custom Judge
The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.
```

### Examples
**Input:**
```plaintext
nums = [1, 1, 2]
```
**Output:**
```plaintext
2
```
**Explanation:**
Your function should return `k = 2`, with the first two elements of `nums` being `1` and `2` respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

**Input:**
```plaintext
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```
**Output:**
```plaintext
5
```
**Explanation:**
Explanation: Your function should return `k = 5`, with the first five elements of `nums` being `0`, `1`, `2`, `3`, and `4` respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

## Constraints
- `1 <= nums.length <= 30,000`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Submission Detail
- Runtime: **94 ms**
- Memory Usage: **12.82 MB**

## Approach
Since the input list is already sorted, my initial approach was to scan the elements and, upon finding a duplicate, move it to the end and shift the remaining elements left. While this method worked, it was not very efficient.

To improve efficiency, I eliminated the shifting loop. As the order of non-unique elements is irrelevant, I used an `index` variable to track where to place unique values. Each time a unique value was found, it was placed at that position and the `index` was incremented.

This approach reduces execution time by avoiding redundant manual shifting of elements.