class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self._vida = vida
        self.daño = daño

    def recibir_daño(self, cantidad):
        self._vida = max(self._vida - cantidad, 0)
        if self._vida == 0:
            print(f"{self.nombre} Ha muerto")
        else:
            print(f"{self.nombre} Ahora tiene {self._vida} de vida, recibio {self.daño} de daño")

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre} causando {self.daño}")
        enemigo.recibir_daño(self.daño)

    def mostrar_estado(self):
        print(f"{self.nombre} - Vida: {self._vida} | Daño: {self.daño}")


class Espadachin(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=120, daño=20)

    def GolpeDobleEspada(self, enemigo):
        doblegolpe = self.daño * 2
        print(f"{self.nombre} Le ha dado golpe doble causando doble de daño {doblegolpe} de daño causado")
        enemigo.recibir_daño(doblegolpe)

class Asesino(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, daño=40)

    def ataque_sorpresa(self, enemigo):
        critico = self.daño * 3
        print(f"{self.nombre} pego un epico critico {critico} de daño")
        enemigo.recibir_daño(critico)

guts = Espadachin("Guts")
nox = Asesino("Nox")
boss = Personaje("Boss", 300, 50)



nox.atacar(guts)
nox.mostrar_estado()
guts.GolpeDobleEspada(nox)
nox.mostrar_estado()