import asyncio
import time


async def fetch_data():
    """
    Mimicks the data fetch delay and returns a hard typed data
    """
    print('start fetching')
    data = '{"data":1}'
    await asyncio.sleep(4)
    print('done fetching')
    return data

async def main():
    """
    Async main function
    """
    start_time = time.time()
    task=asyncio.create_task(fetch_data())
    value = await task
    print(value)
    print(f"--- It took {(time.time() - start_time):.2f} seconds to complete---")

if __name__=='__main__':
    asyncio.run(main())