# Kata: [IP Validation](https://www.codewars.com/kata/515decfd9dcfc23bb6000006)

## Description
Write an algorithm that identifies valid IPv4 addresses in dot-decimal format. An IPv4 address is considered valid if it consists of four octets with values between 0 and 255, inclusive.

### Valid Inputs:
- `1.2.3.4`
- `123.45.67.89`

### Invalid Inputs:
- `1.2.3`
- `1.2.3.4.5`
- `123.456.78.90`
- `123.045.067.089`

### Constraints:
- Leading zeros (e.g., `01.02.03.04`) are considered invalid.
- Inputs are guaranteed to be a single string.

## Examples:
```python
is_valid_ipv4("1.2.3.4")
# Output: True
# 1.2.3.4 is a valid IPv4 address.

is_valid_ipv4("123.45.67.89")
# Output: True
# 123.45.67.89 is a valid IPv4 address.

is_valid_ipv4("1.2.3")
# Output: False
# Not enough octets.

is_valid_ipv4("1.2.3.4.5")
# Output: False
# Too many octets.

is_valid_ipv4("123.456.78.90")
# Output: False
# One or more octets are out of range (256 is invalid).

is_valid_ipv4("123.045.067.089")
# Output: False
# Leading zeros are invalid.
```