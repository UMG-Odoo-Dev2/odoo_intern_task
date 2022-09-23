# Trivial Compression

## Tracing
### Compression
- Set a original string you want to compress
  - <span style="color:green">original: str="TAG"</span>

- Create a variable and set a initial value
  - <span style="color:green">self.bit_string: int=1 (01)</span>

- Start ***For*** Looping and initially shift left two bits on 
  - <span style="color:green">self.bit_string<<=2 </span>

  Left shift bit_string two bits is now => 100
  > 1st Char 'T'
  ```
  nucleotide=="T":
      self.bit_string|=0b11
  ```
  - now do OR with 100 and 0b11
  - bit_string will be = 111
  > 2nd Char 'A'
  ```
  nucleotide=="A": 
      self.bit_string|=0b00
  ```
  - do OR with 111 and 0b00
  - bit_string will be = 11100
  > 3rd Char 'G'
  ```
  nucleotide=="G":
      self.bit_string|=0b10
  ```
  - now do OR with 11100 and 0b10
  - bit_string will be = 1110010
  - Output of Compress Binary List = 0b1110010
  - Origin size of string is 52 bytes
  - Compressed size of string is 28 bytes

### Decompression

  ```
  gene: str = "" 
  for i in range(0, self.bit_string.bit_length() - 1, 2)
  ```

  - set gene=" "
  - bit_string=1110010
  - i = 0
  - lenght of bit_string is 7(1110010)-1, i+=2*

> 1st Round
```
bits: int = self.bit_string >> i & 0b11
```
  - i=0
  - so right shit bit_sting 0 bit
    and then AND 1110010 and 11 (now bits=10)
```
elif bits == 0b10:
      gene += "G"
```
  - now gene has "G"

> 2nd Round
```
bits: int = self.bit_string >> i & 0b11
```
  - i=2
  - so right shit bit_sting 2 bits
    and then AND 001110010 and 11 (now bits=00)
```
elif bits == 0b00:
      gene += "A"
```
  - now gene has "GA"

> 3rd Round
```
bits: int = self.bit_string >> i & 0b11
```
  - i=4
  - so right shit bit_sting 4 bits
    and then AND 0000111 and 11 (now bits=11)
```
if bits == 0b11:
      gene += "T"
```
  - now gene has "GAT"

  - return gene[::-1] ***will return the result in reverse like TAG***










