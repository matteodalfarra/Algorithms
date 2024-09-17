# Kata: [Split Strings](https://www.codewars.com/kata/515de9ae9dcfc28eb6000001)

## Description
Your task is to complete the solution to split a string into pairs of two characters. If the string contains an odd number of characters, the final pair should be completed with an underscore (`'_'`) as the second character.

### Example
For the input `'abc'`, your function should return:
```
['ab', 'c_']
```
For the input `'abcdef'`, your function should return:
```
['ab', 'cd', 'ef']
```

### Requirements
- If the input string has an odd length, the last character should be paired with an underscore (`'_'`).
- The function should handle strings of any length.

### Input:
- A string `s` with alphabetical characters.

### Output:
- A list of strings, each containing two characters. If the length of the input string is odd, the last string in the list will contain an underscore.
