#!/usr/bin/python3
"""Module for solving the lock boxes puzzle."""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (list): List of lists, where each sublist contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    opened = [False] * len(boxes)  # Track opened status for each box
    opened[0] = True  # The first box is always opened
    keys = set(boxes[0])  # Start with keys from the first box

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and not opened[key]:
                opened[key] = True  # Mark the box as opened
                new_keys.update(boxes[key])  # Add new keys found in the box
        if not new_keys:
            break  # Exit if no new keys are found
        keys = new_keys  # Update the keys set for the next iteration

    return all(opened)  # Check if all boxes have been opened


if __name__ == '__main__':
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))
