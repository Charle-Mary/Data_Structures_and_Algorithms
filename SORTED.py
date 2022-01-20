class SortableArray:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, lp, rp):
        pivot_index = rp

        pivot = self.arr[pivot_index]

        rp = rp - 1

        while True:
            if lp >= rp:
                break

            while self.arr[lp] < pivot:
                lp += 1

            while self.arr[rp] > pivot:
                rp -= 1

            self.arr[lp], self.arr[rp] = self.arr[rp], self.arr[lp]
            lp += 1



        self.arr[lp], self.arr[pivot_index] = self.arr[pivot_index], self.arr[lp]

        return lp

    def quicksort(self, li, ri):
        if ri - li == 1:
            return

        piv = self.partition(li, ri)

        self.quicksort(li, piv - 1)
        self.quicksort(piv + 1, ri)








P = [1,2,3,4,5]

p = SortableArray(P)

p.quicksort(0, 4)


print(p.arr)



