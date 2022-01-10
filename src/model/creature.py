import uuid

from src.algorithm.initializers.creature_properties_initializer import CreaturePropertiesInitializer
from src.algorithm.initializers.neural_network_initializer import NeuralNetworkInitializer


class Creature:
    def __init__(self, algorithm_config):
        self.id = uuid.uuid4()
        self.hp = algorithm_config.creature_max_hp
        self.neural_network = NeuralNetworkInitializer.initialize(algorithm_config)
        self.properties = CreaturePropertiesInitializer.initialize(algorithm_config)

    def tick(self, game_state):
        # TODO: implement
        pass

    def mutate(self):
        # TOOD: implement
        pass
