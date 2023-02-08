Time Complexity: 
    Overall time complexity is O(log n), where "n" is the list size.
    For the solution, we are using binary search for both operations which is searching a Pivot and for the position 
    of the number.

Space Complexity:
    Solution Space Complexity is also O(log n) as we're using recursive binary searches. In the worst case,
    the call stack will have a max height of log n.

I chose to use binary search to solve this problem.
We start by calling the "find_pivot" method, which is a recursive method and searches the Pivot's position.
If a pivot is found, we return its position, or -1 for an ordered list.
If the list is sorted, we immediately do a binary through the entire list, either ahead of or below the pivot,
depending on the value being looked up.