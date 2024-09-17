# Kada: [Replace With Alphabet Position](https://www.codewars.com/kata/546f922b54af40e1e90001da)

## Description
Given a string, replace every letter with its position in the alphabet. Non-letter characters should be ignored and not included in the output.

## Task
Write a function that converts each letter in a string to its corresponding position in the alphabet. The position is 1-based (i.e., 'a' = 1, 'b' = 2, ..., 'z' = 26). All non-letter characters should be excluded from the output.

## Examples
```python
alphabet_position("The sunset sets at twelve o' clock.")
# should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
# Explanation: Each letter is replaced by its position in the alphabet, and non-letter characters are ignored.

alphabet_position("Hello World!")
# should return "8 5 12 12 15 23 15 18 12 4"
# Explanation: 'H' -> 8, 'e' -> 5, 'l' -> 12, 'o' -> 15, 'W' -> 23, 'r' -> 18, 'd' -> 4.

alphabet_position("123 ABC! def?")
# should return "1 2 3 4 5 6"
# Explanation: 'A' -> 1, 'B' -> 2, 'C' -> 3, 'd' -> 4, 'e' -> 5, 'f' -> 6.

alphabet_position("")
# should return ""
# Explanation: An empty string results in an empty output.
```

### Notes
- The function should ignore all non-letter characters including digits, punctuation, and whitespace.
- Ensure that the output consists of numbers separated by spaces, and there should be no trailing spaces.