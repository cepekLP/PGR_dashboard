import time
from math import sqrt, pow


class LapTimer:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.time = 0.0
        self.last_time = 0.0
        self.best_time = 0.0

        self.lap_counter = -1
        self.last_x = 0.0
        self.last_y = 0.0

    def init_position(self, x, y):
        self.last_x = x
        self.last_y = y

    def check(self, x, y):
        def dist(x1, y1, x2, y2):
            return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

        cross_x = (
            (self.x1 * self.y2 - self.y1 * self.x2) * (self.last_x - x)
            - (self.x1 - self.x2) * (self.last_x * y - self.last_y * x)
        ) / (
            (self.x1 - self.x2) * (self.last_y - y)
            - (self.y1 - self.y2) * (self.last_x - x)
        )
        cross_y = (
            (self.x1 * self.y2 - self.y1 * self.x2) * (self.last_y - y)
            - (self.y1 - self.y2) * (self.last_x * y - self.last_y * x)
        ) / (
            (self.x1 - self.x2) * (self.last_y - y)
            - (self.y1 - self.y2) * (self.last_x - x)
        )

        a1 = dist(self.x1, self.y1, cross_x, cross_y)
        b1 = dist(self.x2, self.y2, cross_x, cross_y)
        c1 = dist(self.x1, self.y1, self.x2, self.y2)

        a2 = dist(self.last_x, self.last_y, cross_x, cross_y)
        b2 = dist(x, y, cross_x, cross_y)
        c2 = dist(self.last_x, self.last_y, x, y)

        if (
            a1 + b1 <= c1 * 1.01
            and a1 + b1 >= c1 * 0.99
            and a2 + b2 <= c2 * 1.01
            and a2 + b2 >= c2 * 0.99
        ):
            self.last_time = time.time() - self.time
            self.time = time.time()
            if self.last_time < self.best_time or self.lap_counter == 0:
                self.best_time = self.last_time
            self.lap_counter += 1

        self.last_x = x
        self.last_y = y

        return (self.time, self.last_time, self.best_time, self.lap_counter)
