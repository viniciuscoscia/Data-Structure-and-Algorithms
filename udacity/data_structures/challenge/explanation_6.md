For the "Union" method, I have used a new set. Iterated over both linked lists and added each value to the set (O(1)).
This is a linear time complexity O(n) method, as it grows as with the linked lists size.
Also, linear space complexity O(n) in the worst case scenario if all items have different values

The "intersection" is doing an interation through the first linked list and adding all values to a set,
then we iterate through the second linked list and add all mathing values to a new set.
Also, linear time complexity function O(n) as it grows accordingly to the inputs.
And also linear space complexity O(n), as we're using a new set to cache first linked list values and another set for the matching items.