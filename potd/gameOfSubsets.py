'''
https://practice.geeksforgeeks.org/problems/cec5db442a5652d07dd41e37ea780345f08c9a3d/1

Explaination:
The problem is to count the number of good subsets of an array arr, where a subset is considered good if its product can be represented as a product of one or more distinct prime numbers. The solution uses dynamic programming to count the number of good subsets.

The solution maintains a bitmask dp of length 1024 (2^10) where each bit represents the presence or absence of a distinct prime factor in the subset. For example, the bit at position i represents the presence or absence of the ith prime number (2, 3, 5, 7, 11, 13, 17, 19, 23, 29) in the subset. The value of dp[j] represents the number of good subsets whose bitmask is j. Initially, dp[0] = 1 because the empty subset has a product of 1 which can be represented as the product of no prime numbers.

The solution processes each element of the input array and updates the bitmask dp accordingly. For each element i in the input array, if i is equal to 1, it is ignored because 1 has no prime factors. Otherwise, the bitmask cnt is updated to reflect the presence of prime factors in i. The bitmask cnt is used to update the bitmask dp for each possible prime factor. Specifically, for each prime factor j, if i is divisible by j (i.e., i % j == 0), then the bit representing j is set in the bitmask mask. The updated bitmask mask is then used to update the bitmask dp for each subset whose bitmask is a valid superset of mask. Specifically, for each bitmask j that is a valid superset of mask, the value of dp[j] is incremented by dp[j - mask] * cnt[i] because a subset whose bitmask is j can be obtained by taking any subset whose bitmask is j - mask and including cnt[i] instances of i.

Finally, the solution returns the sum of all values in the dp bitmask, minus 1 (to exclude the empty subset), multiplied by 2 to the power of the number of occurrences of 1 in the input array. This multiplication corresponds to the number of ways of including or excluding the number 1 in each good subset.
'''

from typing import List


class Solution:
    # Initialize the bitmask mp to represent the presence or absence of each prime factor
    def __init__(self):
        self.mod = int(1e9 + 7)
        self.mp = [0] * 31
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(2, 31):
            if i % 4 == 0 or i % 9 == 0 or i == 25:
                continue
            mask = 0
            for j in range(10):
                if i % primes[j] == 0:
                    mask |= 1 << j
            self.mp[i] = mask

    # Compute a^b mod mod using binary exponentiation
    def pow(self, n: int) -> int:
        ans, m = 1, 2
        while n != 0:
            if n & 1 == 1:
                ans = (ans * m) % self.mod
            m = (m * m) % self.mod
            n >>= 1
        return ans

    # Count the number of good subsets of arr
    def goodSubsets(self, n: int, arr: List[int]) -> int:
        # Count the number of occurrences of each element in arr and update cnt and mp
        one = 0
        dp = [0] * 1024
        cnt = [0] * 31
        dp[0] = 1
        for i in arr:
            if i == 1:
                one += 1
            elif self.mp[i] != 0:
                cnt[i] += 1

        # Update dp using dynamic programming
        for i in range(31):
            if cnt[i] == 0:
                continue
            for j in range(1024):
                if j & self.mp[i] != 0:
                    continue
                dp[j | self.mp[i]] = (dp[j | self.mp[i]] +
                                      dp[j] * cnt[i]) % self.mod

        # Compute the total number of good subsets
        ans = sum(dp) % self.mod - 1
        if one != 0:
            ans = (ans * self.pow(one)) % self.mod

        return ans


'''
The __init__ method initializes the bitmask mp to represent the presence or absence of each prime factor using the primes list. The bitmask mp[i] is set to a bitmask mask where the jth bit is set if and only if i is divisible by the jth prime in primes. The pow method computes 2^n modulo mod using binary exponentiation.

The goodSubsets method counts the number of good subsets of the input array arr. The one variable counts the number of occurrences of 1 in arr. The dp variable represents the bitmask of each subset whose product is a product of one or more distinct prime numbers. The cnt variable counts the number of occurrences of each element in arr that has at least one prime factor. The dp[0] = 1 initializes the count of the empty subset to 1. The first loop updates cnt and one. The second loop updates dp using dynamic programming as described above. The last block of code computes the total number of good subsets and multiplies it by 2^one to account for including or excluding the number 1 in each good subset.
'''