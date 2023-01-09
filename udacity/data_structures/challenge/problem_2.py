import os


def find_files(suffix: str, initial_path: str):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      initial_path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []

    def recursive_file_search(path):
        for item in os.listdir(path):
            complete_path = f"{path}/{item}"

            if os.path.isfile(complete_path):
                if item.endswith(suffix):
                    paths.append(complete_path)
            elif os.path.isdir(complete_path):
                recursive_file_search(complete_path)

    recursive_file_search(initial_path)

    return paths


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".c", "testdir"))

# Test Case 2
print(find_files(".md", "testdir"))
print(find_files(".md", "./"))

# Test Case 3
print(find_files("", "testdir"))
print(find_files("", "./"))

