from bz2 import decompress


class CompressedGene:
    def __init__(self,char:str)->None:
        self._compress(char)

    def _compress(self,gene:str)->None:
        self.bit_string: int=1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00000
            elif nucleotide == "B":
                self.bit_string |= 0b00001
            elif nucleotide == "C":
                self.bit_string |= 0b00010
            elif nucleotide == "D":
                self.bit_string |= 0b00011
            elif nucleotide == "E":
                self.bit_string |= 0b00100
            elif nucleotide == "F":
                self.bit_string |= 0b00101
            elif nucleotide == "G":
                self.bit_string |= 0b00110
            elif nucleotide == "H":
                self.bit_string |= 0b00111
            elif nucleotide == "I":
                self.bit_string |= 0b01000
            elif nucleotide == "J":
                self.bit_string |= 0b01001
            elif nucleotide == "K":
                self.bit_string |= 0b01010
            elif nucleotide == "L":
                self.bit_string |= 0b01011
            elif nucleotide == "M":
                self.bit_string |= 0b01100
            elif nucleotide == "N":
                self.bit_string |= 0b01101
            elif nucleotide == "O":
                self.bit_string |= 0b01110
            elif nucleotide == "P":
                self.bit_string |= 0b01111
            elif nucleotide == "Q":
                self.bit_string |= 0b10000
            elif nucleotide == "R":
                self.bit_string |= 0b10001
            elif nucleotide == "S":
                self.bit_string |= 0b10010
            elif nucleotide == "T":
                self.bit_string |= 0b10011
            elif nucleotide == "U":
                self.bit_string |= 0b10100
            elif nucleotide == "V":
                self.bit_string |= 0b10101
            elif nucleotide == "W":
                self.bit_string |= 0b10110
            elif nucleotide == "X":
                self.bit_string |= 0b10111
            elif nucleotide == "Y":
                self.bit_string |= 0b11000
            elif nucleotide == "Z":
                self.bit_string |= 0b11001
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str=""
        
        for i in range (0, self.bit_string.bit_length() - 1,2):
            bits: int = self.bit_string >> i & 0b11001
            if bits == 0b00000:
                gene += "A"
            elif bits == 0b00001:
                gene += "B"
            elif bits == 0b00010:
                gene += "C"
            elif bits == 0b00011:
                gene += "D"
            elif bits == 0b00100:
                gene += "E"
            elif bits == 0b00101:
                gene += "F"
            elif bits == 0b00110:
                gene += "G"
            elif bits == 0b00111:
                gene += "H"
            elif bits == 0b01000:
                gene += "I"
            elif bits == 0b01001:
                gene += "J"
            elif bits == 0b01010:
                gene += "K"
            elif bits == 0b01011:
                gene += "L"
            elif bits == 0b01100:
                gene += "M"
            elif bits == 0b01101:
                gene += "N"
            elif bits == 0b01110:
                gene += "O"
            elif bits == 0b01111:
                gene += "P"
            elif bits == 0b10000:
                gene += "Q"
            elif bits == 0b10001:
                gene += "R"
            elif bits == 0b10010:
                gene += "S"
            elif bits == 0b10011:
                gene += "T"
            elif bits == 0b10100:
                gene += "U"
            elif bits == 0b10101:
                gene += "V"
            elif bits == 0b10110:
                gene += "W"
            elif bits == 0b10111:
                gene += "X"
            elif bits == 0b11000:
                gene += "Y"
            elif bits == 0b11001:
                gene += "Z"
            else:
             raise ValueError("Invalid bits{}".format(bits))
        return gene[::-1]
        
    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original:str = "ABCD"
    print ( "orginal is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print(bin(compressed.bit_string))
    print ("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)

    decompress: CompressedGene = CompressedGene(original)
    print(bin(decompress.bit_string))
    print(decompress)
    print("decompressd is {} bytes".format(getsizeof(decompress.decompress())))

    print ("original and decompressed are the same: {}".format(original == compressed.decompress()))
    