# Kata: [Next Smaller Number with Same Digits](https://www.codewars.com/kata/5659c6d896bc135c4c00021e)

## Description
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits. If no such number exists, return `-1`. Numbers with leading zeros are not allowed.

### Examples:
```python
next_smaller(21)    # Output: 12
next_smaller(531)   # Output: 513
next_smaller(2071)  # Output: 2017
next_smaller(9)     # Output: -1
next_smaller(135)   # Output: -1
next_smaller(1027)  # Output: -1
```

### Input 
- A positive integer.

### Output
- The next smaller positive integer containing the same digits, or -1 if no valid smaller number exists.