characters = []

for character in range(0, 1114111):
	characters.append(chr(character))

f = open('unicode.txt','w',encoding="utf-8")
f.write(str(characters))
f.close()