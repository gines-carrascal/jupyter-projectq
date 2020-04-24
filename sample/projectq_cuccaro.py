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
c = eng.allocate_qureg(1)

for i in range(n):
    if sumando_1[i] == "1":
        NOT | (a[n - (i+1)])
for i in range(n):
    if sumando_2[i] == "1":
        NOT | (b[n - (i+1)])

for i in range(1, n):
    CNOT | (a[i], b[i])

CNOT | (a[1], c[0])

Toffoli | (a[0], b[0], c[0])
CNOT | (a[2], a[1])

Toffoli | (c[0], b[1], a[1])
CNOT | a[3], a[2])

for i in range(2, n-2):
    qToffoli | (a[i-1], b[i], a[i])
    CNOT | (a[i+2], a[i+1])

Toffoli | (a[n-3], b[n-2], a[n-2])
CNOT | (a[n-1], b[n])

Toffoli | (a[n-2], b[n-1], b[n])
for i in range(1, n-1):
    NOT | (b[i])

CNOT | (c[0], b[1])
for i in range(2, n):
    CNOT | (a[i-1], b[i])

Toffoli | (a[n-3], b[n-2], a[n-2])

for i in range(n-3,1,-1):
    qc.ccx(a[i-1], b[i], a[i])
    CNOT | (a[i+2], a[i+1])
    NOT | (b[i+1])

Toffoli | (c[0], b[1], a[1])
CNOT | (a[3], a[2])
NOT | (b[2])

Toffoli | (a[0], b[0], c[0])
CNOT | (a[2], a[1])
NOT | (b[1])

CNOT | (a[1], c[0])

for i in range(n):
    CNOT | (a[i], b[i])

All(Measure) | b

eng.flush()

result = []
for i in range(n):
    result.append(int(b[i]))

print(result)
    