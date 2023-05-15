'''
https://practice.geeksforgeeks.org/problems/1132bd8ee92072cd31441858402641d6800fa6b3/1
'''
class Solution:
    def countBits(self, N : int) -> int:
        # ans = 0
        # for i in range(1,N+1):
        #     # ans += sum(list(map(int,bin(i)[2:])))
        #     for j in bin(i)[2:]:
        #         ans+=int(j)
        # return ans
        if N <= 1:
            return N
        set_bits = 0
        # Find the position of the most significant bit
        bits = N.bit_length()
        highest_pow_2 = 2**(bits - 1)
        # Half of the bits in numbers < "2^(bits - 1)" are set to "1"
        # and they are occupying only "bits - 1" bits
        set_bits += highest_pow_2 * (bits - 1) // 2
        remaining_numbers = N - (highest_pow_2 - 1)
        # We are left with a subproblem but each number
        # now has an extra bit at position "bits" set to 1
        # and the numbers start from zero so we decrease it by 1
        set_bits += remaining_numbers + self.countBits(remaining_numbers - 1)
        return set_bits
        
        

