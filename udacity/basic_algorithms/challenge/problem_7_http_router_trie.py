# A RouteTrie will store our routes and their associated handlers
from __future__ import annotations

from collections import defaultdict


class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.handler = handler
        self.root = RouteTrieNode(handler)

    def insert(self, paths: list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for path in paths:
            node = node.children[path]

        node.handler = handler

    def find(self, paths: list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(paths) == 0:
            return self.root.handler

        node = self.root

        for path in paths:
            node = node.children.get(path, None)

            if node is None:
                return None

        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path, handler):
        self.children[path].handler = handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, error_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.error_handler = error_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(self.split_path(path), handler)

    def lookup(self, path: str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.route_trie.find(self.split_path(path))
        if handler is None:
            handler = self.error_handler

        return handler

    def split_path(self, path: str):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        split_path = path.split("/")
        filtered_path = filter(lambda _path: len(_path) > 0, split_path)

        return list(filtered_path)


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'


router.add_handler("/home/about/me", "about me handler")  # add a route
print(router.lookup("/home/about/me"))  # should print 'about me handler'

print(router.lookup("/home//about///"))  # should print 'about handler'
print(router.lookup("///"))  # should print 'root handler'
print(router.lookup(""))  # should print 'root handler'