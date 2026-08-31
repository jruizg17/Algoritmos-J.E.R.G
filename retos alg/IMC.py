class persona:
    def __init__(self):
        self.doc_tipo = ""
        self.doc = ""
        self.nombre = ""
        self.apellido = ""
        self.peso = 0.0
        self.estatura = 0.0
        self.edad = 0
        self.sexo = ""

    def pedirdatos(self):
        self.doc_tipo, self.doc, self.nombre, self.apellido = input("tipo, doc, nombre, apellido: ").split()
        self.peso = float(input("peso: "))
        self.estatura = float(input("estatura: "))
        self.edad = int(input("edad: "))
        self.sexo = input("sexo: ")

    def mostrarpersona(self):
        print(f"{self.nombre} {self.apellido} - {self.doc_tipo}: {self.doc}")

    def calcularimc(self):
        imc = self.peso / (self.estatura ** 2)
        if imc < 20: return "pesobajo"
        elif imc <= 25: return "pesoideal"
        else: return "sobrepeso"

    def mayoredad(self):
        return self.edad >= 18


class empleado(persona):
    def __init__(self):
        super().__init__()
        self.cargo = ""
        self.valorhora = 0.0
        self.horastrabajadas = 0.0
        self.departamento = ""

    def calcularhonorarios(self):
        self.pedirdatos()
        self.cargo = input("cargo: ")
        self.valorhora = float(input("valor hora: "))
        self.horastrabajadas = float(input("horas trabajadas: "))
        self.departamento = input("depto: ")

        total = self.valorhora * self.horastrabajadas
        pago = total - (total * 0.00966)

        print(f"\ndoc: {self.doc_tipo} {self.doc}")
        print(f"nombre: {self.nombre} {self.apellido}")
        print(f"cargo: {self.cargo} | horas: {self.horastrabajadas} | valor hr: {self.valorhora}")
        print(f"pago total: {pago}")


# inicio
e = empleado()
e.calcularhonorarios()

imc = e.calcularimc()
if imc == "pesobajo": print("el peso esta por debajo del ideal")
elif imc == "pesoideal": print("el peso es ideal")
else: print("tiene sobrepeso")