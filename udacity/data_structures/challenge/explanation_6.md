For the "Union" method, I have used a set. Iterated over both linked lists and added each value to the set (O(1)).
This is a linear time complexity method, as it grows as with the linked lists size.

The "intersection" is doing an interation through the first linked list and adding all values to a set,
then we iterate through the second linked list and add all mathing values to a new set.
Also, linear time complexity function as it grows accordingly to the inputs.

Both functions are linear space operations, as we need new sets to cache the results.