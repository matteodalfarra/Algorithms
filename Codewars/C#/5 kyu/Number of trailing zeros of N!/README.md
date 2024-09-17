# Kada: [Number of trailing zeros of N!](https://www.codewars.com/kata/52f787eb172a8b4ae1000a34)

## Description
In this kata, you are required to calculate the number of trailing zeros in the factorial of a given number. Calculating the factorial directly can be computationally expensive, especially for large numbers. Therefore, you need to find a more efficient way to determine the number of trailing zeros.

## Task
Write a function that computes the number of trailing zeros in the factorial of a given number `N`. 

## Explanation
Trailing zeros in a number are created by factors of 10, which are the result of multiplying 2 and 5. In the factorial of a number, there are always more factors of 2 than factors of 5, so the number of trailing zeros is determined by the number of times 5 is a factor in the numbers from 1 to `N`.
To find the number of trailing zeros in `N!`, count how many times 5 is a factor in the numbers from 1 to `N`. This can be done by:
1. Counting the number of multiples of 5.
2. Counting the number of multiples of \(5^2\) (25).
3. Counting the number of multiples of \(5^3\) (125), and so on.

## Examples
```python
count_trailing_zeros(6)
# should return 1

count_trailing_zeros(12)
# should return 2
```

### Additional Notes
- You are not required to compute the factorial of the number directly.
- The function should handle large values of N efficiently.