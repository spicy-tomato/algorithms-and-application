import random

# 3x + 2y + z + q = 34
# 1 <= x, y, z, q <= 20

# Define Number of generations
n_generation = 1000

# Define the population size
n_population = 6

# Crossover rate
r_crossover = 0.8

# Mutation rate
r_mutation = 0.02

# Reproduce rate
r_reproduce = 0.18

# Gene size
n_gene = 4

# constraint values of chromosome
max_chromosome = 20
min_chromosome = 1


def objective(gene: list[int]) -> int:
    # f(x, y, z, q) = | 3x + 2y + z + q | - 34
    return abs(3 * gene[0] + 2 * gene[1] + gene[2] + gene[3] - 34)


def init() -> list[list[int]]:
    population: list[list[int]] = []
    for i in range(n_population):
        population.append([])
        for j in range(n_gene):
            r = random.randint(min_chromosome, max_chromosome)
            population[i].append(r)

    return population


def evaluate(population) -> list[int]:
    return [objective(c) for c in population]


def selection(population: list[list[int]], scores: list[int]) -> None:
    temp = scores.copy()
    temp.sort()
    threshold = temp[round(n_population * (1 - r_reproduce))]

    for i in range(n_population):
        if scores[i] > threshold:
            # reproduction
            reproduce_candidate_index = random.randint(0, n_population - 1)
            population[i] = population[reproduce_candidate_index].copy()


def crossover(p1: list[int], p2: list[int], ):
    pt = random.randint(1, n_gene - 1)

    c1 = p1[:pt] + p2[pt:]
    c2 = p2[:pt] + p1[pt:]

    return [c1, c2]


def mutation(gene: list[int]):
    if random.random() <= r_mutation:
        index = random.randint(0, n_gene - 1)
        new_value = gene[index]

        while new_value == gene[index]:
            new_value = random.randint(min_chromosome, max_chromosome)

        gene[index] = new_value


def genetic_algorithm():
    population = init()
    best_generation = 0
    best_value = objective(population[0])
    gen = 0

    for gen in range(n_generation):
        print('\nGen', gen + 1)
        for i in range(n_population):
            print('\t{:2}: {:>3}\t{}'.format(i+1, objective(population[i]), population[i]))

        children: list[list[int]] = []

        # Evaluate
        scores = evaluate(population)

        # Check for best solution
        for i in range(n_population):
            if scores[i] < best_value:
                best_generation = population[i]
                best_value = scores[i]

        selection(population, scores)

        for i in range(0, n_population, 2):
            p1, p2 = population[i], population[i + 1]
            for c in crossover(p1, p2):
                mutation(c)
                children.append(c)

        population = children

        if best_value == 0:
            break

    return [best_generation, best_value, gen + 1]


best, val, g = genetic_algorithm()
print('\n\nBest genomes: ', best)
print('Value: ', val)
print('Generation: ', g)
