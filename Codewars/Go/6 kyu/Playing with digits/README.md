# Kata: [Playing with digits](https://www.codewars.com/kata/5552101f47fc5178b1000050)

## Description
Some numbers have interesting properties. For example:

- 89 → 8¹ + 9² = 89 * 1
- 695 → 6² + 9³ + 5⁴ = 1390 = 695 * 2
- 46288 → 4³ + 6⁴ + 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given two positive integers `n` and `p`, you need to find a positive integer `k`, if it exists, such that the sum of the digits of `n` raised to consecutive powers starting from `p` equals `k * n`.

In other words, if you write the consecutive digits of `n` as `a`, `b`, `c`, `d`, ..., is there an integer `k` such that:

```
(a^p + b^(p+1) + c^(p+2) + d^(p+3) + ...) = n * k
```


If it is the case, return `k`. If not, return `-1`.

### Examples:
```python
find_k(89, 1)
# Output: 1
# 8¹ + 9² = 89, and 89 = 89 * 1

find_k(92, 1)
# Output: -1
# There is no k such that 9¹ + 2² equals 92 * k

find_k(695, 2)
# Output: 2
# 6² + 9³ + 5⁴ = 1390, and 1390 = 695 * 2

find_k(46288, 3)
# Output: 51
# 4³ + 6⁴ + 2⁵ + 8⁶ + 8⁷ = 2360688, and 2360688 = 46288 * 51
```