For the LRU Cache problem, I've chosen to use a dictionary, setting the values as nodes of a LinkedList.
For every "get()" in a dictionary, we have a Constant time lookup (O(1)), so it's the quickest way to retrieve cache information.

Regarding space complexity, it is 0(n), as the dict grows much as new items are added to the cache

Also, whenever we get data from the cache, we move the node requested to Linked List's tail.
The set method is also constant time and space operations, as it has no iterations for recursive calls.
