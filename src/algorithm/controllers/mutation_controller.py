import random


class MutationController:
    def __init__(self, algorithm_configuration):
        self.mutation_rate = algorithm_configuration

    def mutate_population(self, population):
        for individual in population:
            if self.mutation_rate >= random.random():
                individual.mutate()
        return population
