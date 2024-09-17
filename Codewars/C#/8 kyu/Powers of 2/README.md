# [Powers of 2](https://www.codewars.com/kata/57a083a57cb1f31db7000028)

## Description
Create a function that takes a non-negative integer `n` as input and returns a list of all the powers of 2 from \(2^0\) to \(2^n\) (inclusive).

## Examples
```python
powers_of_two(0)
# should return [1]
# Explanation: 2^0 = 1

powers_of_two(1)
# should return [1, 2]
# Explanation: 2^0 = 1, 2^1 = 2

powers_of_two(2)
# should return [1, 2, 4]
# Explanation: 2^0 = 1, 2^1 = 2, 2^2 = 4

powers_of_two(3)
# should return [1, 2, 4, 8]
# Explanation: 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8

powers_of_two(4)
# should return [1, 2, 4, 8, 16]
# Explanation: 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16
```