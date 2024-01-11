#!/usr/bin/python3

"""The module defines a function to check whether all boxes can be unlocked.

You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked.
"""

from typing import List, Dict


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all the boxes can be unlocked.

    Args:
        boxes: A list of lists of integers representing the boxes
        and their keys.

    Returns:
        A boolean indicating whether all the boxes can be unlocked.
    """
    box_status = {i: 'locked' for i in range(len(boxes))}
    box_status[0] = 'unlocked'

    for _ in boxes:
        unlockIteration(boxes, box_status)

    return len(set(box_status.values())) == 1


def unlockIteration(
        boxes: List[List[int]],
        box_status: Dict[int, str]
        ) -> None:
    """Unlocks boxes from left to right."""
    for i in range(len(boxes)):
        if box_status[i] == 'unlocked':
            for key in boxes[i]:
                box_status[key] = 'unlocked'
