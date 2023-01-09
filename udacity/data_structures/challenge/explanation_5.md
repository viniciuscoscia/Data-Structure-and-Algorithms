For this problem, I have used a dict to hold Nodes of a Linked List.
For every register_transaction call, we add a new node to the dict and move it to the tail. Those operations are Constant Time
The "get_data" is also a constant time operation as it uses the Node's hascode to retrieve the data from the dict

Only the "print_transactions_by_oldest" has linear time complexity, as it iterates through the nodes and prints it's data.