def zamijeni_ključeve_i_vrijednosti(originalni_rječnik):
  novi_rječnik = {}

  for ključ, vrijednost in originalni_rječnik.items():
      novi_rječnik[vrijednost] = ključ

  return novi_rječnik

originalni_rječnik = {'a': 1, 'b': 2, 'c': 3}
rezultat = zamijeni_ključeve_i_vrijednosti(originalni_rječnik)
print(rezultat) 



input("Pritisnite Enter za izlaz...")
