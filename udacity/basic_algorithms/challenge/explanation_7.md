RouteTrie.insert:
    Time Complexity == O(n):
        As bigger the path, the bigger the operation time as we need iterating through the nodes
    Space Complexity == O(1)
        In the worst case, it will be O(n), as we need adding new dicts for each path.
        But the best case will only need adding one more leaf nome with the handler

RouteTrie.find:
    Time Complexity == O(n):
        As bigger the path, the bigger the operation time as we need iterating through the nodes
    Space Complexity == O(1)
        No additional collections required

RouteTrieNode.insert:
    Time Complexity == O(1):
        Simple insertion to a dict
    Space Complexity == O(1)
        Simple insertion to a dict

Router.add_handler:
    Time Complexity == O(n):
        As we need using the Router.split_path method, then it is O(n).
    Space Complexity == O(n)
       As we need using the Router.split_path method, then it is O(n).

Router.lookup:
    Time Complexity == O(n):
        As we need using the Router.split_path method, then it is O(n), 
    Space Complexity == O(m)
        As we need using the Router.split_path method, then it is O(m), where "m" is the path as string.
        The bigger the quantity of paths in this string, the more space is required.

Router.split_path:
    Time Complexity == O(n):
        The bigger the path, the harder to split it.
        First, we split using '/' character, and then we filter all '/' nodes.
        Two separated iterations
    Space Complexity == O(n)
        As we add new nodes to a list and then filter, we need two new lists in total.
        It is O(n + m), then, O(n)

The solution and space/time complexities for this problem are the same from problem 5,
the difference is that when using the "add_handler" or "lookup", we have a call for the "split_path" method, and
instead of having an "enf of word" flag, each node may or not hold a handler, which is the response for the input
path