# Kata: [Supermarket Checkout Queue](https://www.codewars.com/kata/57b06f90e298a7b53d000a86)

## Description
There is a queue for the self-checkout tills at the supermarket. Your task is to write a function that calculates the total time required for all the customers to check out given the following conditions:

- The queue is represented as an array of positive integers, where each integer represents the amount of time a customer requires to check out.
- There are `n` checkout tills available.
- The front person in the queue proceeds to a till as soon as it becomes free.

### Examples:
```python
queue_time([5, 3, 4], 1)
# Output: 12
# With 1 till, the total time is the sum of all customer times.

queue_time([10, 2, 3, 3], 2)
# Output: 10
# With 2 tills, the second, third, and fourth people finish before the first person finishes.

queue_time([2, 3, 10], 2)
# Output: 12
# With 2 tills, the total time is 12, as the 10-minute customer waits until the till becomes free.
```