#1
kvadriraj = lambda x: x ** 2
print(kvadriraj(5))
#2
zbroji_kvadriraj = lambda a, b: (a + b) ** 2
print(zbroji_kvadriraj(5, 6))
#3
kvadriraj_duljinu = lambda niz: len(niz) ** 2
print(kvadriraj_duljinu("Marta"))
#4
pomnozi_potenciraj = lambda x, y: (y * 5) ** x
print(pomnozi_potenciraj(3, 6))
#5
paran_broj = lambda x: True if x % 2 == 0 else None
print(paran_broj(8))

input("Pritisnite Enter za izlaz...")


