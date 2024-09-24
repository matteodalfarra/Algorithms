# Kata: [Get the Middle Character](https://www.codewars.com/kata/56747fd5cb988479af000028)

## Description
You are given a word, and your task is to return its middle character. If the word's length is odd, return the middle character. If the word's length is even, return the middle two characters.

### Examples:
```python
get_middle("test")    # Output: "es"
get_middle("testing") # Output: "t"
get_middle("middle")  # Output: "dd"
get_middle("A")       # Output: "A"
```

### Input:
- A word (string) with a length of 0 < len(str) < 1000.

### Output:
- The middle character(s) of the word as a string.