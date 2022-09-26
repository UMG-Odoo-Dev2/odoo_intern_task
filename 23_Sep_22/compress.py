from re import sub

def encode(text):
 return sub(r'(.)1*', lambda m: str(len(m.group(0))) + m.group(1),text)

def decode(text):
 return sub(r'(d+)(D)', lambda m: m.group(2) * int(m.group(1)),text)

raw = 'bbbbyybbbbbb'
print(encode(raw))
print(decode(raw))

import gzip
s = b'GeeksForGeeks@12345678'
s = gzip.compress(s)
  
# using gzip.decompress(s) method
t = gzip.decompress(s)
print(t)
print(s)