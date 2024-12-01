#3
import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik, lozinka):
    print(f"Autorizacija korisnika {korisnik['korisnicko_ime']} započeta...")
    await asyncio.sleep(2) 
    korisnik_lozinka = next(
        (item for item in baza_lozinka if item['korisnicko_ime'] == korisnik['korisnicko_ime']), None
    )
    if korisnik_lozinka and korisnik_lozinka['lozinka'] == lozinka:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."

async def autentifikacija(unos_korisnika):
    print(f"Autentifikacija korisnika {unos_korisnika['korisnicko_ime']} započeta...")
    await asyncio.sleep(3) 
    korisnik = next(
        (item for item in baza_korisnika if item['korisnicko_ime'] == unos_korisnika['korisnicko_ime'] and item['email'] == unos_korisnika['email']), None
    )
    if not korisnik:
        return f"Korisnik {unos_korisnika['korisnicko_ime']} nije pronađen."
    else:
        rezultat_autorizacije = await autorizacija(korisnik, unos_korisnika['lozinka'])
        return rezultat_autorizacije

async def main():
    unos_korisnika = {
        'korisnicko_ime': 'ana_anic',
        'email': 'aanic@gmail.com',
        'lozinka': 'super_teska_lozinka'
    }
    rezultat = await autentifikacija(unos_korisnika)
    print(rezultat)

asyncio.run(main())



