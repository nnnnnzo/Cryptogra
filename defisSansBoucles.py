def recIntDesc(n):
    if n != 0:
        print(n)
        recIntDesc(n-1)

recIntDesc(10)

def recIntAsc(c,n):
    if c <= n:
        print(c)
        recIntAsc(c+1,n)

print("------------------")
recIntAsc(0,10)

def recSum(n):
    if n != 0:
        return n + recSum(n-1)
    else:
        return 0

print("------------------")
print(recSum(10))

def recConcat(c, tab):
    string = ""
    c += 1
    if c <= len(tab):
        string += tab[c-1]
        return string + recConcat(c, tab)

    else:
        return string

print("------------------")
print(recConcat(0,['je','mange','des','bananes']))

def recPos(tab, mot):
    if len(tab) != 0:
        if tab[0] == mot:
            return 0
        else:
            return 1 + recPos(tab[1:], mot)

    else:
        return "pas trouvé"


print("------------------")
print(recPos(['je','mange','des','bananes'], 'des'))

print("------------------")

from random import *



class Tree:
	def __init__(self, value, children=[]):
		self.value = value
		self.children = children

	def count(self):
		n = 1
		for node in self.children:
			n += node.count()
		return n

	def toString(self):
		s = str(self.value)
		for node in self.children:
			s += node.toString()
		return s

	def contains(self, value):
		if self.value == value:
			return True
		else:
			for node in self.children:
				found = node.contains(value)
				if found:
					return found
			return False

	def nbLeaves(self):
		if len(self.children) == 0:
			return 1
		else:
			n = 0
			for node in self.children:
								n += node.nbLeaves()
			return n

	def generate(self):
		s = self.wordFor(self.value)
		for sub in self.children:
			s += sub.generate()
		return s
	def wordFor(self, element):
		return choice(elements[element])

subjects = [ "Ranjith","Tessa","Leo","Lorris","Pierre-Louis","Agathe",
             "Thibault","Lucie","Tristan","Cormac","Hugo","Tony","Rémy",
             "Allan","Adil","Nathael","Antonio","Dimitri","Cécile",
             "Aymeric","Samuel","Mathis","Pascal Colin", "Emmanuelle Graziano","Enzo","Aurelien", "Baptiste", "Lou", "BABAZ"]
verbs = [ "mange", "bois", "aime", "déteste", "pousse", "écrase", "prend", "adore",
		  "code", "développe","conçoit", "dérange"]
elements = {
	"TEXTE": [""],
	"PHRASE": ["\n"],
	"SUJET": subjects,
	"VERBE": verbs,
	"COMPLEMENT": subjects,
	"ESPACE": [" "],
	"PONCTUATION": [". "," ! ", "... "]
}

tree = Tree("TEXTE",
	[
		Tree("PHRASE", [
			Tree("SUJET"),Tree("ESPACE"),Tree("VERBE"),Tree("ESPACE"),Tree("COMPLEMENT"),Tree("PONCTUATION")
		]),
		Tree("PHRASE", [
			Tree("SUJET"),Tree("ESPACE"),Tree("VERBE"),Tree("ESPACE"),Tree("COMPLEMENT"),Tree("PONCTUATION")
		])
	]
)

print(tree.generate())
