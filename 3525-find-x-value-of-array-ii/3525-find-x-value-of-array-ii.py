# class Solution:
#     def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        
class Node:
    def __init__(self, k=5):
        self.remain = [0] * k
        self.prod = 1

class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def merge(self, left, right):
        res = Node(self.k)
        res.prod = (left.prod * right.prod) % self.k
        for i in range(self.k):
            res.remain[i] = left.remain[i]
        for i in range(self.k):
            res.remain[(i * left.prod) % self.k] += right.remain[i]
        return res

    def build(self, nums, cur, left, right):
        if left == right:
            self.tree[cur].remain[nums[left]] = 1
            self.tree[cur].prod = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, 2 * cur + 1, left, mid)
        self.build(nums, 2 * cur + 2, mid + 1, right)
        self.tree[cur] = self.merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])

    def update(self, treeIndex, lo, hi, i, val):
        if lo == hi:
            for j in range(self.k):
                self.tree[treeIndex].remain[j] = 0
            self.tree[treeIndex].remain[val] = 1
            self.tree[treeIndex].prod = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self.update(2 * treeIndex + 1, lo, mid, i, val)
        else:
            self.update(2 * treeIndex + 2, mid + 1, hi, i, val)
        self.tree[treeIndex] = self.merge(self.tree[2 * treeIndex + 1], self.tree[2 * treeIndex + 2])

    def query(self, treeIndex, lo, hi, i, j):
        if i <= lo and hi <= j:
            return self.tree[treeIndex]
        mid = (lo + hi) // 2
        if j <= mid:
            return self.query(2 * treeIndex + 1, lo, mid, i, j)
        if i > mid:
            return self.query(2 * treeIndex + 2, mid + 1, hi, i, j)
        return self.merge(
            self.query(2 * treeIndex + 1, lo, mid, i, j),
            self.query(2 * treeIndex + 2, mid + 1, hi, i, j)
        )

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        nums = [x % k for x in nums]
        for q in queries:
            q[1] %= k

        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []

        for index, value, start, x in queries:
            tree.update(0, 0, n - 1, index, value)
            res_node = tree.query(0, 0, n - 1, start, n - 1)
            ans.append(res_node.remain[x])

        return ans