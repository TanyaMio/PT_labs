import random, numpy

transM = [[0.4, 0.6, 0.0, 0.0, 0.0, 0.0],
          [0.0, 0.4, 0.6, 0.0, 0.0, 0.0],
          [0.0, 0.0, 0.4, 0.6, 0.0, 0.0],
          [0.0, 0.0, 0.0, 0.4, 0.6, 0.0],
          [0.0, 0.0, 0.0, 0.0, 0.4, 0.6],
          [0.2, 0.0, 0.0, 0.0, 0.0, 0.8]]

integrM = []
for l in transM:
    line = []
    s = 0.0
    for num in l:
        s += num
        line.append(s)
    if not s == 1:
        if s+0.001 > 1 and s-0.001<1:
            line[-1] = 1
        else:
            print("Something is wrong in this line: ", l, "\nPlease change the probabilities.")
            break
    integrM.append(line)

if len(integrM) == 6:
    print("Theory:")
    a = numpy.array([[1, 1, 1, 1, 1, 1],
                     [-1 + transM[0][0], transM[1][0], transM[2][0], transM[3][0], transM[4][0], transM[5][0]],
                     [transM[0][1], -1 + transM[1][1], transM[2][1], transM[3][1], transM[4][1], transM[5][1]],
                     [transM[0][2], transM[1][2], -1 + transM[2][2], transM[3][2], transM[4][2], transM[5][2]],
                     [transM[0][3], transM[1][3], transM[2][3], -1 + transM[3][3], transM[4][3], transM[5][2]],
                     [transM[0][4], transM[1][4], transM[2][4], transM[3][4], -1 + transM[4][4], transM[5][4]]])
    b = numpy.array([[1],
                     [0],
                     [0],
                     [0],
                     [0],
                     [0]])

    c = numpy.linalg.solve(a, b)

    for i in range(len(c)):
        print("p", i + 1, " = ", c[i][0].round(3))

    print("\nExperiment:")
    states = [0, 1, 2, 3, 4, 5]
    counters = [0, 0, 0, 0, 0, 0]

    random.seed()
    curr = random.choice(states)

    r = 0
    n = 1000
    for i in range(n):
        r = random.uniform(0.0, 1.0)
        if r <= integrM[curr][0]:
            curr = 0
        elif r <= integrM[curr][1]:
            curr = 1
        elif r <= integrM[curr][2]:
            curr = 2
        elif r <= integrM[curr][3]:
            curr = 3
        elif r <= integrM[curr][4]:
            curr = 4
        else:
            curr = 5
        counters[curr] += 1

    for i in range(len(counters)):
        print("p", i+1, " = ", counters[i]/n)
