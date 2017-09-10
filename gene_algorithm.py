#!/bin/python3
# replace this with your $PYTHON_PATH or just simple run by execute python3 gene_algorithm

# created by @author stan<holdmylife@qq.com>

# algorithm started

from func import generate_population, fit, choice, mutate, cross

from args import *

# initial group
origin_population = generate_population()

population_dict = {origin_population: fit(origin_population) for i in
                   origin_population}  # create population fit reference

# begin iterate
while True:  # replace True with convergence threshold or iterate number
    population_dict = sorted(population_dict.items(), key=lambda x: x[1])

    top_quarter_population = {i: population_dict[i] for i in
                              list(population_dict.keys())[:int(len(population_dict) / 4)]}
    random_m_population = [choice(population_dict) for i in range(M)]

    # merge
    top_quarter_population.update(random_m_population)
    population_dict = top_quarter_population

    # cross and mutate
    mutate(population_dict)
    cross(population_dict)