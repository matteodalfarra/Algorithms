# Kata: [Remove the minimum](https://www.codewars.com/kata/563cf89eb4747c5fb100001b)

## Description
The Museum of Incredibly Dull Things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

Your task is to write a program that tells her the ratings of the exhibits after removing the lowest one.

### Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

### Examples
- **Input**: `[1, 2, 3, 4, 5]`  
  **Output**: `[2, 3, 4, 5]`
- **Input**: `[5, 3, 2, 1, 4]`  
  **Output**: `[5, 3, 2, 4]`
- **Input**: `[2, 2, 1, 2, 1]`  
  **Output**: `[2, 2, 2, 1]`

## Input:
- `numbers`: A list of integers where each integer represents the rating of an exhibit. The list can be empty.

## Output:
- Returns a new list of integers with the smallest value removed. The original list should remain unchanged.