import sys
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
        
    def _compress(self, gene: str) -> None:
        self.bit_string = 1 # start with sentinal
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # shift left 2 mits
            if nucleotide == "A": 
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G": 
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
                
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): # -1 to exclude sentinal
            bits: int = self.bit_string >> i & 0b11             # get 2 relevant bits
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalide bits: ()".format(bits))
        return gene[::-1]  #reverse string
    
    def __str__(self) -> str:
        return self.decompress()

if __name__== "__main__":
    from sys import getsizeof
    original: str="A"*15
    print("Originnal is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print("Decompressed is {} bytes".format(getsizeof(compressed.decompress())))
    print("Original and decompressed are the same: {}".format(original==compressed.decompress()))
    print(bin(compressed.bit_string))
    #print(len(bin(compressed.bit_string)))
    #print(compressed.bit_string)