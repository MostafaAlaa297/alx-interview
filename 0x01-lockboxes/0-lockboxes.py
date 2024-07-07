#!/usr/bin/python3
"""
lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem.
    """
    if not isinstance(boxes, list) or not boxes:
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
