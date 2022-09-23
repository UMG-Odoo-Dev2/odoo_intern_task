# Trivial Compression
- Firstly, set to 
```
original: str="TAGGG"
```
```
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
```
- In Class CompressedGene,
  - Start for loop,
  - bit_string start with sentinel int=1
  - and then, Shift left two bits bit_string >> 100
  - if first str="T"(we set above TAGGG) therefore self.bit_string of T is 11, and 100|11, the result is>> 111,

  - (Second)For loop, Shift left two bits bit_string >> 11100
  - if second str="A" therefore self.bit_string of A is 00, and 11100|00, the result is>> 1110000,

  - (Third)For loop, Shift left two bits bit_string >> 1110000
  - if third str="G" therefore self.bit_string of G is 10, and 1110000|10, the result is>> 1110010,

  - (Four)For loop, Shift left two bits bit_string >> 111001000
  - if third str="G" therefore self.bit_string of G is 10, and 111001000|10, the result is>> 111001010,
  
  - (Five)For loop, Shift left two bits bit_string >> 11100100000
  - if third str="G" therefore self.bit_string of G is 10, and 11100100000|10, the result is>> 11100101010,
  - End Loop
### Output: (For Compression)
```
0b11100101010
compressed is 28 bytes
```
# Decompresssion
```
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
        return gene[::-1]   

    def __str__(self) -> str: 
        return self.decompress()
``` 
- In decompresss,
  - first, above bit_str is 9 (11100101010)
``` 
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
```
  - Start for i in (0,9-1,2): , bit
  - i=0
  - bit_str= 11100101010 | 11 ,  result is 01 (G)
  - Second for Loop i=2,
  - bit_str= 00111001010 | 11 ,  result is 01 (G)
  - Third for Loop i=4,
  - bit_str= 00001110010 | 11 ,  result is 01 (G)
  - Fourth for Loop i=6,
  - bit_str= 00000011100 | 11 ,  result is 00 (A)
  - Fifth for Loop i=4,
  - bit_str= 00000000111 | 11 ,  result is 11 (T)
```
return gene[::-1]
```
- Therefore, Output is:
```
TAGGG
```
