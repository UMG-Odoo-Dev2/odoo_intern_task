# class CompressedGen:
#     def __init__(self, ch: str) -> None:
#         self._compressed(ch)

#     def _compressed(self, ch: str):
#         gene = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         self.bit_string = 1
#         for i in ch:
#             for j in gene:
#                 if i == j:
#                     self.bit_string <<=2
#                     self.bit_string |= 0b01
#                 else:
#                     raise ValueError("Invalid Nucleotide:{}".format(i))
# if __name__ == "__main__":
#     from sys import getsizeof
#     original: str = "HELLO"
#     compress: CompressedGen = CompressedGen(original)
#     print("compressed is {} bytes".format(getsizeof(compress.bit_string)))

from bz2 import compress, decompress
from operator import ge
from turtle import st
from unicodedata import decimal


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            for i in range(65, 91):
                self.bit_string <<= 5
                if nucleotide == chr(i):
                    self.bit_string |= i
                    print(i)
if __name__ == "__main__":
    from sys import getsizeof
    original: str = "hello welcome"
    print("Original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))