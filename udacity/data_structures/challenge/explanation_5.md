For this problem, I have used a dict to hold Nodes of a Linked List.
For every register_transaction call, we add a new node to the dict and move it to the tail, so, a constant space operation O(1). This operation is also constant time O(1)
The "get_data" is a linear time operation O(n) as it iterates through all items until find the node that matches the hashcode, but is a constant space O(1) operation as it doesn't need any new list

The "print_transactions_by_oldest" has linear time complexity O(n), as it iterates through the nodes and prints its data, but constant space complexity O(1) as no new objects are created
