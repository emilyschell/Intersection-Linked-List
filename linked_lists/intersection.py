

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None
    cur_a = headA
    while cur_a.next:
        cur_b = headB
        while cur_a != cur_b and cur_b.next:
            cur_b = cur_b.next
        if cur_a == cur_b:
            return cur_a
        cur_a = cur_a.next
    return None
