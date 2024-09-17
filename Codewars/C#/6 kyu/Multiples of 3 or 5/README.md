# Kada: [Multiples of 3 or 5](https://www.codewars.com/kata/514b92a657cdc65150000006)

## Description
Write a function that returns the sum of all natural numbers below a given number that are multiples of 3 or 5. If the input number is negative, the function should return 0.

## Task
Given a number `n`, calculate the sum of all multiples of 3 or 5 that are less than `n`. If `n` is negative, return 0.

## Examples
```python
sum_multiples(10)
# should return 23
# Explanation: The multiples of 3 or 5 below 10 are 3, 5, 6, and 9. Their sum is 23.

sum_multiples(15)
# should return 45
# Explanation: The multiples of 3 or 5 below 15 are 3, 5, 6, 9, and 12. Their sum is 45.

sum_multiples(-5)
# should return 0
# Explanation: The input number is negative, so the function returns 0.
```

### Notes
- A number is a multiple of 3 if it is divisible by 3.
- A number is a multiple of 5 if it is divisible by 5.
- Ensure that each multiple is counted only once, even if it is a multiple of both 3 and 5.
- Handle negative input by returning 0.