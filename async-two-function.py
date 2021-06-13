import asyncio
import time


async def fetch_data():
    """
    mimicks the delay for fetching the data and returns a hard-coded data after 1 second
    """
    print('start fetching')
    await asyncio.sleep(1)
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    """
    prints 0-9 numbers with 1 second interval each
    """
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def main():
    """
    ASYNC main function
    """
    start_time = time.time()
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)
    await task2
    print(f"--- It took {(time.time() - start_time):.5f} seconds to complete---")

if __name__ == '__main__':
    asyncio.run(main())
