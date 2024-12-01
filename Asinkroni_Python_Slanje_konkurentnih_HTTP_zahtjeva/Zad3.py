#3
import asyncio
import aiohttp


async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    async with session.get(url) as response:
        data = await response.json()
        print("Dog API response:", data)
        return data['data'][0]['attributes']['body']


async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        print("Cat API response:", data)
        return data['fact']


async def mix_facts(dog_facts, cat_facts):
    mixed_facts = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed_facts.append(dog_fact)
        else:
            mixed_facts.append(cat_fact)
    return mixed_facts


async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]

        dog_cat_facts = await asyncio.gather(*dog_facts_tasks,
                                             *cat_facts_tasks)

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    mixed_facts = await mix_facts(dog_facts, cat_facts)

    print("\nMixane činjenice o psima i mačkama:")
    for fact in mixed_facts:
        print(f"- {fact}")


asyncio.run(main())
