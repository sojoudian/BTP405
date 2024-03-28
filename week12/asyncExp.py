import time
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(3)
    print("Data fetched!")

async def compute_sum(n):
    print(f'Computing sum up to {n}')
    total = sum(range(1, n+1))
    await asyncio.sleep(1)
    print(f'Sum: {total}')


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(compute_sum(20))

    await task1
    await task2

asyncio.run(main())