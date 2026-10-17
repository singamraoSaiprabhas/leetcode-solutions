class Solution:

  def minSwaps(self, nums: list[int]) -> int:
    def get_digit_sum(n: int) -> int:
      s = 0
      while n:
        s += n % 10
        n //= 10
      return s

    n = len(nums)

    # 1. Sort based on (digit_sum, value)
    target = sorted(nums, key=lambda x: (get_digit_sum(x), x))

    # 2. Map each value to its final target position
    target_idx = {val: i for i, val in enumerate(target)}

    # 3. Find permutation cycles
    visited = [False] * n
    swaps = 0

    for i in range(n):
      # Skip if already visited or already in the correct position
      if visited[i] or target_idx[nums[i]] == i:
        continue

      cycle_size = 0
      curr = i
      while not visited[curr]:
        visited[curr] = True
        curr = target_idx[nums[curr]]
        cycle_size += 1

      if cycle_size > 1:
        swaps += cycle_size - 1

    return swaps