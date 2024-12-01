#2
import asyncio

async def dohvat_korisnika():
    print("Dohvaćam podatke o korisnicima...")
    await asyncio.sleep(3)  
    korisnici = [
        {"id": 1, "ime": "Ivan", "prezime": "Ivić"},
        {"id": 2, "ime": "Pero", "prezime": "Perić"},
        {"id": 3, "ime": "Marko", "prezime": "Marković"},
    ]
    print("Podaci o korisnicima dohvaćeni.")
    return korisnici

async def dohvat_proizvoda():
    print("Dohvaćam podatke o proizvodima...")
    await asyncio.sleep(5)  
    proizvodi = [
        {"id": 101, "naziv": "Laptop", "cijena": 8000},
        {"id": 102, "naziv": "Mobitel", "cijena": 5000},
        {"id": 103, "naziv": "Monitor", "cijena": 1500},
    ]
    print("Podaci o proizvodima dohvaćeni.")
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(
        dohvat_korisnika(), 
        dohvat_proizvoda()
    )
    print(f"Dohvaćeni korisnici: {korisnici}")
    print(f"Dohvaćeni proizvodi: {proizvodi}")

asyncio.run(main())


