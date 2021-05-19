# Whiteboard Challenges

# Reverse an Array
Given array or list reverse the items in the array or list

## Whiteboard Process
![reverse-array](./array-reverse.jpg)

# Insert to Middle of an Array
Write a function that takes in an array and a value and returns an array wit hthe new value added in the middle.

## Whiteboard Process
![shift-array](./shift-array.jpg)

## Approach & Efficiency
We used an if statements to determine where to split split an array. We then split the array, appended the 'n' to the left side, and put the arrays back together. This was an O(1) difficulty algorithm.

# Binary Search
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![binary-search](./binary_search.jpg)

## Approach & Efficiency
We split the array in two and compated the mid point to the key value. We determined if the key is larger or smaller then the mid and moved to the appropriate half of the array where we did the same thing again. This is a O(logN) beast.
