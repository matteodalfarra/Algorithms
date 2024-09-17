# Kata: [So Many Permutations!](https://www.codewars.com/kata/5254ca2719453dcc0b00027d)

## Description
In this kata, your task is to generate all unique permutations of a given non-empty input string.

### Example
For the input `'a'`, your function should return:
```
['a']
```
For the input `'ab'`, your function should return:
```
['ab', 'ba']
```
For the input `'abc'`, your function should return:
```
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
For the input `'aabb'`, your function should return:
```
['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```

### Requirements
- The function should generate all permutations of the input string.
- Duplicate permutations should be removed if present.
- The order of the permutations does not matter.

### Input:
- A non-empty string `s`.

### Output:
- A list of unique permutations of the input string.