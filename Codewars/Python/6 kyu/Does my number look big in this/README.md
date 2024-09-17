# Kata: [Does my number look big in this?](https://www.codewars.com/kata/5287e858c6b5a9678200083c)

## Description
A Narcissistic Number (or Armstrong Number) is a positive number that is equal to the sum of its own digits each raised to the power of the number of digits in the number. 

In this challenge, we are restricted to decimal (base 10).

### Example
For the number `153` (which has 3 digits), it is a Narcissistic Number because:
```
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```
For the number `1652` (which has 4 digits), it is not a Narcissistic Number because:
```
1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
```

### Task
Write a function that determines if a given positive integer is a Narcissistic Number.

### Input:
- A positive integer `n`.

### Output:
- `True` if `n` is a Narcissistic Number, `False` otherwise.