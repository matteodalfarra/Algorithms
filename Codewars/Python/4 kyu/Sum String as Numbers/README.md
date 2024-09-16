# Kata: [Sum Strings as Numbers](https://www.codewars.com/kata/5324945e2ece5e1f32000370)

## Description
Given the string representations of two integers, return the string representation of the sum of those integers.

### Example:
```python
sumStrings('1', '2') // => '3'
```

### Constraints:
- A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
- In Java, the use of `BigInteger` and `BigDecimal` has been removed, so solutions must handle large numbers without using these classes.
- In Python, your solution must work with very large numbers (up to about a million digits), meaning direct conversion to `int` will not work.

## Objective
- Create a function that takes two string arguments representing large integers and returns their sum as a string.
- Ensure the function handles very large inputs efficiently, especially in Python where integers can reach up to a million digits.