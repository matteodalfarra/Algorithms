# Kada: [Count Smiley Faces](https://www.codewars.com/kata/583203e6eb35d7980400002a)

## Description
This kata challenges you to count the number of smiling faces in an array. A smiling face is defined by specific characters that must appear in a certain pattern.

## Task
You need to create a function that takes an array of strings as input and returns the total number of valid smiling faces. A valid smiling face must meet the following criteria:
- The eyes can be represented by `:` or `;`.
- The nose is optional and can be represented by `-` or `~`.
- The mouth must be `)` or `D`.

## Examples
```python
count_smileys([':)', ';(', ';}', ':-D'])
# should return 2

count_smileys([';D', ':-(', ':-)', ';~)'])
# should return 3

count_smileys([';]', ':[', ';*', ':$', ';-D'])
# should return 1
```

### Additional Notes
- The input array will only contain valid strings.
- The function should handle empty arrays by returning 0.