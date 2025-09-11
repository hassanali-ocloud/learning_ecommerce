import asyncio
from urllib.request import urlopen

async def read_file(url: str):
    try:
        with urlopen(url=url) as response:
            body = response.read().decode('utf-8')
            return body
    except Exception as e:
        print(f"Error fetching the file: {e.reason}")

async def main():
    url = "https://raw.githubusercontent.com/khuzaima-ocs/railway-incidents/refs/heads/main/rail_incidents.csv"
    data = await read_file(url=url)
    print(data)
if __name__ == "__main__":
    asyncio.run(main())
