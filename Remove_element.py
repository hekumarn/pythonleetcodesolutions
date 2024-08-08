class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Index for the next element not equal to val

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Swap it with the element at index k
                nums[k] = nums[i]
                k += 1  # Increment k

        return k