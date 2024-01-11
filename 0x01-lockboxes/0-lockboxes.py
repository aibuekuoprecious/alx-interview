#!/usr/bin/python3

def canUnlockAll(boxes):
    opened = set([0])  # Start with box 0 opened
    keys = set(boxes[0])  # Get the keys from the first box
    while keys:
        new_keys = set()
        for key in keys:
            if key not in opened and key < len(boxes):
                opened.add(key)
                new_keys.update(boxes[key])
        if not new_keys:
            break
        keys = new_keys
    return len(opened) == len(boxes)