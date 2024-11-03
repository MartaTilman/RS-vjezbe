#drugiZad
def ukloni_duplikate():
  unos = input("Unesite elemente liste odvojene zarezima: ")
  
  lista = [element.strip() for element in unos.split(",")]
  pomocni_skup = set()
  nova_lista = []


  for element in lista:
      if element not in pomocni_skup:
          pomocni_skup.add(element)
          nova_lista.append(element)

  return nova_lista


rezultat = ukloni_duplikate()
print("Lista bez duplikata:", rezultat)

input("Pritisnite Enter za izlaz...")
