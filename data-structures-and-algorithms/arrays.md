# Arrays

## Basic Properties
- Contiguous segments of memory that are 0-indexed
- Fixed size in static arrays, dynamic in most programming languages
- Elements must be of same data type (in typed languages)

## Time Complexities
- Access: O(1)
- Search: O(n) for unsorted, O(log n) for sorted (binary search)
- Insert/Delete: O(n) worst case
- Push/Pop at end: O(1) amortized for dynamic arrays

## Key Operations
- Traversal: forward, backward, or with specific step size
- Insertion: beginning (shift all), middle (shift partial), end (amortized O(1))
- Deletion: similar to insertion, requires shifting elements
- Resizing: typically doubles size when capacity reached (amortized O(1))
- Searching: linear scan or binary search if sorted

## Common Techniques
- Two-pointer technique
  - Fast/slow pointers
  - Start/end pointers for two-sum type problems
- Sliding window
- Prefix sums for range queries
- Kadane's algorithm for maximum subarray

## Common Problems
- Array reversal
- Rotation
- Finding duplicates
- Subarray problems (sum, product)
- Sorting algorithms
- Merging sorted arrays

## Gotchas
- Off-by-one errors with indices
- Bounds checking
- Memory limitations with large arrays
- Modifying array while iterating