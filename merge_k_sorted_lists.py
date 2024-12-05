# Explain your approach in briefly only at top of your code
# Approach:
# To merge k sorted linked lists, we use a priority queue (min-heap) to keep track 
# of the smallest elements from each list. By extracting the smallest element 
# from the heap and advancing its pointer, we efficiently construct the merged list.
# The heap ensures the merging process is optimized.

# Time Complexity : O(N log k), where N is the total number of nodes, and k is the number of lists.
# Space Complexity : O(k), for the heap which holds at most k elements.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Custom comparator for ListNode for heap
        # Tuples are pushed as (node value, unique id, node)
        # Unique id ensures no comparison issues with duplicate values.
        
        min_heap = []
        
        # Push the head node of each list into the heap
        for idx, lst in enumerate(lists):
            if lst:
                heappush(min_heap, (lst.val, id(lst), lst))
        
        # Dummy node to simplify result list construction
        dummy = ListNode()
        current = dummy
        
        # Process the heap until it is empty
        while min_heap:
            # Pop the smallest element
            val, _, node = heappop(min_heap)
            current.next = node  # Add this node to the merged list
            current = current.next  # Move to the next position
            if node.next:  # If the popped node has a next node, add it to the heap
                heappush(min_heap, (node.next.val, id(node.next), node.next))
        
        # Return the head of the merged linked list
        return dummy.next
