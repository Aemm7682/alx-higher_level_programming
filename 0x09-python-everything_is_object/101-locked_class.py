#!/usr/bin/python3
"""define a locked class"""


class LockedClass:
    """
    prevent the user from instantnew lockedclass attribute
    from anything but attribute called first class
    """
    __slots__ = ["first_name"]
