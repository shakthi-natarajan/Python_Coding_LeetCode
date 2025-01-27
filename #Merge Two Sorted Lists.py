#Merge Two Sorted Lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root_node=ListNode(0)
        current_node=root_node
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                current_node.next=list1
                list1=list1.next
            else:
                current_node.next=list2
                list2=list2.next
            current_node=current_node.next
        if list1 is not None:
            current_node.next=list1
        elif list2 is not None:
            current_node.next=list2
        
        return root_node.next