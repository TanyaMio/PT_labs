import scipy.optimize as spo
import scipy.stats as sps
import math, random

global m0
global s0
global m1
global a1
global p1
global lowlim
global highlim
global sq


def inter(xi):
    xi = float(xi)
    return f0(xi) - f1(xi)

def f0(xi):
    xi = float(xi)
    return math.exp(-(xi-m0)*(xi-m0)/(2*s0*s0))/(math.sqrt(2*math.pi)*s0)

def f1(xi):
    xi = float(xi)
    return (1/a1)-math.fabs(xi-m1)/math.pow(a1, 2)

def fy(xi):
    xi = float(xi)
    if xi >= lowlim and xi <= highlim:
        res = sps.norm.cdf((xi-m0)/s0) - sps.norm.cdf((lowlim-m0)/s0) - sq
        return res
    else: return 2

def fy1(xi):
    xi = float(xi)
    if xi >= lowlim and xi <= highlim:
        return (f1(xi)+f1(highlim))*highlim-xi/2-sq
    else: return 2

def ftr(xi):
    xi = float(xi)
    if xi >= lowlim and xi <= highlim:
        return xi*f1(xi)/2 - sq
    else: return 2

m0 = float(input("m0 = "))
s0 = float(input("s0 = "))
m1 = float(input("m1 = "))
a1 = float(input("a1 = "))


curr = m1-a1
intersections = []
while curr < m1+a1:
    intersection = spo.fsolve(inter, curr)[0].round(10)
    if not intersection in intersections:
        intersections.append(intersection)
    curr+=a1/20

maxp = sps.norm.cdf((m1+a1-m0)/s0) - sps.norm.cdf((m1-a1-m0)/s0)

print("0 <= p1 <= ", round(maxp, 3))
p1 = float(input("p1 = "))

while p1 < 0 or p1 > maxp:
    print("\nInvalid probability! Please, enter number between 0 and ", maxp)
    p1 = float(input("p1 = "))

p2 = maxp - p1

if m1 > m0:
    prob = p2
else:
    prob = p1

sq = prob
lowlim = m1-a1
highlim = m1+a1
crity = spo.fsolve(fy, m1)[0]

crity = round(crity, 3)
if m1 > m0:
    print("\nCriteria: We choose theory 0 if y < ", crity, " or y > ", m1+a1)
else:
    print("\nCriteria: We choose theory 0 if y > ", crity, "or y < ", m1-a1)

if m0 > m1:
    if crity >= m1:
        p2 = (m1+a1-crity)*f1(crity)/2
    else:
        p2 = 0.5 + (f1(crity)+f1(m1))*(m1 - crity)/2
else:
    if crity <= m1:
        p2 = (crity - m1 + a1) * f1(crity) / 2
    else:
        p2 = 0.5 + (f1(crity)+f1(m1))*(crity-m1)/2


print("\nTheory:\np1 = ", p1, "\np2 = ", p2)

random.seed()
n = 1000
c1 = 0

for i in range(n):
    psy = -6
    for j in range(12):
        psy += random.uniform(0.0, 1.0)
    res = m0 + s0*psy
    if m0 > m1:
        if res <= crity and res >= m1-a1:
            c1 += 1
    else:
        if res >= crity and res <= m1+a1:
            c1 += 1

c2 = 0
for i in range(n):
    r = random.uniform(0.0, 1.0)
    if r <= 0.5:
        res = m1-a1+a1*math.sqrt(2*r)
    else:
        res = m1+a1-a1*math.sqrt(2*(1-r))
    if m0 > m1:
        if res > crity:
            c2 += 1
    else:
        if res < crity:
            c2 += 1

c1 /= n
c2 /= n

print("\nExperiment:\np1 = ", c1, "\np2 = ", c2)
