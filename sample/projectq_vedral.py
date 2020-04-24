from projectq import MainEngine  # import the main compiler engine
from projectq.ops import All, CNOT, NOT, H, Toffoli, Measure  # import the operations we want to perform 
from projectq.backends import CircuitDrawer

sumando_1 = input("Primer sumando en binario (4 bits)")
sumando_2 = input("Segundo sumando en binario(4 bits)")

n = 4

backend = CircuitDrawer()
#ResourceCounter()
eng = MainEngine(backend)
#eng = MainEngine()

a = eng.allocate_qureg(n)
b = eng.allocate_qureg(n+1)
c = eng.allocate_qureg(n)

for i in range(n):
    if sumando_1[i] == "1":
        NOT | (a[n - (i+1)])
for i in range(n):
    if sumando_2[i] == "1":
        NOT | (b[n - (i+1)])
        
for i in range(n-1):
    Toffoli | (a[i], b[i], c[i+1])
    CNOT | (a[i], b[i])
    Toffoli | (a[i], b[i], c[i+1])

Toffoli | (a[n-1], b[n-1], b[n])
CNOT | (a[n-1], b[n-1])
Toffoli | (a[n-1], b[n-1], b[n])  

CNOT | (c[n-1], b[n-1])

for i in range(n-1):
    Toffoli | (c[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
    CNOT | (a[(n-2)-i], b[(n-2)-i])
    Toffoli | (a[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
    
    CNOT | (c[(n-2)-i], b[(n-2)-i])
    CNOT | (a[(n-2)-i], b[(n-2)-i])

All(Measure) | b

eng.flush()

result = []
for i in range(n):
    result.append(int(b[i]))


print(result)

    
    