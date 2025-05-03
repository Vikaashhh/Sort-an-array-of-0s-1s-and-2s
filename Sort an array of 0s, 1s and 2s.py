class Solution:
    # Function to sort an array of 0s, 1s, and 2s without using inbuilt sort
    def sort012(self, arr):
        low = 0           # 0s ke liye pointer
        mid = 0           # current element pointer
        high = len(arr) - 1  # 2s ke liye pointer

        # Jab tak mid pointer high se chhota ya equal hai
        while mid <= high:
            if arr[mid] == 0:
                # 0 mila toh low aur mid wale elements ko swap karo
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # 1 mila toh aage badho
                mid += 1
            else:
                # 2 mila toh mid aur high swap karo, par mid ko mat badhao
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1



# ✅ Sample Test
if __name__ == "__main__":
    obj = Solution()
    arr = [0, 1, 2, 0, 1, 2, 1, 0]
    obj.sort012(arr)
    print("Sorted array:", arr)  # Output: [0, 0, 0, 1, 1, 1, 2, 2]
