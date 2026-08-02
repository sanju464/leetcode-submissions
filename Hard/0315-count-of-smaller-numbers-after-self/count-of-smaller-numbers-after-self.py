class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n

        # Store (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            temp = []
            i = left
            j = mid + 1
            right_taken = 0

            while i <= mid and j <= right:
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    right_taken += 1
                    j += 1
                else:
                    ans[arr[i][1]] += right_taken
                    temp.append(arr[i])
                    i += 1

            while i <= mid:
                ans[arr[i][1]] += right_taken
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            arr[left:right + 1] = temp

        merge_sort(0, n - 1)
        return ans