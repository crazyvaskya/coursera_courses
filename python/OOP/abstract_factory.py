import random


### My code ###
class AbstractLevel:
    @classmethod
    def get_map(Class):
        return Class.Map()

    @classmethod
    def get_objects(Class):
        return Class.Objects()


class EasyLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self.map = EasyMap()

        def get_map(self):
            return self.map.get_map()

    class Objects:
        def __init__(self):
            self.objects = EasyObjects()

        def get_objects(self, map):
            return self.objects.get_objects(map)


class MediumLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self.map = MediumMap()

        def get_map(self):
            return self.map.get_map()

    class Objects:
        def __init__(self):
            self.objects = MediumObjects()

        def get_objects(self, map):
            return self.objects.get_objects(map)


class HardLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self.map = HardMap()

        def get_map(self):
            return self.map.get_map()

    class Objects:
        def __init__(self):
            self.objects = HardObjects()

        def get_objects(self, map):
            return self.objects.get_objects(map)


### Given code ###
class EasyMap:

    def __init__(self):
        self.map = [[0 for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                if i == 0 or j == 0 or i == 4 or j == 4:
                    self.map[j][i] = -1  # граница карты
                else:
                    # случайная характеристика области
                    self.map[j][i] = random.randint(0, 2)

    def get_map(self):
        return self.map


class EasyObjects:

    def __init__(self):
        # размещаем переход на след. уровень
        self.objects = [('next_lvl', (2, 2))]

    def get_objects(self, map):
        # размещаем противников
        for obj_name in ['rat']:
            coord = (random.randint(1, 3), random.randint(1, 3))
            # ищем случайную свободную локацию
            intersect = True
            while intersect:
                intersect = False
                for obj in self.objects:
                    if coord == obj[1]:
                        intersect = True
                        coord = (random.randint(1, 3), random.randint(1, 3))

            self.objects.append((obj_name, coord))

        return self.objects


class MediumMap:

    def __init__(self):
        self.map = [[0 for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if i == 0 or j == 0 or i == 7 or j == 7:
                    self.map[j][i] = -1  # граница карты
                else:
                    # случайная характеристика области
                    self.map[j][i] = random.randint(0, 2)

    def get_map(self):
        return self.map


class MediumObjects:

    def __init__(self):
        # размещаем переход на след. уровень
        self.objects = [('next_lvl', (4, 4))]

    def get_objects(self, map):
        # размещаем врагов
        for obj_name in ['rat', 'snake']:
            coord = (random.randint(1, 6), random.randint(1, 6))
            # ищем случайную свободную локацию
            intersect = True
            while intersect:
                intersect = False
                for obj in self.objects:
                    if coord == obj[1]:
                        intersect = True
                        coord = (random.randint(1, 6), random.randint(1, 6))

            self.objects.append((obj_name, coord))

        return self.objects


class HardMap:

    def __init__(self):
        self.map = [[0 for j in range(10)] for i in range(10)]
        for i in range(10):
            for j in range(10):
                if i == 0 or j == 0 or i == 9 or j == 9:
                    # граница карты
                    self.map[j][i] = -1
                else:
                    # характеристика области (-1 для непроходимой обл.)
                    self.map[j][i] = random.randint(-1, 8)

    def get_map(self):
        return self.map


class HardObjects:

    def __init__(self):
        # размещаем переход на след. уровень
        self.objects = [('next_lvl', (5, 5))]

    def get_objects(self, map):
        # размещаем врагов
        for obj_name in ['rat', 'snake']:
            coord = (random.randint(1, 8), random.randint(1, 8))
            # ищем случайную свободную локацию
            intersect = True
            while intersect:
                intersect = False
                if map[coord[0]][coord[1]] == -1:
                    intersect = True
                    coord = (random.randint(1, 8), random.randint(1, 8))
                    continue
                for obj in self.objects:
                    if coord == obj[1]:
                        intersect = True
                        coord = (random.randint(1, 8), random.randint(1, 8))

            self.objects.append((obj_name, coord))

        return self.objects
### End of given code ###


def create_map (factory):
    mapa = factory.get_map()
    objects = factory.get_objects()
    return mapa, objects


if __name__ == "__main__":
    mapa, objects = create_map(EasyLevel())
    print (type(mapa), type(objects))
    mapa, objects = create_map(MediumLevel())
    print (type(mapa), type(objects))
    mapa, objects = create_map(HardLevel())
    print (type(mapa), type(objects))
    print (EasyLevel().get_objects().get_objects())
