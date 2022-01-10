from src.model.population import Population


class GameState:
    """
    Class to represent the current state of the game.
    """

    def __init__(self, algorithm_config):
        self.algorithm_config = algorithm_config
        self.population = Population(algorithm_config)
        self.generation = 0

