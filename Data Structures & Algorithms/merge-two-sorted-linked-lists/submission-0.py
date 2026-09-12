class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Ek dummy node banate hain jisse result list ka starting point yaad rahe
        dummy = ListNode()
        current = dummy

        # Jab tak dono lists mein nodes bache hain, unhe compare karo
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Chote node ko current ke aage jodo
                list1 = list1.next    # list1 ko ek kadam aage badhao
            else:
                current.next = list2  # Agar list2 choti (ya barabar) hai toh use jodo
                list2 = list2.next    # list2 ko ek kadam aage badhao
            
            # Current pointer ko agle node par shift karo taaki aage ki list ban sake
            current = current.next

        # Agar koi ek list jaldi khatam ho jaye, toh doosri list ke bache hue nodes direct jod do
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Dummy node khud empty tha, hamari asli list uske 'next' se shuru hoti hai
        return dummy.next