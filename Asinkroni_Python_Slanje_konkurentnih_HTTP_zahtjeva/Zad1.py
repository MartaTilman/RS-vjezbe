#1
import asyncio
import aiohttp
import time

async def fetch_users(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    url = "https://jsonplaceholder.typicode.com/users"
    broj_zahtjeva = 5

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        zadaci = [fetch_users(session, url) for _ in range(broj_zahtjeva)]
        rezultati = await asyncio.gather(*zadaci)

    korisnici = rezultati[0]

    imena = [korisnik['name'] for korisnik in korisnici]
    emailovi = [korisnik['email'] for korisnik in korisnici]
    usernameovi = [korisnik['username'] for korisnik in korisnici]

    end_time = time.time()
    trajanje = end_time - start_time

    print("Imena korisnika:", imena)
    print("Email adrese korisnika:", emailovi)
    print("Username korisnika:", usernameovi)
    print(f"Vrijeme izvođenja programa: {trajanje:.2f} sekundi")

asyncio.run(main())






