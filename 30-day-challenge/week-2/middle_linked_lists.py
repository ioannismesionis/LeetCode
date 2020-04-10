# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.


# Example 1:

# Input: [1, 2, 3, 4, 5]
# Output: Node 3 from this list(Serialization: [3, 4, 5])
# The returned node has value 3.  (The judge's serialization of this node is [3, 4, 5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1, 2, 3, 4, 5, 6]
# Output: Node 4 from this list(Serialization: [4, 5, 6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Note:

# The number of nodes in the given list will be between 1 and 100.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def lengthNode(self, node):
        # length of list is 1 in the beginning
        length = 1

        # while there is still next
        # increment length
        while node.next != None:
            length += 1
            node = node.next
        # return the length of the list
        return length

    def middleNode(self, head):
        length = self.lengthNode(head)
        # capture the middle of the list
        middle = (length//2) + 1
        counter = 1
        while (counter != middle):
            counter += 1
            head = head.next

        return head

# UPDATE:
# Using the fast-low pointers below


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # hare and tortoise start at the same time
        hare = head
        tortoise = head

        # while we can iterate
        # update the hare twice
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

        # return tortoise as the momoment hare finishes
        # tortoise will be at the half (middle) of the ListNode
        return tortoise
