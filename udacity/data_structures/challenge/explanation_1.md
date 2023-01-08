For the LRU Cache problem, I've chosen to use a dictionary, setting the values as nodes of a LinkedList.
For every "get()" in a dictionary, we have a Constant time lookup (O(1)), so it's the quickest way to retrieve cache information.
Also, whenever we get data from the cache, we move the node requested to Linked List's tail.
Both get and set methods are constant time operations O(1).
