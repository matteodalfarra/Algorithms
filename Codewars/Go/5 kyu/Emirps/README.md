# Kata: [Emirps](https://www.codewars.com/kata/55de8eabd9bef5205e0000ba)

## Description
An **emirp** is a prime number that, when reversed, yields a different prime number. Palindromic primes (numbers that read the same backward as forward) should be excluded from this definition.

For example:
- 13 is an emirp because 31 (its reverse) is also prime.
- 17 is an emirp because 71 (its reverse) is also prime.
- 757 is not an emirp because it is a palindromic prime (it reads the same backward).

Your task is to create a function that receives an upper limit `n` and returns an array with the following elements:
1. The number of emirps below `n`.
2. The largest emirp below `n`.
3. The sum of all emirps below `n`.

### Examples:
```python
find_emirp(10)
# Output: [0, 0, 0]  # No emirps below 10

find_emirp(50)
# Output: [4, 37, 98]  # There are 4 emirps below 50: 13, 17, 31, 37; largest = 37; sum = 98

find_emirp(100)
# Output: [8, 97, 418]  # There are 8 emirps below 100: 13, 17, 31, 37, 71, 73, 79, 97; largest = 97; sum = 418
```

## Task:
1. Input: An integer n (the upper limit).
2. Output: A list containing:
    - The number of emirps below n.
    - The largest emirp below n.
    - The sum of all emirps below n.