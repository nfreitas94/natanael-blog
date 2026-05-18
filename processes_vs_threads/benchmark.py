# Execute com: PYTHON_GIL=0 python3.13t benchmark.py
import sys
import threading
import multiprocessing
import time
import os

print(f"GIL ativo: {sys._is_gil_enabled()}")  # False

def cpu_work(n):
    """Simula trabalho que usa CPU."""
    total = 0
    for i in range(n):
        total += i * i
    return total

N = 10_000_000

# Sequencial
start = time.perf_counter()
cpu_work(N)
cpu_work(N)
seq_time = time.perf_counter() - start

# 2 threads
start = time.perf_counter()
t1 = threading.Thread(target=cpu_work, args=(N,))
t2 = threading.Thread(target=cpu_work, args=(N,))
t1.start(); t2.start()
t1.join(); t2.join()
thread_time = time.perf_counter() - start

# 2 processos
start = time.perf_counter()
p1 = multiprocessing.Process(target=cpu_work, args=(N,))
p2 = multiprocessing.Process(target=cpu_work, args=(N,))
p1.start(); p2.start()
p1.join(); p2.join()
process_time = time.perf_counter() - start

print(f"Sequencial:  {seq_time:.2f}s")
print(f"2 threads:   {thread_time:.2f}s")
print(f"2 processos: {process_time:.2f}s")
print(f"Cores:       {os.cpu_count()}")

# 64 processos na mesma máquina de 8 cores
start = time.perf_counter()
processes = []
for _ in range(64):
    p = multiprocessing.Process(target=cpu_work, args=(N,))
    processes.append(p)
    p.start()
for p in processes:
    p.join()
many_process_time = time.perf_counter() - start

print(f"64 processos: {many_process_time:.2f}s")
print(f"Tempo ideal se não houvesse overhead: {seq_time * 32 / os.cpu_count():.2f}s")