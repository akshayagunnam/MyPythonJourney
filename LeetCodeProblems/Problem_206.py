#Given the head of a singly linked list, reverse the list, and return the reversed list.
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return head
        elif head.next == None:
            return head
        current = head
        next_ = current.next
        while next_.next != None:
            now = next_.next
            next_.next = current
            current = next_
            next_ = now
        next_.next = current
        head.next = None
        return next_
