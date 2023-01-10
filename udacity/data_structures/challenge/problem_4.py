class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


class ActiveDirectory:
    def __init__(self):
        self.users = dict(set())

    def add_group(self, group: Group):
        self.search_for_users(group, set())

    def search_for_users(self, group: Group, group_set: set):
        group_set.add(group.name)

        for user in group.users:
            groups = self.users.get(user)
            if groups is None:
                self.users.setdefault(user, group_set)
            else:
                groups.union(group_set)

        for inner_group in group.groups:
            self.search_for_users(inner_group, group_set.copy())

    def is_user_in_group(self, user: str, group: Group):
        """
        Return True if user is in the group, False otherwise.

        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """

        if user in self.users:
            return group.name in self.users.get(user)
        else:
            return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

parent_group = Group("parent g")
child_group = Group("child g")
child_group2 = Group("child2 g")
sub_child_group = Group("subchild g")

child_user = "child_user"
child_group.add_user(child_user)
child_group.add_group(sub_child_group)

child_user2 = "child_user2"
child_group2.add_user(child_user2)

sub_child_user = "sub_child_user"
sub_child_group.add_user(sub_child_user)

parent_group.add_group(child_group)
parent_group.add_group(child_group2)

active_directory = ActiveDirectory()
active_directory.add_group(parent_group)

print("Test 1")
print(active_directory.is_user_in_group(user=sub_child_user, group=parent_group))  # True
print(active_directory.is_user_in_group(user=sub_child_user, group=sub_child_group))  # True
print(active_directory.is_user_in_group(user=child_user2, group=child_group))  # False
print(active_directory.is_user_in_group(user=child_user, group=child_group2))  # False
print(active_directory.is_user_in_group(user=child_user, group=parent_group))  # True
print(active_directory.is_user_in_group(user=child_user2, group=parent_group))  # True

print("Test 2")
print(active_directory.is_user_in_group(user=child_user2, group=child_group))  # False

print("Test 3")
print(active_directory.is_user_in_group(user="", group=parent_group))  # False
print(
    active_directory.is_user_in_group(
        user="14325314653241562314562314652314536241562314562341232314526314526231456231426231406252341+562314",
        group=parent_group
    )
)  # False
