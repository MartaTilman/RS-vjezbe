from aiohttp import web

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def get_adults(request):
    adults = [user for user in korisnici if user['godine'] > 18]
    return web.json_response(adults)


app = web.Application()
app.router.add_get("/punoljetni", get_adults)

if __name__ == "__main__":
    web.run_app(app, port=8082)
