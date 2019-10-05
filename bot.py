#[jump interval, accelaration]

#jump interval will be the base interval between jumps
#accelaration will increase the jump interval
#the speed of the acceleration will be determined by the current score

POPULATION = 100

import random;

def generate_genes():
    gene = []
    for i in range(POPULATION):
        gene.append([random.random(), random.uniform(0.01, 2)])

    return gene


#we gotta have a population of bots playing our game in one generation
def fitness(game_score):
    #fitness will be based on the current score of the game
    pass

def select_genes(gene, fitness_list):    
    #check parents to mate and loop till a new N-sized list is created
    children = []        
    while len(children) < POPULATION or len(children) == 0:
        parent = []
        for i in range(len(fitness_list)):
            if random.randint(1, 100) < fitness_list[i]:
                parent.push(gene[i])
            if len(parent) == 2:
                (child1, child2) = create_child(parent)
                children.push(child1);
                children.push(child2);
    
    return children

def evaluate():
    #check if program has achieved the "goal", in this case their is now outright goal as the game is in theory infinite.
    return False

def create_child(parent):
    select1 = 0
    select2 = 1
    child1 = []
    child2 = []
    for i in range(2):
        child1.append(parent[select1][i])
        child2.append(parent[select2][i])

        if select1 == 1:
            select1 = 0
            select2 = 1
        else:
            select1 = 1
            select2 = 0
    
    return (child1, child2)