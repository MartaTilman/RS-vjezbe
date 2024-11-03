def razdvoji_parne_i_neparne(lista_brojeva):
  rječnik = {
      'parni': [],
      'neparni': []
  }

  for broj in lista_brojeva:
      if broj % 2 == 0:
          rječnik['parni'].append(broj)
      else:
          rječnik['neparni'].append(broj)

  return rječnik

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rezultat = razdvoji_parne_i_neparne(lista)
print(rezultat)



input("Pritisnite Enter za izlaz...")
