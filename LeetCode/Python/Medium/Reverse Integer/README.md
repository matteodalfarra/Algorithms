# Problem: [Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)

[My Solution](https://leetcode.com/problems/reverse-integer/solutions/8286559/integer-reversal-using-string-conversion-zrky/)

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, return `0`.

The environment does not allow storing 64-bit integers.

## Examples
**Input:**
```
x = 123
```
**Output:**
```
321
```

**Input:**
```
x = -123
```
**Output:**
```
-321
```

**Input:**
```
x = 120
```

**Output:**
```
21
```

## Constraints
- `-2^31 <= x <= 2^31 - 1`

## Intuition
The problem is essentially about reversing the digit sequence of an integer while carefully handling two edge cases:

- The sign of the number (positive or negative)
- Overflow beyond the 32-bit integer range

A straightforward idea is to treat the integer as a string, reverse its digits, and reconstruct the result.

## Approach
1. Convert the integer to a string and extract digits, ignoring the `-` sign.
2. Reverse the digit sequence.
3. Rebuild the number from the reversed digits.
4. Check if the result exceeds the 32-bit signed integer upper bound (`2^31 - 1`).
5. Apply the original sign back if the input was negative.
6. Return `0` if overflow occurs.

## Complexity
**Time Complexity:**
$$O(n)$$
Where `n` is the number of digits in `x`. We convert, reverse, and reconstruct the number.

**Space Complexity:**
$$O(n)$$
We store the digits in an auxiliary list.

## Submission Detail
- Runtime: **45 ms**
- Memory Usage: **19.08 MB**
