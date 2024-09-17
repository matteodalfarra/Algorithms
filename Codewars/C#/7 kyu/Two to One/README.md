# Kada: [Two to One](https://www.codewars.com/kata/5656b6906de340bd1b0000ac)

## Description

The task is to take two input strings `s1` and `s2`, each containing only letters from 'a' to 'z'. The goal is to return a new string composed of distinct letters that appear in either `s1` or `s2`, sorted in alphabetical order.

## Task

Write a function `longest(s1, s2)` that takes two strings `s1` and `s2` and returns a new string with the following properties:
- Contains only distinct letters.
- Each letter is taken only once.
- Letters should be sorted in ascending alphabetical order.

## Example

```python
longest("xyaabbbccccdefww", "xxxxyyyyabklmopq")
# should return "abcdefklmopqwxy"

longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz")
# should return "abcdefghijklmnopqrstuvwxyz"
```

### Notes
- The resulting string should contain only distinct letters.
- The order of the letters should be alphabetical.
- The function should handle cases where s1 and s2 are the same or different.