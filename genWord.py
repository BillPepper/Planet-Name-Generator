import random

arrVocals = ["a", "e", "i", "o", "u"]
arrConsonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
arrGreek = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Xi", "Omikron", "Rho", "Sigma", "Tau", "Ypsilon", "Phi", "Chi", "Psi", "Omega"]
arrSpecials = ["th","tt", "sch", "ch","aa", "mm", "nn", "oo", "pp"]
def genWord(cnt):
	
	letterType = random.randrange(0,2)
	isFirst = "true"
	
	i = 0	
	while (i < int(cnt)):
		
		if i > 0:
			isFirst = "false"
		
		if letterType == 1:
			genVocal(isFirst)
			letterType = 0
			
			coin = random.randrange(0,10)
			if coin == 7:
				genSpec()
				letterType = 1
				
		else:
			genConsonant(isFirst)
			letterType = 1

		i = i + 1
		
	print (" ", arrGreek[random.randrange(0, len(arrGreek))])

def genConsonant(upr):
	out = arrConsonants[random.randrange(0, len(arrVocals))]
	
	if upr == "true":
		print(out.upper(), end="")
		
	if upr == "false":
		print(out, end="")
	
def genVocal(upr):
	out = arrVocals[random.randrange(0, len(arrVocals))]

	if upr == "true":
		print(out.upper(), end="")
		
	if upr == "false":
		print(out, end="")	
		
def genSpec():
	print(arrSpecials[random.randrange(0, len(arrSpecials))], end="")
		
genWord(random.randrange(4,9))