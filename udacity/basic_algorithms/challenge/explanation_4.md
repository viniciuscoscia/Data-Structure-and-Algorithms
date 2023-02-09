Time complexity: 
    For this problem, the time complexity is O(n) as we iterate through the list once in all cases.

Space Complexity:
    For this problem, it's O(1), as no new collections are required or recursive calls.

The logic behind this algorithm is to iterate through the list only once, moving the 0s to the beginning of the 
list and the 2s to the end of the list. It uses one variable to store the last zero or two indexes,
which moves backwards (two) or forwards (zero).
After moving all 0s and 2s, all the 1s will be automatically organized.
