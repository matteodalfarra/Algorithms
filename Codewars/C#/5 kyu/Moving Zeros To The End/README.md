# Kada: [Moving Zeros To The End](https://www.codewars.com/kata/52597aa56021e91c93000cb0)

## Description
The goal of this algorithm is to move all the zeros in an array to the end while preserving the order of the non-zero elements. 

## Task
Write a function `move_zeros(arr)` that takes an array `arr` and returns a new array with all zeros moved to the end, maintaining the order of the other elements.

## Example
```python
move_zeros([1, 0, 1, 2, 0, 1, 3])
# should return [1, 1, 2, 1, 3, 0, 0]
```

### Notes
- The input array can contain any type of elements, but only zeros should be moved.
- The order of non-zero elements should remain the same.
- Zeros should be moved to the end of the array, not added to the beginning.