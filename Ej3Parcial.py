class Cola():
    def __init__(self):
        self.elementos = []

    def init(self):
        self.elementos = []

    def arrive(self, value):
        self.elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.elementos.pop(0)

    def size(self):
        return len(self.elementos)

    def on_front(self):
        if self.size() > 0:
            return self.elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux


class Pila():
    def __init__(self):
        self.elementos = []

    def init(self):
        self.elementos = []

    def eq(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.elementos == stack_aux.elementos
        else:
            return False

    def push(self, value):
        self.elementos.append(value)

    def pop(self):
        if self.size() > 0:
            dato = self.elementos.pop()
            return dato

    def size(self):
        return len(self.elementos)

    def on_top(self):
        if self.size() > 0:
            return self.elementos[-1]


bitacora = Pila()

bitacora.push(("Tatooine", "Luke", 100))
bitacora.push(("Coruscant", "Vader", 200))
bitacora.push(("Endor", "Yoda", 150))
bitacora.push(("Kamino", "Obi-Wan", 180))
bitacora.push(("Hoth", "Han Solo", 300))

planetas = Cola()
creditos_totales = 0

while bitacora.size() > 0:
    mision = bitacora.pop()
    planetas.arrive(mision[0])
    creditos_totales += mision[2]

print("Créditos galácticos totales:", creditos_totales)

mision_han_solo = None
num_mision = 1
bitacora_temp = Pila()

while bitacora.size() > 0:
    mision = bitacora.pop()
    bitacora_temp.push(mision)
    if mision[1] == "Han Solo":
        mision_han_solo = (num_mision, mision[0])
    num_mision += 1

while bitacora_temp.size() > 0:
    mision = bitacora_temp.pop()
    bitacora.push(mision)

if mision_han_solo:
    print("Han Solo fue capturado en la misión número:", mision_han_solo[0])
    print("Planeta de la captura de Han Solo:", mision_han_solo[1])
else:
    print("Han Solo no fue capturado en ninguna misión.")

print("Planetas visitados en orden de las misiones:")
while planetas.size() > 0:
    print(planetas.atention())

