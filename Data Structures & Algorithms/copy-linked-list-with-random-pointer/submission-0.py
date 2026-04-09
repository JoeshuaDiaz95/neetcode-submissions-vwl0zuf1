"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # creating a copy of  the nodes A -> A' -> B 
        if not head:
            return None
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        
        # poiting the random nodes to the correct ones
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            
            curr = curr.next.next
        
        # Disconnecting the two nodes
        old = head
        new = head.next
        new_head = head.next

        while old:
            old_next = old.next.next
            new_next = new.next.next if new.next else None
            old.next = old_next
            new.next = new_next
            old = old_next
            new = new_next
        
        return new_head