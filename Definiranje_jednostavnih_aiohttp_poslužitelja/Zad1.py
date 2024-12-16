from aiohttp import web
import json

products = [
    {"naziv": "Jabuka", "cijena": 1.2, "kolicina": 50},
    {"naziv": "Kruh", "cijena": 1.5, "kolicina": 30},
    {"naziv": "Mlijeko", "cijena": 0.99, "kolicina": 20},
    {"naziv": "Sir", "cijena": 5.5, "kolicina": 10},
]

async def get_products(request):
    return web.json_response(products)

async def add_product(request):
    try:
        data = await request.json()

        if not all(key in data for key in ["naziv", "cijena", "kolicina"]):
            return web.json_response(
                {"error": "Nedostaju ključevi: naziv, cijena, kolicina"}, status=400
            )

        products.append(data)

        print(f"Novi proizvod: {json.dumps(data, ensure_ascii=False, indent=4)}")

        return web.json_response(products)

    except json.JSONDecodeError:
        return web.json_response(
            {"error": "Neispravan JSON format"}, status=400
        )
app = web.Application()
app.router.add_get("/proizvodi", get_products)
app.router.add_post("/proizvodi", add_product)

if __name__ == "__main__":
    web.run_app(app, port=8081)
