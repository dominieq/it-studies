
def adjustPlot(plt, ax, solutions, title):
    X = [s[0] for s in solutions]
    Y = [s[1] for s in solutions]
    plt.plot([0,1],[1,0], marker='', linestyle='--', lw=1.0, color='blue')
    plt.plot([0,2],[2,0], marker='', linestyle='-', lw=1.0, color='blue')
    plt.plot(X, Y, marker='o', linestyle='', markersize=2, mfc = 'black' ,mec='black')
    ax.set_xlim(0.0, 2.2)
    ax.set_ylim(0.0, 2.2)
    plt.xlabel("$f_{1}$")
    plt.ylabel("$f_{2}$")
    plt.title(title)
    plt.grid(True)
    
def displaySnapshots(plt, plotEvery, plotSize, snapshots): 
    GENS = [0] + [plotEvery * (i+1) for i in range(8)]
    IDX = [i for i in range(9)]

    plt.figure(figsize=(plotSize, plotSize))

    for i, generation, snapshot in zip(IDX, GENS, snapshots):
        ax = plt.subplot(3, 3, i + 1)
        solutions = [[s.objective_vector[0], s.objective_vector[1]] for s in snapshot]
        adjustPlot(plt, ax, solutions, "Generation = {}".format(generation))
    plt.show()
    
def plotQualityIndicators(plt, GD, IGD):
    plt.figure(figsize=(10, 6))
    ax = plt.subplot(1,1, 1)
    plt.plot(GD, label="GD")
    plt.plot(IGD, label="IGD")
    ax.set_ylim(0.0, 0.6)
    plt.xlabel("generation")
    plt.ylabel("quality")    
    plt.grid(True)
    plt.legend()
    plt.show()
    
def getGenerationalDistance(population):
    total = 0.0
    for s in population:
        alpha = 1.0 / (s.objective_vector[0] + s.objective_vector[1])
        total += ((s.objective_vector[0] * (1-alpha))**2 + (s.objective_vector[1] * (1-alpha))**2)**0.5
    return total/len(population)

def getInvertedGenerationalDistance(population, N):
    dataSet = [[1.0/N * i, 1.0 - 1.0/N * i] for i in range(N + 1)]
    total = 0.0 
    for p in dataSet:
        m = 100000.0
        for s in population:
            d = ((s.objective_vector[0] - p[0])**2 + (s.objective_vector[1] - p[1])**2)**0.5
            if d < m:
                m = d
        total += m
    return total / N

