from src.model.creature import Creature


class Population:
    def __init__(self, game_config):
        self.size = game_config.population_size
        self.creatures = []
        self.generate_creatures()

    def generate_creatures(self):
        for i in range(self.size):
            self.creatures.append(Creature(i))
