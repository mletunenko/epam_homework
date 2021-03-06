"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    if isinstance(tree, (str, bool, int)):
        if tree == element:
            return 1
    elif isinstance(tree, dict):
        for key in tree:
            counter += find_occurrences(tree[key], element)
    elif isinstance(tree, (list, tuple, set)):
        for unit in tree:
            counter += find_occurrences(unit, element)
    return counter


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
