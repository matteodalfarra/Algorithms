# Problem: [Maximum Number of Balls in a Box](https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/)

## Problem Description
You are working in a ball factory where you have `n` balls numbered from `lowLimit` up to `highLimit` inclusive. An infinite number of boxes are numbered from 1 to infinity. Each ball is placed in a box where the box number is equal to the sum of the digits of the ball's number. 
Your task is to determine the maximum number of balls in any single box after placing all balls from `lowLimit` to `highLimit`.

### Example
**Input:**
```plaintext
lowLimit = 1
highLimit = 10
```
**Output:**
```plaintext
2
```
**Explanation:**
- Ball numbers and their corresponding box numbers:
    - Ball 1 goes into box 1
    - Ball 2 goes into box 2
    - ...
    - Ball 10 goes into box 1 (1 + 0 = 1)
    Box 1 has the most number of balls with 2 balls.

**Input:**
```plaintext
lowLimit = 5
highLimit = 15
```
**Output:**
```plaintext
2
```
**Explanation:**
- Ball numbers and their corresponding box numbers:
    - Ball 5 goes into box 5
    - Ball 6 goes into box 6
    - ...
    - Ball 15 goes into box 6 (1 + 5 = 6)
    Box 1 has the most number of balls with 2 balls.

### Constraints
- `1 <= lowLimit <= highLimit <= 10^5`

## Submission Detail
- Runtime: **77 ms**
- Memory Usage: **6.8 MB**