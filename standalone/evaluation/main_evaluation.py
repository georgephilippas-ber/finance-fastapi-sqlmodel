import asyncio

from adapter.restcountries.restcountries_adapter import RESTCountriesAdapter
from client.restcountries.restcountries_client import RESTCountriesClient

if __name__ == '__main__':
    async def ex():
        f = await RESTCountriesClient().get_all()
        g = RESTCountriesAdapter().adapt_many(f)
        for s in g:
            print(s[0].location)


    asyncio.run(ex())
