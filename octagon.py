import math

class Octagon:
    
    def __init__(self, side, angle=None, konstant=None):
        self.side = side
        self.angle = 135
        self.konstant = 1 + pow(2, 0.5)

    def endo_circle_R_and_S(self):
        endo_R = (self.side / 2) * self.konstant
        print(f"Радиус вписанной окружности равен {endo_R} ед")
        print(f"Площадь вписанной окружности равна {endo_R * endo_R * math.pi} ед")
        
    def exo_circle_R_and_S(self):
        exo_R = pow(self.konstant / (self.konstant - 1), 0.5) * self.side
        print(f"Радиус описанной окружности равен {exo_R} ед")
        print(f"Площадь описанной окружности равна {exo_R * exo_R * math.pi} ед")
            
    def octagon_S_and_P(self):
        print(f"Площадь восьмиугольника равна {2 * self.side * self.side * self.konstant} кв.ед")
        print(f"Периметр восьмиугольника равен {8 * self.side} ед")
    
    def __del__(self):
        print("ОбЪект уничтожен")