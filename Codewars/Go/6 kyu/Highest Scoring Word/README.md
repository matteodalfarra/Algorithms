# Kata: [Highest Scoring Word](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272)

## Description
Given a string of words, return the word with the highest score.

Each letter in a word scores points according to its position in the alphabet: 
- `a = 1`, `b = 2`, `c = 3`, etc.

The word score is the sum of the letter scores. If two words have the same score, return the one that appears first in the string.

### Example:
```python
high("abad cbbd") 
# Output: "cbbd"
```

### Constraints:
- All letters will be lowercase.
- Inputs will always be valid strings consisting of space-separated words.