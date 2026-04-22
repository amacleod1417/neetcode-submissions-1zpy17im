# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        prev = None
        merged = None
        mt = None
        counter = 0
        
        while curr1 is not None or curr2 is not None:

            if curr2 is None:
                if merged is None:
                    merged = curr1
                    mt = curr1
                    curr1 = curr1.next
                    

                else: 
                    mt.next = curr1
                    mt = mt.next
                    curr1 = curr1.next

            elif curr1 is None:
                if merged is None:
                    merged = curr2
                    mt = curr2
                    curr2 = curr2.next
                    
                    
                else:
                    mt.next = curr2
                    mt = mt.next
                    curr2 = curr2.next

    

            elif curr1.val <= curr2.val:
                if merged is None:
                    merged = curr1
                    mt = curr1
                    curr1 = curr1.next
                    

                else: 
                    mt.next = curr1
                    mt = mt.next
                    curr1 = curr1.next

            else:
                if merged is None:
                    merged = curr2
                    mt = curr2
                    curr2 = curr2.next
                    
                    
                else:
                    mt.next = curr2
                    mt = mt.next
                    curr2 = curr2.next

        
        return merged


        
            
            




        
