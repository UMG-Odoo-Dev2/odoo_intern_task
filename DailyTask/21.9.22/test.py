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
            # print(nucleotide)
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
                print(getsizeof(self.bit_string))
            elif nucleotide == "B":
                self.bit_string |= 0b01
                print(getsizeof(self.bit_string))
            elif nucleotide == "C":
                self.bit_string |= 0b10
                print(getsizeof(self.bit_string))
            elif nucleotide == "D":
                self.bit_string |= 0b11
                print(getsizeof(self.bit_string))
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            # print(bits)
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "B"
            elif bits == 0b10:
                gene += "C"
            elif bits == 0b11:
                gene += "D"
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