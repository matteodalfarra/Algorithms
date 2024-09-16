# Kata: [Histogram V1](https://www.codewars.com/kata/57c6c2e1f8392d982a0000f2)

## Description
You are given a list of results from rolling a 6-sided die multiple times. Your task is to write code that returns a string representing a histogram based on the results, formatted as shown in the example.

### Example:
Given the results:
```
10, 5, 3, 1
```
The output should be:
```
    10
    #
    #
7   #
#   #
#   #     5
#   #     #
# 3 #     #
# # #     #
# # # 1   #
# # # #   #
-----------
1 2 3 4 5 6
```

### Task:
- You need to create a histogram that displays the frequency of each die face from 1 to 6.
- The histogram should be displayed in a character-based format, where each `#` represents one occurrence of the face value.
- The counts should be displayed above the bars, unless the count is zero.
- The output should not have any trailing spaces on the lines.
- All lines, including the last one, should end with a newline character `\n`.

### Notes:
- There are no trailing spaces on the lines.
- All lines (including the last) end with a newline `\n`.
- The number of rolls is always less than 100, so you should be able to handle the histogram generation efficiently.