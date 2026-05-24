# Execute com: python3.13 async_vs_threads.py
import asyncio
import threading
import time

def thread_io_work(seconds):
    time.sleep(seconds)

async def async_io_work(seconds):
    await asyncio.sleep(seconds)

for n in [100, 1000, 5000]:
    # threads
    start = time.perf_counter()
    threads = [threading.Thread(target=thread_io_work, args=(0.5,)) for _ in range(n)]
    for t in threads: t.start()
    for t in threads: t.join()
    thread_time = time.perf_counter() - start

    # asyncio
    async def run_async(count):
        tasks = [async_io_work(0.5) for _ in range(count)]
        await asyncio.gather(*tasks)

    start = time.perf_counter()
    asyncio.run(run_async(n))
    async_time = time.perf_counter() - start

    print(f"{n:>5} threads: {thread_time:.2f}s | asyncio: {async_time:.2f}s")