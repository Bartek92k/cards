import random

lista = []
players = 10
n_cards = 5

def deck():
	kolory = ['c','d','h','s']
	liczba = ['2','3','4','5','6','7','8','9','10','J','D','K','A']
	
	for i in liczba:
		for n in kolory:
			karta =(i , n)
			lista.append(karta)
			
	return lista


def shuffle_deck(lista):
	n_cards = len(lista)
	for i in range(n_cards):
		
		zmienna = random.randint(0, n_cards-1)
		karta_pom = lista[i]
		lista[i] = lista[zmienna]
		lista[zmienna] = karta_pom
	return lista	

def deal(lista, players, n_cards):

        print("Karty rozdane do gry dla %s graczy po %s sztuk: " % (players, n_cards))
        gracz = []
        random.shuffle(lista)
        for o in range(players):
            gracz=[lista.pop() for m in range(n_cards)]
            print("gracz %s = %s" %(o+1,gracz))

    
deck()
shuffle_deck(lista)
deal(lista, players, n_cards)

