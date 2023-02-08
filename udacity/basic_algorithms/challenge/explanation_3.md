Time Complexity: 
    The time complexity is O(n log n) because we are using a Heapsort algorithm, where n is the input list size.

Space Complexity:
    Space complexity is O(log n) because of the stack space used for recursion in the "heapify" method.

I chose to use a heap sort for the solution.
For the first part of the algorithm, the input list is transformed into a max heap because we can easily sort it.
Then the "find_values" sorts it, and while sorting, we check the values indexes to form the numbers. 
For every index which is a pair, we add to the first number, or to the second number if it is an even index.
For form the numbers we are making simple calculations by multiplying the numbers by 10 and adding the new value.
