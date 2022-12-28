from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self) -> Optional[TreeNode]:
        return self.left

    def get_left_child_value(self):
        if self.left is None:
            return None

        return self.left.value

    def get_right_child(self):
        return self.right

    def get_right_child_value(self):
        if self.right is None:
            return None

        return self.right.value

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"
