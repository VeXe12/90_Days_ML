class BitManipulator:
    
    @staticmethod
    def is_even(n):
        """
        Checks if n is even using AND.
        Logic: Even numbers always end in 0 in binary.
        """
        # n & 1 returns 1 if the last bit is 1 (odd), else 0 (even)
        return (n & 1) == 0

    @staticmethod
    def get_bit(n, pos):
        """Returns the bit at position 'pos' (0-indexed)."""
        mask = 1 << pos
        return 1 if (n & mask) else 0

    @staticmethod
    def set_bit(n, pos):
        """Sets the bit at position 'pos' to 1."""
        mask = 1 << pos
        return n | mask

    @staticmethod
    def clear_bit(n, pos):
        """Sets the bit at position 'pos' to 0."""
        mask = ~(1 << pos)
        return n & mask

    @staticmethod
    def toggle_bit(n, pos):
        """Flips the bit at position 'pos'."""
        mask = 1 << pos
        return n ^ mask

    @staticmethod
    def count_set_bits(n):
        """
        Brian Kernighan’s Algorithm:
        Counts how many 1s are in the binary representation.
        Time Complexity: O(k) where k is the number of 1s.
        """
        count = 0
        while n > 0:
            n = n & (n - 1)  # The Magic Trick: Clears the lowest set bit
            count += 1
        return count

    @staticmethod
    def lowest_set_bit(n):
        """
        Isolates the lowest 1 bit.
        Used extensively in Fenwick Trees (Binary Indexed Trees).
        Example: 12 (1100) -> 4 (0100)
        """
        return n & (-n)

    @staticmethod
    def xor_swap(a, b):
        """
        Swaps two numbers without a temporary variable.
        Note: In Python, a, b = b, a is preferred, but this demonstrates XOR logic.
        """
        if a == b: return a, b
        
        a = a ^ b
        b = a ^ b  # (a ^ b) ^ b = a
        a = a ^ b  # (a ^ b) ^ a = b
        return a, b

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    bm = BitManipulator()
    
    # 1. Parity Check
    num = 42  # 101010
    print(f"Is {num} even? {bm.is_even(num)}") # True
    
    # 2. Manipulation
    print(f"\nOriginal: {bin(num)}")
    print(f"Set bit 0:  {bin(bm.set_bit(num, 0))} (Should be 43)")
    print(f"Toggle bit 1: {bin(bm.toggle_bit(num, 1))} (Should be 40)")
    
    # 3. Counting Bits (Brian Kernighan's)
    # 42 is 101010 -> 3 set bits
    print(f"\nSet bits in 42: {bm.count_set_bits(42)}") 
    
    # 4. XOR Swap
    x, y = 10, 20
    x, y = bm.xor_swap(x, y)
    print(f"\nSwapped: x={x}, y={y}")
    
    # 5. Fenwick Tree Logic (Isolate Lowest Bit)
    # 12 is 1100. Lowest bit is the '4' position.
    print(f"\nLowest set bit of 12 (1100): {bm.lowest_set_bit(12)} (0100)")