# Debugging Compression and Decompression
## ***Compression***

original ="TAGG"

`self.bit_string = 1 ` *set bit_string =1 (01)*

`self.bit_string <<= 2 ` *shift left bit_string 2 bits* 
### ***1st character "T"***
left shift bit_string two bits >> 100<br>
cause 1st character is"T"

`elif nucleotide == "T":
                self.bit_string |= 0b11`

OR 100 and 11 = 111 (now bit_string=111)

### ***2nd character "A"***
left shift bit_string two bits >> 11100<br>
cause 2nd character is"A"

`if nucleotide == "A": 
                self.bit_string |= 0b00`

OR 11100 and 00 = 11100 (now bit_string=11100)

### ***3rd character "G"***
left shift bit_string two bits >> 1110000<br>
cause 3nd character is"G"

`elif nucleotide == "G": 
                self.bit_string |= 0b10`

OR 1110000 and 10 = 1110010 (now bit_string=1110010)

### ***4th character "G"***
left shift bit_string two bits >> 111000000<br>
cause 4th character is"G"

`elif nucleotide == "G": 
                self.bit_string |= 0b10`

OR 111000000 and 10 = 111001010 (now bit_string=1110010)


## ***Decompression***

`gene: str = ""` *set gene=" "*<br>
bit_string=111001010
`for i in range(0, self.bit_string.bit_length() - 1, 2)` *i=0,lenght of bit_string is 9(111001010)-1, i+=2*

### ***1st round***
`bits: int = self.bit_string >> i & 0b11`<br>
i=0 <br>
so right shit bit_sting 0 bit<br>
and then AND 111001010 and 11 (now bits=10)<br>
`elif bits == 0b10:
                gene += "G"`<br>
now *gene has "G"*

### ***2nd round***
`bits: int = self.bit_string >> i & 0b11`<br>
i=2 <br>
so right shit bit_sting 2 bits<br>
and then AND 001110010 and 11 (now bits=10)<br>
`elif bits == 0b10:
                gene += "G"`<br>
now *gene has "GG"*

### ***3rd round***
`bits: int = self.bit_string >> i & 0b11`<br>
i=4 <br>
so right shit bit_sting 4 bits<br>
and then AND 000011100 and 11 (now bits=00)<br>
`if bits == 0b00:
                gene += "A"`<br>
now *gene has "GGA"*

### ***4th round***
`bits: int = self.bit_string >> i & 0b11`<br>
i=6 <br>
so right shit bit_sting 6 bist<br>
and then AND 000000111 and 11 (now bits=11)<br>
`elif bits == 0b11:
                gene += "T"`<br>
now *gene has "GGAT"*

`return gene[::-1]` *will return the result in reverse like TAGG*









