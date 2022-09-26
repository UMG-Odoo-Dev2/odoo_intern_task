s = 'foo.'
print(s * -8)

print(ord('a'))
print(ord('#'))

print(chr(252))

print(str(3+4j))

sst= 'football'
print(sst[2:len(sst)])

you = "Are you hiding from the truth?"
print("Original String : {}".format(you)) # content
print(id(you)) # return memory address of you
print(type(you))

replace = you.replace("hiding", "finding").replace("truth","trash").replace("from","something").replace("the","from")
print("Replace String : {}".format(replace))
print(id(replace))
print(type(replace))



