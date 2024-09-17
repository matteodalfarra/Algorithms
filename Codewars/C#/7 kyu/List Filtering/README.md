# Kada: [List Filtering](https://www.codewars.com/kata/53dbd5315a3c69eed20002dd)

## Description
Create a function that filters out strings from a list of non-negative integers and strings, returning a new list that contains only the integers.

## Task
Write a function `filter_list(lst)` that takes a list `lst` which may contain non-negative integers and strings, and returns a new list containing only the integers from the input list.

## Examples
```python
filter_list([1, 2, 'a', 'b'])
# should return [1, 2]

filter_list([1, 'a', 'b', 0, 15])
# should return [1, 0, 15]

filter_list([1, 2, 'aasf', '1', '123', 123])
# should return [1, 2, 123]
```

### Notes
- The function should handle lists that contain any mixture of non-negative integers and strings.
- Ensure that only integers are included in the returned list, and all string elements are filtered out.