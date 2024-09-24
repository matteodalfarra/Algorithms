# Kada: [Find The Parity Outlier](https://www.codewars.com/kata/5526fc09a1bbd946250002dc)

## Description
You are given an array of integers, which will have a minimum length of 3. The array consists of either all odd integers or all even integers, except for a single integer \( N \). Your task is to write a method that takes the array as an argument and returns this "outlier" \( N \).

## Requirements
- Implement a function that identifies and returns the outlier from the given array.
- The outlier will be the only integer that does not match the parity (odd/even) of the rest of the integers in the array.

## Examples
- **Input:** `[2, 4, 0, 100, 4, 11, 2602, 36]`  
  **Output:** `11` (the only odd number)

- **Input:** `[160, 3, 1719, 19, 11, 13, -21]`  
  **Output:** `160` (the only even number)

## Function Signature
```cpp
int FindOutlier(const std::vector<int>& arr);
```