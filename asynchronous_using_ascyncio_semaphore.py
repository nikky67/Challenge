import time
import aiohttp
import asyncio


# Asynchronous solution using ascyncio and adding asyncio.Semaphore() with maximum tasks of 1000
start_time = int(time.time())


async def calling_endpoint(session, url):
    async with session.get(url) as response:
        print(response)


async def sem_fetch(sem, session, url):
    async with sem:
        await calling_endpoint(session, url)


async def run(r):
    url = "https://q0zjgslzg5.execute-api.us-west-2.amazonaws.com/prod/"
    tasks = []
    sem = asyncio.Semaphore(1000)

    async with aiohttp.ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(sem_fetch(sem, session, url))
            tasks.append(task)

        asyncio.gather(*tasks)
        responses = asyncio.gather(*tasks)
        await responses


max_calls = 200000
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(max_calls))
loop.run_until_complete(future)
print("--- %s seconds ---" % (time.time() - start_time))
