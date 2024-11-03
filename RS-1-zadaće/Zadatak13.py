def prva_i_posljednja(lista):
  return (lista[0], lista[-1]) if lista else (None, None)

lista = [1, 2, 3, 4, 5]
rezultat = prva_i_posljednja(lista)
print("Funkcija prvi i posljedni:", rezultat) 

def max_min_torka(lista):
  if not lista: 
      return (None, None)

  maksimalni = minimalni = lista[0] 

  for broj in lista:
      if broj > maksimalni:
          maksimalni = broj
      if broj < minimalni:
          minimalni = broj

  return (maksimalni, minimalni)

lista = [3, 5, 1, 8, 2]
rezultat = max_min_torka(lista)
print("Funkcija najveći i najmanji u listi:",rezultat) 

def presjek(skup1, skup2):
  rezultat = set()  

  for element in skup1:
      if element in skup2:  
          rezultat.add(element)

  return rezultat

skup1 = {1, 2, 3, 4}
skup2 = {3, 4, 5, 6}
rezultat = presjek(skup1, skup2)
print("Presjek skupova:", rezultat)  


input("Pritisnite Enter za izlaz...")
