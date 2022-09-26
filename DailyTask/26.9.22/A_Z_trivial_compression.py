from bz2 import compress, decompress
from operator import ge
from turtle import st
from unicodedata import decimal
from sys import getsizeof

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 5
            if nucleotide == "A":
                self.bit_string |= 0b00000
                print(getsizeof(self.bit_string))
            elif nucleotide == "B":
                self.bit_string |= 0b00001
                print(getsizeof(self.bit_string))
            elif nucleotide == "C":
                self.bit_string |= 0b00010
                print(getsizeof(self.bit_string))
            elif nucleotide == "D":
                self.bit_string |= 0b00011
                print(getsizeof(self.bit_string))
            elif nucleotide == "E":
                self.bit_string |= 0b00100
                print(getsizeof(self.bit_string))
            elif nucleotide == "F":
                self.bit_string |= 0b00101
                print(getsizeof(self.bit_string))
            elif nucleotide == "G":
                self.bit_string |= 0b00110
                print(getsizeof(self.bit_string))
            elif nucleotide == "H":
                self.bit_string |= 0b00111
                print(getsizeof(self.bit_string))
            elif nucleotide == "I":
                self.bit_string |= 0b01000
                print(getsizeof(self.bit_string))
            elif nucleotide == "J":
                self.bit_string |= 0b01001
                print(getsizeof(self.bit_string))
            elif nucleotide == "K":
                self.bit_string |= 0b01010
                print(getsizeof(self.bit_string))
            elif nucleotide == "L":
                self.bit_string |= 0b01011
                print(getsizeof(self.bit_string))
            elif nucleotide == "M":
                self.bit_string |= 0b01100
                print(getsizeof(self.bit_string))
            elif nucleotide == "N":
                self.bit_string |= 0b01101
                print(getsizeof(self.bit_string))
            elif nucleotide == "O":
                self.bit_string |= 0b01110
                print(getsizeof(self.bit_string))
            elif nucleotide == "P":
                self.bit_string |= 0b01111
                print(getsizeof(self.bit_string))
            elif nucleotide == "Q":
                self.bit_string |= 0b10000
                print(getsizeof(self.bit_string))
            elif nucleotide == "R":
                self.bit_string |= 0b10001
                print(getsizeof(self.bit_string))
            elif nucleotide == "S":
                self.bit_string |= 0b10010
                print(getsizeof(self.bit_string))
            elif nucleotide == "T":
                self.bit_string |= 0b10011
                print(getsizeof(self.bit_string))
            elif nucleotide == "U":
                self.bit_string |= 0b10100
                print(getsizeof(self.bit_string))
            elif nucleotide == "V":
                self.bit_string |= 0b10101
                print(getsizeof(self.bit_string))
            elif nucleotide == "W":
                self.bit_string |= 0b10110
                print(getsizeof(self.bit_string))
            elif nucleotide == "X":
                self.bit_string |= 0b10111
                print(getsizeof(self.bit_string))
            elif nucleotide == "Y":
                self.bit_string |= 0b11000
                print(getsizeof(self.bit_string))
            elif nucleotide == "Z":
                self.bit_string |= 0b11001
                print(getsizeof(self.bit_string))
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 5):
            bits: int = self.bit_string >> i & 0b11
            # print(bits)
            if bits == 0b00000:
                gene += "A"
            elif bits == 0b00001:
                gene += "B"
            elif bits == 0b00010:
                gene += "C"
            elif bits == 0b00011:
                gene += "D"
            if bits == 0b00100:
                gene += "E"
            elif bits == 0b00101:
                gene += "F"
            elif bits == 0b00110:
                gene += "G"
            elif bits == 0b00111:
                gene += "H"
            if bits == 0b01000:
                gene += "I"
            elif bits == 0b01001:
                gene += "J"
            elif bits == 0b01010:
                gene += "K"
            elif bits == 0b01011:
                gene += "L"
            if bits == 0b01100:
                gene += "M"
            elif bits == 0b01101:
                gene += "N"
            elif bits == 0b01110:
                gene += "O"
            elif bits == 0b01111:
                gene += "P"
            if bits == 0b10000:
                gene += "Q"
            elif bits == 0b10001:
                gene += "R"
            elif bits == 0b10010:
                gene += "S"
            elif bits == 0b10011:
                gene += "T"
            if bits == 0b10100:
                gene += "U"
            elif bits == 0b10101:
                gene += "V"
            elif bits == 0b10110:
                gene += "W"
            elif bits == 0b10111:
                gene += "X"
            if bits == 0b11000:
                gene += "Y"
            elif bits == 0b11001:
                gene += "Z"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    original: str = "a"
    print("Original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))