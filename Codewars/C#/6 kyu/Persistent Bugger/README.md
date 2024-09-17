# Kada: [Persistent Bugger.](https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec)

## Description
In this kata, you are tasked with finding the multiplicative persistence of a positive integer. The multiplicative persistence is defined as the number of times you must multiply the digits of the number together until you end up with a single digit.

## Task
Write a function `persistence(num)` that takes a positive integer `num` and returns its multiplicative persistence. This is the number of times you must multiply the digits of `num` together until you obtain a single digit.

## Example
For example:
```python
persistence(39)
# should return 3
# because 3 * 9 = 27, 2 * 7 = 14, 1 * 4 = 4 and 4 has only one digit, there are 3 multiplications

persistence(999)
# should return 4
# because 9 * 9 * 9 = 729, 7 * 2 * 9 = 126, 1 * 2 * 6 = 12, and finally 1 * 2 = 2, there are 4 multiplications

persistence(4)
# should return 0
# because 4 is already a one-digit number, there are no multiplications needed
```

### Notes
- The input `num` will always be a positive integer.
- If the input number is already a single digit, the persistence is 0 because no multiplication is needed.