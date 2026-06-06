# 1. Stack: recursion error
print("=== RecursionError ===")
def recursion_infinita():
    return recursion_infinita()

try:
    recursion_infinita()
except RecursionError as e:
    print(f"RecursionError: {e}")

print()

# 2. Refcount
print("=== Reference Counting ===")
import sys

a = [1, 2, 3]
print(f"refcount após criar 'a':   {sys.getrefcount(a)}")

b = a
print(f"refcount após 'b = a':     {sys.getrefcount(a)}")

del b
print(f"refcount após 'del b':     {sys.getrefcount(a)}")

print()

# 3. Memory leak com tracemalloc
print("=== Memory Leak (tracemalloc) ===")
import tracemalloc

tracemalloc.start()

cache = {}

def processa_request(request_id):
    resultado = {"id": request_id, "dados": "x" * 10000}
    cache[request_id] = resultado

for i in range(10000):
    processa_request(i)

snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics("lineno")

print(f"Itens no cache: {len(cache)}")
for stat in stats[:3]:
    print(stat)

tracemalloc.stop()

print()

# 4. Detectando leak com snapshots
print("=== Detectando Leak (compare snapshots) ===")
tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

dados = []
for i in range(100000):
    dados.append({"index": i, "payload": "x" * 1000})

snapshot2 = tracemalloc.take_snapshot()

stats = snapshot2.compare_to(snapshot1, "lineno")

print("Top 3 diferenças de alocação:")
for stat in stats[:3]:
    print(stat)

tracemalloc.stop()