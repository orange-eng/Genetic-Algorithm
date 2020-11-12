# Genetic-Algorithm
learing trips in genetic algorithm
## 前言
* 这里是orange研究Genetic Algorithm的一些基本案例，和一些自己的理解~

------
## 目录（后期会根据学习内容增加）
* GA_find_toppoint（已完成）
    * 一个二次函数，通过遗传算法找到最高点
* Travel Sales Person（已完成）
    * 旅行者问题。给定几座城市，旅行者需要找到一条最短路径，经过所有的城市

## 所需环境
* numpy   (任意版本)
* matplotlib（任意版本）

## 算法精华
 如果让我用一句话概括遗传算法: 在程序里生宝宝, 杀死不乖的宝宝, 让乖宝宝继续生宝宝.

```python

def crossover(parent,pop):#父亲母亲交叉配对，就是将父母的基因混合。                            

def select(pop,fitness):#自然选择，适应度较高的得以保留

def get_fitness(pred):     #计算适应度

def translateDNA(pop):    #对DNA进行解码

for _ in range(N_GENERATIONS):
    F_value = F(translateDNA(pop))       # compute function value by extracting DNA
    fitness = get_fitness(F_value)      #获得适应度，越高越好
    pop = select(pop, fitness)          #根据适应度，选择适应度高的pop    
    pop_copy = pop.copy()
    for parent in pop:                          #交叉配对和变异
        child = crossover(parent, pop_copy)     #自交
        parent[:] = child       # parent is replaced by its child

```
