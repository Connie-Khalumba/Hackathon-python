class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Calculate middle index
            
            if nums[mid] == target:
                return mid  # Target found at mid
            
            # Check if the left side is sorted
            if nums[left] <= nums[mid]:
                # Target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right side is sorted
            else:
                # Target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1  # Target not found
    
    # Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
solution = Solution()
result = solution.search(nums, target)
print(f"Element {target} found at index {result}")

