
# **Debugging Compression & Decompression**
## **Compression**

* Input String = "TAGG"

* intialize bit_string value :1;
bit_string = 1

* after shift two places to left ,add the value to bit string , bit_string (OR - logical operator ) with first word of input string , repeat again till the end of input string.

    << =2 ( left shift ): 100

	100 (or) 11 ( T) => 111

    bit_string = 111
    
    <<=2	: 11100

    11100 (or)	00 (A) => 11100
	
    bit_string = 11100

    <<=2	: 1110000

	1110000 (or) 10 (G) => 1110010
	
    bit_string = 1110010

    <<=2 	: 111001000

	111001000 (or) 10 (G) => 111001010

    result bit_string = 111001010
********************************
## **Decompression**

> * shift to right by the looping on the constant bit_string.
> * use logical operator AND 

    for ( 0, 8 =>length of bit_string, 2) , i & 0b11

    i=0
    bit_string = 111001010	
    >> 111001010 & 000000011 = 000000010 (G)
	
    i=2
    bit_string = 111001010
    >> 001110010 & 000000011 = 000000010 (G) 

    i=4
    bit_string = 111001010
    >> 000011100 & 000000011 = 000000000 (A)

    i=6
    bit_string = 111001010
    >> 000000111 & 000000011 = 000000011 (T)
	
    output string = "GGAT"
    retrun gene[::-1] => mean the reverse
    output string = "TAGG"
