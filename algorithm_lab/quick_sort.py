class Quicksort:

    list_for_sorting = []

    def __init__(self, list):
        self.list_for_sorting = list

    def quick_sort(self, low, hi):
        if low < hi:
            p = self.partition(low, hi)
            self.quick_sort(low, p-1)
            self.quick_sort(p+1, hi)
            pass

    def pivot(self, low, hi):
        mid = int((hi+low)/2)
        pivot = hi

        if self.list_for_sorting[low].capacity < self.list_for_sorting[mid].capacity:
            if self.list_for_sorting[mid].capacity < self.list_for_sorting[hi].capacity:
                pivot = mid

        elif self.list_for_sorting[low].capacity < self.list_for_sorting[hi].capacity:
            pivot = low

        return pivot

    def partition(self, low, hi):
        pivot_index = self.pivot(low, hi)
        pivot_value = self.list_for_sorting[pivot_index]
        self.list_for_sorting[pivot_index], self.list_for_sorting[low] = self.list_for_sorting[low], self.list_for_sorting[pivot_index]

        border = low

        for i in range(low, hi+1):
            if self.list_for_sorting[i].capacity < pivot_value.capacity:
                border+=1
                self.list_for_sorting[i], self.list_for_sorting[border] = self.list_for_sorting[border], self.list_for_sorting[i]

        self.list_for_sorting[low], self.list_for_sorting[border] = self.list_for_sorting[border], self.list_for_sorting[low]


        return border