class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result <<= 1          # Make room for next bit
            result |= (n & 1)     # Copy last bit of n
            n >>= 1               # Remove last bit

        return result
