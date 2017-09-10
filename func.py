# function define

from random import choice, choices
from string import digits

from args import *


def generate_gene():
    return ''.join(choice(digits) for i in range(LENGTH_OF_GENES))


def generate_entity():
    return [[generate_gene() for j in range(9)] for i in range(5)]


def generate_population():
    return [i for i in COUNT_OF_GENES]


def rule_one(entity): return (sum([sum([0 if int(j[5]) % 2 else 1 for j in i[0:4]]) for i in entity])) / 15


def rule_two(entity): return (sum([sum([0 if int(j[5]) % 2 else 1 for j in i[0:5]]) for i in entity])) / 20


def rule_three(entity):
    return ((sum([1 if (len(set([i[5:9] for i in chromosome[0:4]]))) <= 2 else 0 for chromosome in entity])) + (
        sum([1 if (len(set([i[5:9] for i in chromosome[4:8]]))) <= 2 else 0 for chromosome in entity]))) / 8


def rule_four(entity): return sum(
    [1 if abs(sum([0 if int(j[5]) % 2 else 1 for j in i for i in entity]) - COUNT_OF_MAJOR) <= 1 else 0 for i in
     entity]) / 5


def fit(entity):
    return (rule_one(entity) + rule_two(entity) + rule_three(entity) + rule_four(entity)) / 5


def cross_entity(entities):
    entity1 = entities[0]
    entity2 = entities[1]
    choose1 = [choices(range(len(entity1))), choices(range(len(entity1[0])))]
    choose2 = [choices(range(len(entity2))), choices(range(len(entity2[0])))]
    picked_one = list(entity1[choose1[0]][choose1[1]])
    picked_two = list(entity2[choose1[0]][choose2[1]])
    picked_two[4:8], picked_one[4:8] = picked_one[4:8], picked_two[4:8]
    entity1[choose1[0]][choose1[1]] = ''.join(picked_one)
    entity1[choose2[0]][choose2[1]] = ''.join(picked_two)


def cross(population):
    for i in range(COUNT_OF_CROSS):
        cross_entity(choices(population, k=2))


# mutate
# get one chromosome -> get two
def mutate_chromosome(chromosome):
    picked_no = choices(range(len(chromosome)), k=2)
    picked_one = list(chromosome[picked_no[0]])
    picked_two = list(chromosome[picked_no[1]])
    picked_two[4:8], picked_one[4:8] = picked_one[4:8], picked_two[4:8]
    chromosome[picked_no[0]] = ''.join(picked_one)
    chromosome[picked_no[1]] = ''.join(picked_two)


def mutate(group):
    for i in range(COUNT_OF_MUTATE):
        mutate_chromosome(choice(choice(group)))
