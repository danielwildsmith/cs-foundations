# Hashmaps

## Basic Properties
- Stores key-value pairs using hash function to map keys to array indices
- Handles collisions via chaining (linked lists) or open addressing
- Load factor (n/k) determines when to resize to maintain performance
- Keys must be immutable in most implementations

## Time Complexities
- Average Case:
    - Insert: O(1)
    - Delete: O(1) 
    - Search: O(1)
    - Access: O(1)
- Worst Case (rare, with many collisions):
    - All operations: O(n)

## Key Concepts
- Hash Function
    - Converts key into array index
    - Should distribute values uniformly
    - Must be deterministic (same input → same output)
- Collision Resolution
    - Chaining: each bucket contains linked list of entries
    - Open Addressing: probe sequence to find next empty slot
        - Linear probing
        - Quadratic probing
        - Double hashing
- Dynamic Resizing
    - Grows when load factor exceeds threshold
    - Typically doubles size and rehashes all elements

## Common Applications
- Caching
- Counting frequencies
- Two-sum type problems
- De-duplication
- Symbol tables
- Fast access to data by identifier

## Implementation Considerations
- Initial capacity choice
- Load factor threshold
- Hash function quality
- Key equality comparison
- Memory usage vs performance tradeoff