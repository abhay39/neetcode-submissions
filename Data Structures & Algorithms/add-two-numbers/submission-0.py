class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        # Keep looping if there are digits left in l1, l2, OR if a carry remains
        while l1 or l2 or carry:
            # Get values or 0 if a list has already finished
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum including the incoming carry
            total_sum = val1 + val2 + carry
            
            # Extract new carry and the node value
            carry = total_sum // 10    # e.g., 12 // 10 = 1 (goes to next turn)
            node_val = total_sum % 10   # e.g., 12 % 10 = 2 (goes into current node)
            
            # Create the node with the units digit
            current.next = ListNode(node_val)
            current = current.next
            
            # Safely move pointers forward
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
