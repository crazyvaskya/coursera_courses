from abc import ABC, abstractmethod


class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    @abstractmethod
    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects().copy()

    @abstractmethod
    def get_stats(self):
        pass


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects().copy()

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append("Blessing")
        return positive_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Perception"] += 2
        stats["Endurance"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        return stats.copy()


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append("Berserk")
        return positive_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 7
        stats["Perception"] -= 3
        stats["Endurance"] += 7
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["HP"] += 50
        return stats.copy()


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append("Weakness")
        return negative_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats.copy()


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append("EvilEye")
        effect_applied = True
        return negative_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats.copy()


class Curse(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append("Curse")
        return negative_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Perception"] -= 2
        stats["Endurance"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        return stats.copy()
