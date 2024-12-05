# Explain your approach in briefly only at top of your code
# Approach:
# To find the kth largest element in the array without fully sorting it, 
# we use a min-heap of size k. The heap maintains the k largest elements seen so far.
# The smallest element in this heap will be the kth largest element.
# We iterate through the array, ensuring the heap size does not exceed k.

# Time Complexity : O(n log k), where n is the size of nums.
# Space Complexity : O(k), as the heap stores k elements.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap to keep track of the k largest elements
        min_heap = []
        
        # Iterate through all elements in the array
        for num in nums:
            heappush(min_heap, num)  # Push the current number into the heap
            if len(min_heap) > k:   # If the heap exceeds size k
                heappop(min_heap)   # Remove the smallest element in the heap
        
        # The root of the heap will be the kth largest element
        return min_heap[0]  # Return the smallest element in the heap (kth largest overall)
