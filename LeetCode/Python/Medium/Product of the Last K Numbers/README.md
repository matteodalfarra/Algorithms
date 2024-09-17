# Problem: [Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/description/)

## Problem Description
Design an algorithm that accepts a stream of integers and retrieves the product of the last `k` integers of the stream.
You need to implement the `ProductOfNumbers` class with the following methods:
- **`ProductOfNumbers()`**: Initializes the object with an empty stream.
- **`void add(int num)`**: Appends the integer `num` to the stream.
- **`int getProduct(int k)`**: Returns the product of the last `k` numbers in the current list. You can assume that the current list always has at least `k` numbers.

### Example
**Input:**
```plaintext
["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"]
[[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
```
**Output:**
```
[null, null, null, null, null, null, 20, 40, 0, null, 32]
```
**Explanation:**
1. `ProductOfNumbers productOfNumbers = new ProductOfNumbers();`
    Initializes an empty stream.
2. `productOfNumbers.add(3);`
    Stream: `[3]`
3. `productOfNumbers.add(0);`
    Stream: `[3, 0]`
4. `productOfNumbers.add(2);`
    Stream: `[3, 0, 2]`
5. `productOfNumbers.add(5);`
    Stream: `[3, 0, 2, 5]`
6. `productOfNumbers.add(4);`
    Stream: `[3, 0, 2, 5, 4]`
7. `productOfNumbers.getProduct(2);`
    Returns `20`. The product of the last 2 numbers (`5 * 4`) is `20`.
8. `productOfNumbers.getProduct(3);`
    Returns `40`. The product of the last 3 numbers (`2 * 5 * 4`) is `40`.
9. `productOfNumbers.getProduct(4);`
    Returns `0`. The product of the last 4 numbers (`0 * 2 * 5 * 4`) is `0`.
10. `productOfNumbers.add(8);`
    Stream: `[3, 0, 2, 5, 4, 8]`
11. `productOfNumbers.getProduct(2);`
    Returns `32`. The product of the last 2 numbers (`4 * 8`) is `32`.

### Constraints
- `0 <= num <= 100`
- `1 <= k <= 40,000`
- At most `40,000` calls will be made to `add` and `getProduct`.
- The product of the stream at any point in time will fit in a 32-bit integer.

## Submission Detail
- Runtime: **211 ms**
- Memory Usage: **28.6 MB**