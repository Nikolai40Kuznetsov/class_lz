import math
import matplotlib.pyplot as plt

class Octagon:

    def __init__(self, side):
        self.side = side
        self.angle = 135
        self.konstant = 1 + math.sqrt(2)

    def endo_circle_R_and_S(self):
        endo_R = (self.side / 2) * self.konstant
        print(f"Радиус вписанной окружности равен {endo_R} ед")
        print(f"Площадь вписанной окружности равна {endo_R * endo_R * math.pi} ед")
        return endo_R
        
    def exo_circle_R_and_S(self):
        exo_R = math.sqrt(self.konstant / (self.konstant - 1)) * self.side
        print(f"Радиус описанной окружности равен {exo_R} ед")
        print(f"Площадь описанной окружности равна {exo_R * exo_R * math.pi} ед")
        return exo_R
            
    def octagon_S_and_P(self):
        print(f"Площадь восьмиугольника равна {2 * self.side * self.side * self.konstant} кв.ед")
        print(f"Периметр восьмиугольника равен {8 * self.side} ед")

    def draw_shapes(self):
        # Получаем радиусы вписанной и описанной окружностей
        endo_R = self.endo_circle_R_and_S()
        exo_R = self.exo_circle_R_and_S()
        
        # Координаты центра фигур
        center_x, center_y = 0, 0
        
        # Отрисовка описанной окружности
        circle_exo = plt.Circle((center_x, center_y), exo_R, color='blue', fill=False, label='Описанная окружность')
        
        # Отрисовка вписанной окружности
        circle_endo = plt.Circle((center_x, center_y), endo_R, color='green', fill=False, label='Вписанная окружность')
        
        # Отрисовка восьмиугольника
        angles = [i * (360 / 8) for i in range(8)]  # Углы для вершин восьмиугольника
        x_points = [center_x + exo_R * math.cos(math.radians(angle)) for angle in angles]
        y_points = [center_y + exo_R * math.sin(math.radians(angle)) for angle in angles]
        
        plt.gca().add_patch(plt.Polygon(list(zip(x_points, y_points)), closed=True, color='red', fill=False, label='Восьмиугольник'))
        
        # Настройка графика
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
