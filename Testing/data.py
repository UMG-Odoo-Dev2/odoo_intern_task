class CompressedGene:
    def __init__(self,gene:str)->None:
        self.compress(gene)

    def compress(self,gene:str)->None:
        self.bit_string: int=1          #start with sentinel
        
        for nucleotide in gene.upper():
            self.bit_string<<=2         #Shift left two bits
            if nucleotide=="A":
                self.bit_string|=0b00
            elif nucleotide=="C":
                self.bit_string|=0b01
            elif nucleotide=="G":
                self.bit_string|=0b10 
            elif nucleotide=="T":
                self.bit_string|=0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
    
    def decompress(self)->str:
        gene:str=""
        for i in range(0,self.bit_string.bit_length()-1,2):
            bits: int=self.bit_string>>i & 0b11
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
        return gene[::-1]   #[::-1] reverses string by slicing backward
    
    def __str__(self) -> str: #string representation for pretty printing
        return self.decompress()

original: str="TAGGG"
import sys
print(len(original)) #5
print(sys.getsizeof(original))#54
print("original is {} bytes".format(sys.getsizeof(original)))
print(original,"\n")
compressed: CompressedGene=CompressedGene(original)
print("compressed is {} bytes".format(sys.getsizeof(compressed.bit_string)),"\n")
#print(compressed.decompress())
print(bin(compressed.bit_string))
print("original and decompressed are same size: {} ".format(original==compressed.decompress()))
print(compressed.bit_string)
print(len(bin(compressed.bit_string)))