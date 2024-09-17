# Kata: [Roman Numerals Decoder](https://www.codewars.com/kata/51b6249c4612257ac0000005)

## Description
Create a function that takes a Roman numeral as input and returns its value as a numeric decimal integer.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. For example:
- `1990` is rendered as `"MCMXC"` (1000 = M, 900 = CM, 90 = XC)
- `2008` is rendered as `"MMVIII"` (2000 = MM, 8 = VIII)
- `1666` is rendered as `"MDCLXVI"`

### Roman Numeral Symbols:
- `I = 1`
- `V = 5`
- `X = 10`
- `L = 50`
- `C = 100`
- `D = 500`
- `M = 1,000`

### Example:
```python
roman_to_integer("MM")       # Output: 2000
roman_to_integer("MDCLXVI")  # Output: 1666
roman_to_integer("CD")       # Output: 400
roman_to_integer("XC")       # Output: 90
```