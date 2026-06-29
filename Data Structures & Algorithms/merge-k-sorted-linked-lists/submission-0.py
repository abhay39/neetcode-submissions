# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp=[]
        for node in lists:
            curr = node
            while curr:
                temp.append(curr.val)
                curr = curr.next
        temp.sort()
        print(temp)
        head = None
        tail = None

        for val in temp:
            node = ListNode(val)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
        return head