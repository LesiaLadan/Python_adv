class BinaryNumber:
    def __init__(self, value: str) -> None:
        """Initialize a BinaryNumber from string"""
        if not all(c in "01" for c in value):
            raise ValueError("Binary number must have only 0 and 1")
        self.value = value

    def __str__(self) -> str:
        """Return a string presentation of the BinaryNumber"""
        return self.value

    def add_zeros(self, other: "BinaryNumber") -> tuple:
        """Add leading zeros to make two binary numbers the same length"""
        max_len = max(len(self.value), len(other.value))
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)
        return a, b

    def __and__(self, other: "BinaryNumber") -> "BinaryNumber":
        """Perform & between two binary numbers"""
        a, b = self.add_zeros(other)
        result = []
        for x, y in zip(a, b):
            if x == "1" and y == "1":
                result.append("1")
            else:
                result.append("0")
        result = "".join(result)
        return BinaryNumber(result)

    def __or__(self, other: "BinaryNumber") -> "BinaryNumber":
        """Perform | between two binary numbers"""
        a, b = self.add_zeros(other)
        result = []
        for x, y in zip(a, b):
            if x == "1" or y == "1":
                result.append("1")
            else:
                result.append("0")
        result = "".join(result)
        return BinaryNumber(result)

    def __xor__(self, other: "BinaryNumber") -> "BinaryNumber":
        """Perform ^ between two binary numbers"""
        a, b = self.add_zeros(other)
        result = []
        for x, y in zip(a, b):
            if x != y:
                result.append("1")
            else:
                result.append("0")
        result = "".join(result)
        return BinaryNumber(result)

    def __invert__(self) -> "BinaryNumber":
        """Invert all bits of the binary number"""
        result = []
        for x in self.value:
            if x == "0":
                result.append("1")
            else:
                result.append("0")
        result = "".join(result)
        return BinaryNumber(result)


if __name__ == "__main__":

    a = BinaryNumber("1010")
    b = BinaryNumber("1100")

    result_and = a & b
    assert str(result_and) == "1000"

    result_or = a | b
    assert str(result_or) == "1110"

    result_xor = a ^ b
    assert str(result_xor) == "0110"

    result_invert = ~a
    assert str(result_invert) == "0101"

    c = BinaryNumber("101")
    d = BinaryNumber("11010")

    result_and_diff = c & d

    assert str(result_and_diff) == "00000"

    result_or_diff = c | d
    assert str(result_or_diff) == "11111"

    result_xor_diff = c ^ d
    assert str(result_xor_diff) == "11111"

    print("All tests passed!")
