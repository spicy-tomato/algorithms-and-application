import random

# 3x + 2y + z + q = 34
# 1 <= x, y, z, q <= 20

c1 = c2 = 1.5

# Define size of swarm
n_swarm = 10

# Define number of plans
n_plan = 4

# Define number of generations
n_generation = 100

# Inertia
w = 0.7

# Constraint values of particle
max_step = 20
min_step = 1


def objective(plan: list[float]) -> float:
    # f(x, y, z, q) = | 3x + 2y + z + q - 34 | -> 0
    return abs(3 * plan[0] + 2 * plan[1] + plan[2] + plan[3] - 34)


def init() -> (list[list[float]], list[float]):
    swarm: list[list[float]] = []
    for i in range(n_swarm):
        swarm.append([])
        for _ in range(n_plan):
            r = random.uniform(min_step, max_step)
            swarm[i].append(r)

    velocity: list[list[float]] = [[random.uniform(min_step, max_step) for _ in range(n_plan)] for _ in range(n_swarm)]

    return swarm, velocity


def calculate_fitness(swarm: list[list[float]]) -> list[float]:
    return [objective(particle) for particle in swarm]


def find_best(swarm: list[list[float]], fitness: list[float]) -> (list[float], float):
    min_particle = swarm[0]
    min_fitness = fitness[0]

    for i in range(1, n_swarm):
        if fitness[i] < min_fitness:
            min_particle = swarm[i]
            min_fitness = fitness[i]
    return min_particle, min_fitness


def subtract_list(a: list[float], b: list[float]) -> list[float]:
    return [a[i] - b[i] for i in range(len(a))]


def sum_list(*argv: list[float]) -> list[float]:
    result: list[float] = []

    for arg in argv:
        for i in range(len(arg)):
            if i >= len(result):
                result.append(arg[i])
            else:
                result[i] += arg[i]

    return result


def multiply_list(f: float, arr: list[float]) -> list[float]:
    return [f * a for a in arr]


def calculate_velocity(swarm: list[list[float]], old_velocity: list[list[float]], r1: list[float], r2: list[float],
                       particle_best: list[list[float]], swarm_best: list[float]) -> list[list[float]]:
    return [sum_list(multiply_list(w, old_velocity[i]),
                     multiply_list(c1 * r1[i], subtract_list(particle_best[i], swarm[i])),
                     multiply_list(c2 * r2[i], subtract_list(swarm_best, swarm[i])))
            for i in range(n_swarm)]


def calculate_position(position: list[list[float]], velocity: list[list[float]]) -> list[list[float]]:
    new_position = position.copy()
    for i in range(len(new_position)):
        for j in range(len(new_position[i])):
            np = new_position[i][j] + velocity[i][j]
            if min_step <= np <= max_step:
                new_position[i][j] = np
    return new_position


def pso() -> (list[float], float, int):
    gen = 1
    swarm, velocity = init()
    fitness = calculate_fitness(swarm)
    best_swarm, best_fitness = find_best(swarm, fitness)
    p_best_swarm = swarm
    p_best_fitness = fitness

    print(best_fitness)
    print('\nGen 0')
    for i in range(n_swarm):
        print('\t{:2}: {:>3}\t{}'.format(i + 1, objective(swarm[i]), swarm[i]))

    for gen in range(n_generation):
        r1 = [random.uniform(0, 1) for _ in range(n_swarm)]
        r2 = [random.uniform(0, 1) for _ in range(n_swarm)]
        velocity = calculate_velocity(swarm, velocity, r1, r2, p_best_swarm, best_swarm)
        swarm = calculate_position(swarm, velocity)
        fitness = calculate_fitness(swarm)

        for i in range(n_swarm):
            if fitness[i] < p_best_fitness[i]:
                p_best_swarm[i] = swarm[i]
                p_best_fitness[i] = fitness[i]
            if fitness[i] < best_fitness:
                best_fitness = fitness[i]
                best_swarm = swarm[i]

        print('\nGen ', gen + 1)
        for i in range(n_swarm):
            print('\t{:2}: {:>3}\t{}'.format(i + 1, objective(swarm[i]), swarm[i]))

    return best_swarm, best_fitness, gen + 1


best, val, g = pso()
print('\n\nBest plan: ', best)
print('Value: ', val)
print('Generation: ', g)
