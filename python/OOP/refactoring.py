import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vec2d({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __radd__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __rsub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __rmul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def int_pair():
        return(int(self.x), int(self.y))

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def clear(self):
        self.points = []
        self.speeds = []

    def set_points(self):
        points = self.points
        speeds = self.speeds
        for p in range(len(points)):
            points[p] = points[p] + speeds[p]
            if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
                speeds[p] = Vec2d(- speeds[p][0], speeds[p][1])
            if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
                speeds[p] = Vec2d(speeds[p][0], - speeds[p][1])

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        Polyline.draw(self.points, style, width, color)

    @staticmethod
    def draw(points, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]),
                                  int(points[p_n + 1][1])),
                                 width)
        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)


class Knot(Polyline):
    def __init__(self):
        super().__init__()
        self.knots = []
        self.steps = 35

    def increase_step(self):
        self.steps += 1
        self.knots = self.get_knot()

    def decrease_step(self):
        self.steps -= 1 if self.steps > 1 else 0
        self.knots = self.get_knot()

    def get_knot(self):
        points = self.points
        count = self.steps
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((points[i] + points[i + 1]) * 0.5)
            ptn.append(points[i + 1])
            ptn.append((points[i + 1] + points[i + 2]) * 0.5)

            res.extend(Knot.__get_points(ptn, count))
        return res

    def add_point(self, point, speed):
        super().add_point(point, speed)
        self.knots = self.get_knot()

    def draw_knots(self, style="points", width=3, color=(255, 255, 255)):
        Polyline.draw(self.knots, style, width, color)

    def clear(self):
        super().clear()
        self.knots = []
        self.steps = 35

    @staticmethod
    def __get_point(points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + \
            Knot.__get_point(points, alpha, deg - 1) * (1 - alpha)

    @staticmethod
    def __get_points(base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(Knot.__get_point(base_points, i * alpha))
        return res


def draw_help(steps):
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
                      (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    kn = Knot()
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    kn.clear()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    kn.increase_step()
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    kn.decrease_step()

            if event.type == pygame.MOUSEBUTTONDOWN:
                kn.add_point(Vec2d(event.pos[0], event.pos[1]),
                             Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        kn.draw_points()
        kn.draw_knots("line", 3, color)
        if not pause:
            kn.set_points()
        if show_help:
            draw_help(kn.steps)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
