#1
import asyncio

async def dohvat_podataka():
    print("Dohvacam podatke...")
    await asyncio.sleep(3)
    podaci = [x for x in range(1, 11)]
    print("Podaci dohvaceni.")
    return podaci

async def main():
    podaci = await dohvat_podataka()
    print(f"Dohvaceni podaci: {podaci}")

asyncio.run(main())

