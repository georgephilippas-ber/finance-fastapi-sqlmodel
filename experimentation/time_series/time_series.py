import asyncio

from client.eodhd.eodhd_client import EODHDClient

if __name__ == '__main__':
    async def async_main():
        eodhd_client = EODHDClient()

        print(await eodhd_client.fundamentals("MSFT", "US"))


    asyncio.run(async_main())
