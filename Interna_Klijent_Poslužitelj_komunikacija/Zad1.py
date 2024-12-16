import aiohttp
from aiohttp import web
import asyncio
import json

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod(request):
    proizvod_id = int(request.match_info['id'])
    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)

    if proizvod is None:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

    return web.json_response(proizvod)

async def post_narudzba(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.json_response({'error': 'Neispravan JSON format'}, status=400)

    proizvod_id = data.get("proizvod_id")
    kolicina = data.get("kolicina")

    if proizvod_id is None or kolicina is None:
        return web.json_response({'error': 'Podaci su nepotpuni, proizvod_id i kolicina su obavezni'}, status=400)

    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    if proizvod is None:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

    narudzba = {
        "proizvod_id": proizvod_id,
        "kolicina": kolicina,
        "naziv": proizvod["naziv"],
        "cijena": proizvod["cijena"],
        "ukupna_cijena": proizvod["cijena"] * kolicina
    }
    narudzbe.append(narudzba)

    return web.json_response(narudzbe, status=201)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod)
app.router.add_post('/narudzbe', post_narudzba)

async def test_server():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8081/proizvodi') as response:
            print(f"GET /proizvodi - Status: {response.status}")
            proizvodi_json = await response.json()
            print(proizvodi_json)

        async with session.get('http://localhost:8081/proizvodi/2') as response:
            print(f"GET /proizvodi/2 - Status: {response.status}")
            proizvod_json = await response.json()
            print(proizvod_json)

        new_order = {
            "proizvod_id": 1,
            "kolicina": 2
        }
        async with session.post('http://localhost:8081/narudzbe', json=new_order) as response:
            print(f"POST /narudzbe - Status: {response.status}")
            narudzbe_json = await response.json()
            print(narudzbe_json)

        invalid_order = {
            "proizvod_id": 99,
            "kolicina": 1
        }
        async with session.post('http://localhost:8081/narudzbe', json=invalid_order) as response:
            print(f"POST /narudzbe (invalid) - Status: {response.status}")
            error_json = await response.json()
            print(error_json)

async def main():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()

    print("Poslužitelj je pokrenut na http://localhost:8081")

    await test_server()

    while True:
        await asyncio.sleep(3600)  

if __name__ == "__main__":
    asyncio.run(main())
