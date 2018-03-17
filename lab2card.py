lista = []

def deck():
	kolory = ['c','d','h','s']
	liczba = ['2','3','4','5','6','7','8','9','10','J','D','K','A']
	
	for i in liczba:
		for n in kolory:
			karta =(i , n)
			lista.append(karta)
			
	return lista


def shuffle_deck(lista):
	import random
	n_cards = len(lista)
	for i in range(n_cards):
		
		zmienna = random.randint(0, n_cards-1)
		karta_pom = lista[i]
		lista[i] = lista[zmienna]
		lista[zmienna] = karta_pom
	return lista	

def deal(lista):


    
deck()
shuffle_deck(lista)
print(lista)
