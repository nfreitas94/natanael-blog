import threading

counter = 0

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()

print(counter)  # Esperado: 2.000.000. Resultado real: algo menor.