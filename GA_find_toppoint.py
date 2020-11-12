import numpy as np
import matplotlib.pyplot as plt
DNA_SIZE = 10            # DNA length       DNA长度
POP_SIZE = 100           # population size  多少个人
CROSS_RATE = 0.8         # mating probability (DNA crossover)   有80%可以交叉配对
MUTATION_RATE = 0.003    # mutation probability                 有3%的概率发生0和1交换
N_GENERATIONS = 20                                            #循环了多少次
X_BOUND = [0, 5]         # x upper and lower bounds

pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))   # initialize the pop DNA

#--------------------------------------------------------------------------------函数
#定义一个曲线的方程 返回某一个点的高度
def F(x): return np.sin(10*x)*x + np.cos(2*x)*x                                 # to find the maximum of this function

def crossover(parent,pop):                                                      #parent是一个数字（母亲），pop是一个10位向量
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, POP_SIZE, size=1)                             # 再随机选出一个适应度高的父亲
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)   #在10个位置中随机选择交叉点
        parent[cross_points] = pop[i_, cross_points]                            # 在指定的交叉点上，换成父亲，其余依然为母亲
    return parent

def select(pop,fitness):
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,
                           p=fitness/fitness.sum())                             #p：一个一维数组，与a的元素一一对应，给出相应元素被采样的概率。
    return pop[idx]                                                             #选择适应度比较高的。导致适应度高的越来越多

def get_fitness(pred):                                                          #计算适应度
    return pred + 1e-3 - np.min(pred)                                           #所有的数字都减去最小值，使得所有值都一定大于0， +1e-3是为了防止出现0的情况

def translateDNA(pop):
    return (pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2**DNA_SIZE-1)) * X_BOUND[1]      # 意思是矩阵pop 乘以矩阵[512 256 128  64  32  16   8   4   2   1]
    #该函数把所有权重压缩到[0,5]之间
    # **表示平方
    #dot()函数是矩阵乘,而*则表示逐个元素相乘
	#np.arange()函数返回一个有终点和起点的固定步长的排列
	#pop.dot(2 ** np.arange(DNA_SIZE)[::-1])已经转换成十进制
	#但是需要归一化到0~5,如有1111这么长的DNA,要产生的十进制数范围是[0, 15],
    # 而所需范围是 [-1, 1],就将[0,15]缩放到[-1,1]这个范围
	#a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。
    # 所以你看到一个倒序np.arange(DNA_SIZE)[::-1]得到10,9,8,...,0
#---------------------------------------------------------------------------------------------------------------
'''
F_values = F(translateDNA(pop))    # compute function value by extracting DNA
#print(F_values)
Fitness = get_fitness(F_values)

# print(Fitness)
# print(select(pop,Fitness))

pop = select(pop, Fitness)          #根据适应度，选择适应度高的pop    
print(pop)
pop_copy = pop.copy()
i=1
for parent in pop:                          #交叉配对和变异
    
    child = crossover(parent, pop_copy)     #自交
    #print(child,i)
    i = i+1
    # child = mutate(child)
    # parent[:] = child       # parent is replaced by its child

# print(pop)
# print(2**np.arange(DNA_SIZE)[::-1])
# print(pop.dot(2 ** np.arange(DNA_SIZE)[::-1]))
# print((2**DNA_SIZE-1))
# print(translateDNA(pop))
'''
#------------------------------------------------------------------------------------

plt.ion()                                           # something about plotting  使matplotlib的显示模式转换为交互（interactive）模式
x = np.linspace(*X_BOUND, 200)                      #在[0,5]之间取200个点
plt.plot(x, F(x))

for _ in range(N_GENERATIONS):
    F_value = F(translateDNA(pop))       # compute function value by extracting DNA 
    if 'sca' in globals(): sca.remove()
    sca = plt.scatter(translateDNA(pop), F_value, s=200, lw=0, c='red', alpha=0.5); plt.pause(0.05)
    
    fitness = get_fitness(F_value)      #获得适应度，越高越好
    pop = select(pop, fitness)          #根据适应度，选择适应度高的pop    
    pop_copy = pop.copy()
    for parent in pop:                          #交叉配对和变异
        child = crossover(parent, pop_copy)     #自交
        parent[:] = child       # parent is replaced by its child

plt.ioff(); plt.show()


