class QuickSelect:
    def partition(self, arr, l, r):
        pivot = arr[r]
        i = l  # this is used always swap elements with an elements that wasnt swaped befor
        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def kth_smallest(self, arr, left, right, k):
        if 0 < k <= right - left + 1:
            index = self.partition(arr, left, right)
            if index - left == k - 1:
                return arr[index]
            if index - left > k - 1:
                return self.kth_smallest(arr, left, index - 1, k)
            return self.kth_smallest(arr, index + 1, right, k - index + left - 1)
        return 'Index out of bound'
