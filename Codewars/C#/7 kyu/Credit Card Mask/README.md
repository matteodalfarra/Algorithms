# Kada: [Credit Card Mask](https://www.codewars.com/kata/5412509bd436bd33920011bc)

## Description
The task is to mask all but the last four characters of a given string, typically used to obscure sensitive information such as credit card numbers or phone numbers. The masking should replace all characters except for the last four with the `#` symbol.

## Task
Write a function `maskify(cc)` that takes a string `cc` and returns a new string where all but the last four characters are replaced with `#`. 

## Examples
```python
maskify("4556364607935616")
# should return "############5616"

maskify("64607935616")
# should return "#######5616"

maskify("1")
# should return "1"

maskify("")
# should return ""

maskify("Skippy")
# should return "##ippy"

maskify("Nananananananananananananananana Batman!")
# should return "####################################man!"
```

### Notes
- Ensure that if the input string is empty or has a length of 4 or fewer characters, the function returns the original string unchanged.
- The resulting masked string should always end with the last four characters of the input string, with all preceding characters replaced by #.