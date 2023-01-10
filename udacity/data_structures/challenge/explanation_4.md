For this problem, I have added the ActiveDirectory class, and when using the "add_group()" method, it searches for
every user in the groups, passing a set as argument.
For each user, we are concatenating a set of groups using a dict.
This method has O(N) time complexity, it grows as much as we have groups and users.

The "is_user_in_group" method is super fast, as we use the user's name to retrieve the groups the user is in
If we find the user, we check in the group set if we match the group using a constant time operation.
Both "get" operations for the dict and set are O(1) operations, then, "is_user_in_group" is O(1)

Space complexity:
Constant space operation for "is user in group" as it uses lookups in dicts and sets, whose are constant space (O(n)) operations.
The "add_group" method is a linear space operation (O(1)), as we add new users and new sets to the dict as the number of groups and users grows.