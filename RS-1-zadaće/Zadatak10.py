def brojanje_riječi(tekst):
  
  riječi = tekst.split()
  rječnik = {}

  for riječ in riječi:
      riječ = riječ.strip('.,!?"')
      riječ = riječ.lower()
      if riječ in rječnik:
          rječnik[riječ] += 1
      else:
          rječnik[riječ] = 1

  return rječnik

tekst = "Dobro jutro. Kako ste? Pijete li još istu toplu čokoladu? Ja sam dobro, ali ja ne volim toplu čokoladu."
print(brojanje_riječi(tekst))


input("Pritisnite Enter za izlaz...")
