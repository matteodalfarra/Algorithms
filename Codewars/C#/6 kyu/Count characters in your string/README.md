# Kada: [Count characters in your string](https://www.codewars.com/kata/52efefcbcdf57161d4000091)

## Description
The task is to count the occurrence of each character in a given string and return the result as a dictionary. If the string is empty, the result should be an empty dictionary.

## Task
Write a function `count_characters(s)` that takes a string `s` and returns a dictionary with the characters as keys and their corresponding counts as values.

## Example
```python
count_characters("aba")
# should return {'a': 2, 'b': 1}

count_characters("")
# should return {}
```

### Notes
- The function should handle both empty and non-empty strings.
- The dictionary keys should be the characters from the string.
- The dictionary values should represent the count of each character.