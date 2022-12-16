def check_contains_common_items(list0, list1):
    for char in list0:
        if char in list1:
            return True
    return False
