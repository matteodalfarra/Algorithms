# Kada: [Build Tower](https://www.codewars.com/kata/576757b1df89ecf5bd00073b)

## Description
The task is to build a pyramid-shaped tower represented as an array of strings, given a positive integer number of floors. Each block of the tower is represented with the character `*`. 

### Requirements
Create a function that generates a tower with the specified number of floors. The tower should be centered and each floor should consist of an increasing number of blocks. The widest part of the tower will be at the bottom.

### Examples
- **Input**: `3`  
  **Output**: 
  ```python
  [
    "  *  ",
    " *** ", 
    "*****"
  ]
  ```
- **Input**: `6`  
  **Output**: 
  ```python
    [
    "     *     ", 
    "    ***    ", 
    "   *****   ", 
    "  *******  ", 
    " ********* ", 
    "***********"
    ]
  ```

## Input:
- `floors`: A positive integer representing the number of floors in the tower.

## Output:
- Returns a list of strings representing the pyramid-shaped tower. Each string represents a single floor of the tower.