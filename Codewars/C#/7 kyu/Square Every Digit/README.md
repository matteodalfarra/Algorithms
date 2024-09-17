# Kada: [Square Every Digit](https://www.codewars.com/kata/546e2562b03326a88e000020)

## Description
In this kata, you are required to square every digit of a given number and concatenate the results. The function should return the final result as an integer.

## Task
Write a function that takes an integer as input, squares each of its digits, concatenates the squared results, and returns the resulting integer.

## Examples
```python
square_digits(9119)
# should return 811181
# Explanation: Squaring each digit results in 81, 1, 1, 81. Concatenating these gives 811181.

square_digits(765)
# should return 493625
# Explanation: Squaring each digit results in 49, 36, 25. Concatenating these gives 493625.

square_digits(0)
# should return 0
# Explanation: The only digit is 0, and 0 squared is 0.

square_digits(123)
# should return 149
# Explanation: Squaring each digit results in 1, 4, 9. Concatenating these gives 149.
```

### Notes
- The function should handle integers with multiple digits, including single digits.
- Ensure the result is returned as an integer and not as a string.