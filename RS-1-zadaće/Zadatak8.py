#drugiZad
def parni_brojevi(lista):
  nova_lista = [broj for broj in lista if broj % 2 == 0]
  return nova_lista


originalna_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parni = parni_brojevi(originalna_lista)
print(parni)  
input("Pritisnite Enter za izlaz...")
