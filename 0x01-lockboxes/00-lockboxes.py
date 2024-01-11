#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened with the keys available.

    Parameters:
    boxes (list of lists): A list where each element represents a box and contains a list of keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.

    The function works as follows:
    - It starts with the first box (box 0) already opened.
    - It iterates through the keys in the opened boxes, attempting to open new boxes.
    - The process continues until no new boxes can be opened or all boxes are opened.
    - The function returns True if all boxes are opened, otherwise False.
    """

    # Set to keep track of opened boxes, starting with box 0
    opened = set([0])
    
    # Set to keep track of keys available from the first box
    keys = set(boxes[0])
    
    # Loop to go through available keys and open new boxes
    while keys:
        # Set to keep track of new keys found in this iteration
        new_keys = set()
        
        # Loop through each key in the current set of keys
        for key in keys:
            # If the key is for an unopened box and the box exists
            if key not in opened and key < len(boxes):
                # Add the box to the set of opened boxes
                opened.add(key)
                # Add the keys from the newly opened box to the new keys set
                new_keys.update(boxes[key])
        
        # If no new keys are found, break out of the loop
        if not new_keys:
            break
        
        # Update the keys set with the new keys found
        keys = new_keys
    
    # Return True if all boxes have been opened, False otherwise
    return len(opened) == len(boxes)