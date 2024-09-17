# Kada: [Count Odd Numbers below n](https://www.codewars.com/kata/59342039eb450e39970000a6)

## Description
Given a positive integer `n`, your task is to return the number of positive odd numbers that are less than `n`.

## Examples
```python
count_odds(7)
# should return 3
# Explanation: The odd numbers below 7 are [1, 3, 5], which totals 3.

count_odds(15)
# should return 7
# Explanation: The odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13], which totals 7.

count_odds(1)
# should return 0
# Explanation: There are no positive odd numbers below 1.

count_odds(20)
# should return 10
# Explanation: The odd numbers below 20 are [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], which totals 10.
```

### Note
- If n is less than or equal to 1, the result will be 0 as there are no positive odd numbers less than or equal to 1.