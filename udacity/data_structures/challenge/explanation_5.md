For this problem, I have used a dict to hold Nodes of a Linked List.
For every register_transaction call, we add a new node to the dict and move it to the tail, so, a constant space operation O(1). Those operations are Constant Time
The "get_data" is also a constant time operation as it uses the Node's hashcode to retrieve the data from the dict

Only the "print_transactions_by_oldest" has linear time complexity, as it iterates through the nodes and prints its data.

All functions are constant space operations, no new collections are required.