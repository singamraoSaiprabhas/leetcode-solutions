class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Suffix Automaton state arrays (state 0 is the root)
        length = [0]
        link = [-1]
        cnt = [0]
        nxt = [{}]
        last = 0

        for x in nums:
            cur = len(length)
            length.append(length[last] + 1)
            link.append(0)
            cnt.append(1)  # Real state: represents a new prefix end position
            nxt.append({})

            p = last
            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][x]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(length)
                    length.append(length[p] + 1)
                    link.append(link[q])
                    cnt.append(0)  # Cloned state: does not add a new end position
                    nxt.append(nxt[q].copy())

                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        # Counting sort states by length (0..n) in O(n)
        m = len(length)
        bucket = [0] * (n + 1)
        for l in length:
            bucket[l] += 1
        for i in range(1, n + 1):
            bucket[i] += bucket[i - 1]

        order = [0] * m
        for v in range(m - 1, -1, -1):
            l = length[v]
            bucket[l] -= 1
            order[bucket[l]] = v

        # Propagate counts from longest to shortest states and track minimum unique length
        ans = n
        for v in reversed(order):
            if v == 0:
                continue
            p = link[v]
            cnt[p] += cnt[v]
            if cnt[v] == 1:
                cand = length[p] + 1
                if cand < ans:
                    ans = cand

        return ans