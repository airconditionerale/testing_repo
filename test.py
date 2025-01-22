
alph=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
wrd= input("gimme a word (all CAPS)")
key= input("gimme the key") 

stream = []
done = []
j = 0

for i in range(len(wrd)):
	if(i>=len(key)):
		stream.append(key[i-len(key)])
	else:
		stream.append(key[i])

print(stream)

