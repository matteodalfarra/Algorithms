# Kata: [Encrypt This!](https://www.codewars.com/kata/5848565e273af816fb000449)

## Description
You want to create secret messages that can be deciphered by the "Decipher this!" kata. To encrypt each word in the message, follow these rules:

1. Convert the first letter of each word to its ASCII code.
2. Switch the second letter with the last letter of each word.
3. Keep the rest of the letters in the same order.

### Examples:
```python
encrypt_this("Hello")       # Output: "72olle"
encrypt_this("good")        # Output: "103doo"
encrypt_this("hello world") # Output: "104olle 119drlo"
```