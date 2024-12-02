# Kata: [Range Extraction](https://www.codewars.com/kata/51ba717bb08c1cd60f00002f)

## Problem Description

You are given a list of integers in increasing order. Your task is to return a correctly formatted string that summarizes the ranges in the list. 

### Rules
- A range is defined as three or more consecutive numbers (e.g., `1, 2, 3` becomes `1-3`).
- If there are fewer than three consecutive numbers, they should appear as individual numbers in the result.
- Each range or individual number should be separated by a comma in the final output.

### Examples

#### Input
```python
[-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
```

#### Output
```python
"-10--8,-6,-3-1,3-5,7-11,14-15,17-20"
```