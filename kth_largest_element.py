
import heapq

def find_kth_largest(nums, k):
    # Create a min-heap with the first k elements
    heap = nums[:k]
    heapq.heapify(heap)
    
    # For the rest of the elements, maintain the size of the heap as k
    for num in nums[k:]:
        if num > heap[0]:  # Only add the element if it's bigger than the smallest element in the heap
            heapq.heapreplace(heap, num)
    
    # The root of the heap is the Kth largest element
    return heap[0]
# Example 
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
result = find_kth_largest(nums, k)
print(f"The {k}th largest element is {result}")

