#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of lists): List of boxes where each box contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    if not boxes:
        return False

    n = len(boxes)
    keys = {0}
    opened_boxes = set()

    while keys:
        new_key = keys.pop()

        if new_key not in opened_boxes:
            opened_boxes.add(new_key)
            
            for key in boxes[new_key]:
                if key < n:
                    keys.add(key)
    return len(opened_boxes) == n
