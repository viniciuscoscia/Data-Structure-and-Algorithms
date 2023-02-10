Linear time complexity O(n), as we iterate only once to find min and max numbers, where n is the list input size.
Constant space complexity O(1), no new collections required

The strategy for this algorithm is to have two variables: One with infinite positive value for the minimum,
other with infinite negative value for the maximum.
THen, iterating through the list, we check if the current number is lower than the previous minimum, if so, 
assign the new value to the variable. The same happens to find the higher number.