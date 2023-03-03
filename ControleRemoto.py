
class Televisor:
    def __init__(self, canal, volume, canalMax, volMax, status: "Desligada"):
        self.canal = canal
        self.volume = volume
        self.canalMax = canalMax
        self.volMax = volMax
        self.status = status

    def ligar(self):
        self.status = "Ligada"
        print(self.status)

    def desligar(self):
        self.status = "Desligada"
        print(self.status)

    def canalAcima(self, canal):
        if canal <= self.canalMax:
            self.canal = canal
        else:
            self.canal = 0

    def canalAbaixo(self):
         if self.canal <= 0
            self.canal -= 1
         else:
            self.canal = self.canalMax





