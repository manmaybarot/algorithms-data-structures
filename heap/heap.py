# Heap ADT


class Heap():
    def buildheap(self, A):
        for i in range((len(A) // 2) - 1, -1, -1):
            self.heapify(A, i)

    def heapify(self, A, i, sort_offset=None):
        # sort_offset for heapsort inplace
        left = (2 * i) + 1
        right = left + 1
        offset = sort_offset or len(A)

        if left >= offset and right >= offset:
            return
        elif right >= offset:
            if A[i] > A[left]:
                A[i], A[left] = A[left], A[i]
                self.heapify(A, left, offset)
        else:
            if A[i] > A[left] and A[left] <= A[right]:
                A[i], A[left] = A[left], A[i]
                self.heapify(A, left, offset)
            elif A[i] > A[right] and A[right] <= A[left]:
                A[i], A[right] = A[right], A[i]
                self.heapify(A, right, offset)

    def heappop(self, A):
        min_ele = A[0]
        new_root = A.pop(-1)
        if not A:
            return new_root
        A[0] = new_root
        self.heapify(A, 0)
        return min_ele

    def heappeak(self, A):
        return A[0]

    def heappush(self, A, ele):
        A.append(ele)
        i = len(A) - 1
        parent = self.get_parent(i)
        while parent >= 0:
            if A[parent] > A[i]:
                A[parent], A[i] = A[i], A[parent]
                i = parent
                parent = self.get_parent(i)
            else:
                break

    def get_parent(self, i):
        return i // 2 if i % 2 != 0 else (i // 2) - 1

    def heapsort(self, A):
        counter = len(A) - 1
        while counter >= 0:
            new_root = A.pop(counter)
            if counter == 0:
                A.append(new_root)
                break

            min_ele = A[0]
            A[0] = new_root
            A.append(min_ele)
            self.heapify(A, 0, counter)
            counter -= 1


if __name__ == '__main__':
    heap = Heap()

    l1 = [1, 4, 6, 7, 3, 2, -556, 3, 2, 9, 2]
    heap.buildheap(l1)

    heap.heappush(l1, -1)

    heap.heapsort(l1)
    print(l1)

    print('-----')
    heap.buildheap(l1)

    ans = []
    for i in range(len(l1)):
        ans.append(heap.heappop(l1))
    print(ans)

# push: O(log n)
# pop: O(log n)
# peek: O(1)
