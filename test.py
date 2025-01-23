
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


for i in range(len(wrd)):
	x = alph.index(wrd[i])
	y = alph.index(stream[i])
	add = x + y
	if add> len(alph)-1:
		add = add-len(alph)
			
	done.append(alph[add])

print(done)
			
	
