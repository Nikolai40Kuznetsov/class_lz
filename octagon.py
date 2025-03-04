import math
import matplotlib.pyplot as plt

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

    def draw_shapes(self):
        endo_R = self.endo_circle_R_and_S()
        exo_R = self.exo_circle_R_and_S()
        center_x, center_y = 0, 0
        circle_exo = plt.Circle((center_x, center_y), exo_R, color='blue', fill=False, label='Описанная окружность')
        circle_endo = plt.Circle((center_x, center_y), endo_R, color='green', fill=False, label='Вписанная окружность')
        angles = [i * (360 / 8) for i in range(8)]
        x_points = [center_x + exo_R * math.cos(math.radians(angle)) for angle in angles]
        y_points = [center_y + exo_R * math.sin(math.radians(angle)) for angle in angles]        
        plt.gca().add_patch(plt.Polygon(list(zip(x_points, y_points)), closed=True, color='red', fill=False, label='Восьмиугольник'))
        plt.gca().add_patch(circle_exo)
        plt.gca().add_patch(circle_endo)
        plt.axis('scaled')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Отрисовка восьмиугольника и окружностей')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def __del__(self):
        print("Объект уничтожен")
