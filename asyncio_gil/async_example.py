# Execute com: python3.13 async_example.py
import asyncio
import time

async def io_work(task_id, seconds):
    """Simula trabalho de I/O."""
    print(f"Tarefa {task_id}: iniciando")
    await asyncio.sleep(seconds)
    print(f"Tarefa {task_id}: concluída")

async def main():
    start = time.perf_counter()

    tasks = [io_work(i, 1) for i in range(5)]
    await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start
    print(f"Tempo total: {elapsed:.2f}s")

asyncio.run(main())