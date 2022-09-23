class CompressedGene:
    def __init__(self,gene:str)->None:
        self.compress(gene)

    def compress(self,gene:str)->None:
        self.bit_string:int=1 # set initial value int=1 
        for nucleotide in gene.upper():
            
            self.bit_string<<=2 # shift left two bits
            
            if nucleotide=="A": # change last two bits to 00
                self.bit_string|=0b00
            elif nucleotide=="C": # change last two bits to 01
                self.bit_string|=0b01
            elif nucleotide=="G": # change last two bits to 10
                self.bit_string|=0b10
            elif nucleotide=="T": # change last two bits to 11
                self.bit_string|=0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
    
    def decompress(self)->str:
        gene:str=""
        for i in range(0,self.bit_string.bit_length()-1,2):
            bits: int=self.bit_string>>i & 0b11 # get just 2 relevant bits
            if bits==0b00:
                gene+="A"
            elif bits==0b01:
                gene+="C"
            elif bits==0b10:
                gene+="G"
            elif bits==0b11:
                gene+="T"
            else:
                raise ValueError("Invalid bits: ()".format(bits))
        return gene[::-1] # [::-1] reverse string by slicing backward 
    
    def str(self) -> str: # string representation for pretty printing
        return self.decompress()

original: str="TAG"

from bz2 import decompress
import sys

compressed: CompressedGene=CompressedGene(original)

#print(sys.getsizeof(original))#54
#print(original,"\n")#TAGGG
print("Compressed Binary List {}".format(bin(compressed.bit_string)))
print(len(original)) #5
print("Original is {} bytes".format(sys.getsizeof(original)))
print("Compressed is {} bytes".format(sys.getsizeof(compressed.bit_string)))
print("Decompress is {} bytes".format(sys.getsizeof(compressed.decompress())),"\n")
print(compressed.decompress())
print("original and decompressed are the same: {} ".format(original==compressed.decompress()))