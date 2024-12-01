#5
import asyncio

async def secure_data(podaci):
    print(f"Enkripcija podataka za {podaci['prezime']} započeta...")
    await asyncio.sleep(3)
    enkriptirani_podaci = {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV']),
    }
    print(f"Enkripcija podataka za {podaci['prezime']} završena.")
    return enkriptirani_podaci

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Horvat', 'broj_kartice': '1234567812345678', 'CVV': '123'},
        {'prezime': 'Kovačić', 'broj_kartice': '8765432187654321', 'CVV': '456'},
        {'prezime': 'Marić', 'broj_kartice': '1122334455667788', 'CVV': '789'},
    ]

    zadaci = [secure_data(podaci) for podaci in osjetljivi_podaci]

    rezultati = await asyncio.gather(*zadaci)

    print("Enkriptirani podaci:")
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())





