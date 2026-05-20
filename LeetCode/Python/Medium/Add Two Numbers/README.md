# Problem: [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

[My Solution](https://leetcode.com/problems/add-two-numbers/solutions/8281439/add-two-numbers-linked-list-addition-by-o1lxx/)

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit.

Your task is to add the two numbers and return the sum as a linked list in the same reversed format.

You may assume the numbers do not contain leading zeros, except for the number 0 itself.

## Examples
**Input:**
```
l1 = [2,4,3], l2 = [5,6,4]
```
**Output:**
```
[7,0,8]
```
**Explanation:**  
342 + 465 = 807 → reversed result: 7 → 0 → 8

**Input:**
```
l1 = [0], l2 = [0]
```
**Output:**
```
[0]
```

**Input:**
```
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
```
**Output:**
```
[8,9,9,9,0,0,0,1]
```

## Constraints
- Number of nodes in each linked list: `[1, 100]`
- `0 <= Node.val <= 9`
- No leading zeros except the number 0 itself

## Submission Detail
- Runtime: **2 ms**
- Memory Usage: **19.40 MB**
