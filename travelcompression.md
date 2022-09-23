# Trivial Compression and decompresson

    class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
 ## ***Compression***



original ="TAGG"

 self.bit_string: int = 1
### ***1st character "T"***

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            
            self.bit_string <<= 2
            
            if nucleotide == "T":
                self.bit_string |= 0b00
                
left shift bit_string two bit >> 100
cause 1st character is"T"

OR 100 and 11 = 111 (now bit_string=111)

### ***2nd character "A"***
    elif nucleotide == "A":
                self.bit_string |= 0b01


left shift bit_string two bit >> 11100
cause 2nd character is"A"

OR 11100 and 00 = 11100 (now bit_string=11100)

### *** char G***
    elif nucleotide == "G":
                self.bit_string |= 0b10
 increase left shift bit_string two bit >> 1110000
cause 3rd  character is"G"

OR 1110000 and 10 = 1110010 (now bit_string=1110010)

### ***4th character "G"***
    elif nucleotide == "G":
                self.bit_string |= 0b11
 increaseleft shift bit_string two bit >> 111000000
cause 4th character is"G"

OR 111000000 and 10 = 111001010 (now bit_string=1110010)


## ***Decompression***