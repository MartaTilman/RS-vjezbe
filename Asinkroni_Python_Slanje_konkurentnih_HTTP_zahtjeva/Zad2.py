#2
import asyncio
import aiohttp
import re

async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('fact', "Fact not found.")
            else:
                return f"Error: {response.status}"
    except aiohttp.ClientError as e:
        return f"HTTP error: {e}"
    except asyncio.TimeoutError:
        return "Request timed out."

async def filter_cat_facts(facts):
    pattern = re.compile(r'\bcat\b|\bcats\b', re.IGNORECASE)
    return [fact for fact in facts if pattern.search(fact)]

async def main():
    broj_zahtjeva = 20

    async with aiohttp.ClientSession() as session:
        zadaci = [get_cat_fact(session) for _ in range(broj_zahtjeva)]
        sve_cinjenice = await asyncio.gather(*zadaci)

    filtrirane_cinjenice = await filter_cat_facts(sve_cinjenice)

    print("Filtrirane činjenice o mačkama:")
    for fact in filtrirane_cinjenice:
        print(f"- {fact}")

asyncio.run(main())







