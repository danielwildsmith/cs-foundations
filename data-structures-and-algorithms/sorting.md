# Sorting Algorithms

## Quick Sort
Key Idea: Choose a pivot, partition array around pivot, recursively sort partitions

```
Initial:     [5, 2, 9, 1, 7, 6, 3]
Partition:   [2, 1, 3 | 5 | 9, 7, 6]  (pivot = 5)
Left half:   [1 | 2 | 3]              (pivot = 2)
Right half:  [6, 7 | 9]               (pivot = 9)
Final:       [1, 2, 3, 5, 6, 7, 9]
```

Core Properties:
- Divide and conquer strategy
- In-place sorting (low space complexity)
- Unstable sort
- Average case: O(n log n)
- Worst case: O(n²) when poorly pivoted
- Best case: O(n log n)

Implementation Pattern:
1. Choose pivot (usually rightmost)
2. Partition around pivot
3. Recursively sort left and right partitions

## Merge Sort
Key Idea: Divide array in half, sort each half, merge sorted halves

```
Split:                Merge:
[6,5,3,1,8,7,2,4]    
[6,5,3,1] [8,7,2,4]  
[6,5] [3,1] [8,7] [2,4]
[6] [5] [3] [1] [8] [7] [2] [4]
                      [5,6] [1,3] [7,8] [2,4]
                      [1,3,5,6] [2,4,7,8]
                      [1,2,3,4,5,6,7,8]
```

Core Properties:
- Divide and conquer
- Stable sort
- Not in-place (requires extra space)
- Always O(n log n) time complexity
- Space complexity: O(n)

Implementation Pattern:
1. Divide array into halves until single elements
2. Merge sorted arrays by comparing elements
3. Build up larger sorted arrays

## Selection Sort
Key Idea: Find minimum element, place at beginning, repeat

```
[5, 2, 9, 1, 7]   Start
[1| 5, 2, 9, 7]   Found min (1)
[1, 2| 5, 9, 7]   Found min (2)
[1, 2, 5| 9, 7]   Found min (5)
[1, 2, 5, 7| 9]   Found min (7)
[1, 2, 5, 7, 9]   Done
```

Core Properties:
- Simple implementation
- O(n²) time complexity
- In-place sorting
- Unstable sort
- Makes minimum number of swaps

Implementation Pattern:
1. Find minimum in unsorted portion
2. Swap with first unsorted position
3. Repeat for rest of array

## Insertion Sort
Key Idea: Build sorted array one item at a time, inserting each item in correct position

```
[5, 2, 9, 1, 7]   Start
[2, 5| 9, 1, 7]   Insert 2
[2, 5, 9| 1, 7]   Insert 9
[1, 2, 5, 9| 7]   Insert 1
[1, 2, 5, 7, 9]   Insert 7
```

Core Properties:
- Efficient for small data sets
- Good for nearly sorted arrays
- Stable sort
- O(n²) time complexity
- In-place algorithm

Implementation Pattern:
1. Start with first element as sorted portion
2. Take next element and insert into correct position in sorted portion
3. Repeat until all elements are sorted

## Memory Aid for Time Complexities

| Algorithm      | Best       | Average    | Worst      | Space      | Stable |
|---------------|------------|------------|------------|------------|---------|
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n)   | No      |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)       | Yes     |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)       | No      |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)       | Yes     |

## Python Implementation Tips

```python
# Built-in sorting
arr.sort()  # in-place
sorted(arr)  # returns new sorted array

# Custom sort with key function
arr.sort(key=lambda x: x[1])  # sort by second element
arr.sort(key=lambda x: (-x[0], x[1]))  # sort by first desc, then second asc

# Reverse sort
arr.sort(reverse=True)
```

## When to Use Each
- Quick Sort: General purpose, in-place sorting needed
- Merge Sort: Stable sorting required, linked lists
- Insertion Sort: Small arrays, nearly sorted data
- Selection Sort: Small arrays, minimum swaps needed
